#!/usr/bin/python3
# coding: utf-8
# whoosh 使用流程: 1. 创建 schema 2. 索引生成 3. 索引查询
# https://my.oschina.net/u/2351685/blog/603079
# https://github.com/fxsjy/jieba/blob/master/test/test_whoosh.py
from whoosh.fields import ID, TEXT, Schema
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh import qparser
# 执行前保证 ./tmp/ 目录存在, 否则会报错
##################################################################
## 0. 先写一个简洁的版本, 后面是讲解
from whoosh.index import create_in
from whoosh.fields import TEXT, ID, Schema  # 只引入这两个就够了
schema = Schema(title=TEXT(stored=True), content=TEXT)
ix = create_in('./tmp', schema)               # 存储 schema 信息至 ./tmp/; ** 这个只能执行一遍, 否则会报 LockError **
writer = ix.writer()                          # 按照 schema 定义信息, 增加需要建立索引的文档
writer.add_document(title='hello', content='hello world')
writer.add_document(title='world', content='world hello')
writer.commit()                               # searcher() 要写到 commit() 后面
searcher = ix.searcher()                      # 创建一个检索器; 最好用 with ix.searcher() as searcher: 来写, 这里只是为了方便
## 第一种检索方式:
print(searcher.find('content', 'hello world').fields(0))  # {'title': 'hello'}; TEXT 会存储位置信息, 支持短语检索
print(searcher.find('content', 'hello world')[1].fields())  # {'title': 'world'};
## 另一种检索方式: Construct query objects directly
from whoosh.query import *
myquery = And([Term("content", "hello"), Term("content", "world")])
print(searcher.search(myquery).fields(1))  # {'title': 'world'}; 和上面的结果一样
## 第三种检索方式: Parse a query string; 一般最好用这种方法做
from whoosh.qparser import QueryParser
parser = QueryParser("content", ix.schema)
myquery = parser.parse('hello world')
print(len(searcher.search(myquery)))  # 2
for hit in searcher.search(myquery): print(hit.highlights('title'))  # 可以高亮输出指定部分, 见 ./l2_jieba-中文.py
for hit in searcher.search(myquery): print(hit.fields())  # 因为 TEXT 检索不到的, 所以没有输出
for hit in searcher.search(myquery, limit=100): print(hit.fields())  # 默认一次返回 10 个, 这里改为 100 个
# 第三种检索方式支持: AND OR NOT, group terms together into clauses with parentheses, do range, prefix,
#                     and wilcard queries, and specify different fields to search
# By default it joins clauses together with AND
print(parser.parse("render shade animate"))  # (content:render AND content:shade AND content:animate)
# 交互式环境输出: And([Term("content", "render"), Term("content", "shade"), Term("content", "animate")])
print(parser.parse("render OR (title:shade content:animate)"))  # (content:render OR (title:shade AND content:animate))
# 交互式环境输出: Or([Term("content", "render"), And([Term("title", "shade"), Term("keyword", "animate")])])
print(parser.parse("rend*"))  # content:rend*
# 交互式环境输出: Prefix("content", "rend")
## search_page(query, pagenum, pagelen=10, **kwargs)
results = searcher.search_page(myquery, 2, 1); print(results[0])  # <Hit {'title': 'world'}>; 每页显示一个结果, 第 2 页
results = searcher.search_page(myquery, 1, 1); print(results[0])  # <Hit {'title': 'hello'}>; 每页显示一个结果, 第 1 页

##################################################################
## 1. 创建 schema
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)  # stored 为 True 表示能够被检索
# All keyword arguments to the constructor are treated as fieldname = fieldtype pairs.
# The fieldtype can be an instantiated FieldType object, or a FieldType sub-class
#     (in which case the Schema will instantiate it with the default constructor before adding it).
# For example: s = Schema(content=TEXT, title=TEXT(stored = True), tags=KEYWORD(stored = True))
# 返回索引结果的时候一般只想得到文章标题和路径, 文章内容是想要点进去看; 所以 content 没有 stored=True
from whoosh import fields
# 打印支持的变量类型
print([item for item in dir(fields)[:10] if item.isupper()])  # ['BOOLEAN', 'COLUMN', 'DATETIME', 'ID', 'IDLIST', 'KEYWORD']
print(len(schema.items()))  # 3
print(schema.items()[0])  # ('content', TEXT(format=Positions(boost=1.0), scorable=True, stored=False, unique=None))
print(schema.items()[1])  # ('path', ID(format=Existence(boost=1.0), scorable=None, stored=True, unique=False))
print(schema.items()[2])  # ('title', TEXT(format=Positions(boost=1.0), scorable=True, stored=True, unique=None))
print(schema.names())  # ['content', 'path', 'title']; Returns a list of the names of the fields in this schema.
print(schema.scorable_names())  # ['content', 'title']; Returns a list of the names of fields that store field lengths.
print(schema.stored_names())  # ['path', 'title']; Returns a list of the names of fields that are stored.
print(schema.has_scorable_fields())  # True
##################################################################
## 2. 索引生成
## create_in(dirname, schema, indexname=None)
## Convenience function to create an index in a directory. Takes care of creating a FileStorage object for you.
ix = create_in('./tmp', schema)  # 存储 schema 信息至 ./tmp/; ** 这个只能执行一遍, 否则会报 LockError **
print(type(ix))  # <class 'whoosh.index.FileIndex'>
print(ix.schema)  # <Schema: ['content', 'path', 'title']>
## writer(procs=1, **kwargs): Returns an IndexWriter object for this index.
writer = ix.writer()  # 按照 schema 定义信息, 增加需要建立索引的文档
print(type(writer))  # <class 'whoosh.writing.SegmentWriter'>
print(writer.schema)  # <Schema: ['content', 'path', 'title']>
## add_document(**fields): The keyword arguments map field names to the values to index/store
writer.add_document(title="First document", path="/a", content="This is the first document we've added!")
writer.add_document(title="Second document", path="/b", content="The second one is even more interesting!")
## commit(mergetype=None, optimize=None, merge=None) Finishes writing and saves all additions and changes to disk.
writer.commit()  # 提交结果, 写会磁盘
##################################################################
## 3. 索引查询
## open_dir(dirname, indexname=None, readonly=False, schema=None)
## Convenience function for opening an index in a directory. Takes care of creating a FileStorage object for you.
## dirname is the filename of the directory in containing the index. indexname is the name of the index to create;
## you only need to specify this if you have multiple indexes within the same storage object.
ix = open_dir('./tmp')  # 直接用上面的 ix 也可以
## searcher(**kwargs): Returns a Searcher object for this index. Keyword arguments are passed to the Searcher object's constructor.
searcher = ix.searcher()  # 创建一个检索器; 最好用 with ix.searcher() as searcher: 来写, 这里只是为了方便

## 查询方法一:
## __init__(self, fieldname, schema, plugins=None)
# A hand-written query parser built on modular plug-ins. The default configuration implements a powerful fielded query language similar to Lucene.
# fieldname: the default field -- the parser uses this as the field for any terms without an explicit field.
# schema: a :class:`whoosh.fields.Schema` object to use when parsing. The appropriate fields in the schema will be used to
#     tokenize terms/phrases before they are turned into query objects.
#     You can specify None for the schema to create a parser that does not analyze the text of the query, usually for testing purposes.
parser = QueryParser("content", ix.schema)  # ix.schema 和 schema 是相同的东西
print(len(parser.plugins), parser.plugins)  # 11
# [<whoosh.qparser.plugins.WhitespacePlugin>, <whoosh.qparser.plugins.WhitespacePlugin>, <whoosh.qparser.plugins.SingleQuotePlugin>,
#  <whoosh.qparser.plugins.FieldsPlugin>,     <whoosh.qparser.plugins.WildcardPlugin>,   <whoosh.qparser.plugins.PhrasePlugin>,
#  <whoosh.qparser.plugins.RangePlugin>,      <whoosh.qparser.plugins.GroupPlugin>,      <whoosh.qparser.plugins.OperatorsPlugin>,
#  <whoosh.qparser.plugins.BoostPlugin>,      <whoosh.qparser.plugins.EveryPlugin>]
## default_set(): Returns the default list of plugins to use.
print(len(parser.default_set()), parser.default_set())  # 10
# [<whoosh.qparser.plugins.WhitespacePlugin>, <whoosh.qparser.plugins.SingleQuotePlugin>, <whoosh.qparser.plugins.FieldsPlugin>,
#  <whoosh.qparser.plugins.WildcardPlugin>,   <whoosh.qparser.plugins.PhrasePlugin>,      <whoosh.qparser.plugins.RangePlugin>,
#  <whoosh.qparser.plugins.GroupPlugin>,      <whoosh.qparser.plugins.OperatorsPlugin>,   <whoosh.qparser.plugins.BoostPlugin>,
#  <whoosh.qparser.plugins.EveryPlugin>]
parser.remove_plugin_class(whoosh.qparser.plugins.WildcardPlugin)
print(len(parser.plugins), len(parser.default_set()))  # 10 10
parser.add_plugin(qparser.PrefixPlugin)
print(len(parser.plugins), len(parser.default_set()))  # 11 10
## parse(text, normalize=True, debug=False) Parses the input string and returns a :class:`whoosh.query.Query` object/tree.
query = parser.parse('document')
## search(q, **kwargs) Runs a :class:`whoosh.query.Query` object on this searcher and returns a :class:`Results` object.
# See :doc:`/searching` for more information.
results = searcher.search(query)  # 检索 "content" 中出现 "document"
print(results)  # <Top 1 Results for Term('content', 'document') runtime=0.0015511049998622184>
print(type(results))  # <class 'whoosh.searching.Results'>

## 查询方法二: 上面两行是只用方法, 下面一行也形
## find(defaultfield, querystring, **kwargs)
results = searcher.find("title", "document")  # 检索标题中出现 'document' 的文档
print(results)  # <Top 2 Results for Term('title', 'document') runtime=0.0008875329999682435>
print(type(results))  # <class 'whoosh.searching.Results'>; 和上面第一种方法得到的结果一样

# searcher.find() 使用方便, 但是定制性不好
# searcher.search() 使用麻烦, 但是很多功能可以添加
##################################################################
## 4. 结果处理
# fields(n): Returns the stored fields for the document at the ``n`` th position
print(results.fields(0))  # {'path': '/a', 'title': 'First document'}; 因为 Schema(content=TEXT), 没有 sorted=True, 所以没有显示出来
print(results[0])  # <Hit {'path': '/a', 'title': 'First document'}>
print(type(results[0]))  # <class 'whoosh.searching.Hit'>
firstdoc = results[0].fields()  # 检索出来的第一个结果，数据格式为 dict{'title':.., 'content':...}
print(firstdoc)  # {'path': '/a', 'title': 'First document'}
print(results[0].highlights("title"))  # First <b class="match term0">document</b>; 高亮标题中的检索词
print(results[0].score)  # 0.5945348918918356; bm25 分数
