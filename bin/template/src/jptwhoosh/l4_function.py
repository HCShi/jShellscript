#!/usr/bin/python3
# coding: utf-8
##################################################################
## 王斌老师课程大作业, 后端接口实现, 一堆垃圾代码...
import bson
import pickle
import whoosh
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
def init_search():
    ix = open_dir('./tmp-homework-back')  # 在 ./tmp-homework-back 中进行备份
    searcher = ix.searcher()
    parser = QueryParser("news_body", schema=ix.schema)
    parser.add_plugin(whoosh.qparser.plugins.WildcardPlugin)
    items = list(bson.decode_file_iter(open('./tmp.bson', 'rb')))
    items_dic = dict((item['news_id'], item) for item in items)
    with open('tmp_document-dict.pkl', 'rb') as f:
        documents_dic = pickle.load(f)
    with open('tmp_tfidf_dic.pkl', 'rb') as f:
        tfidf_dic = pickle.load(f)
    with open('tmp_wordlist.pkl', 'rb') as f:
        wordlist = pickle.load(f)
    with open('tmp_idflist.pkl', 'rb') as f:
        idflist = pickle.load(f)
    word_idf_dic = dict(zip(wordlist, idflist))
    return searcher, parser, items, items_dic, documents_dic, tfidf_dic, wordlist, word_idf_dic
def search(query):  # 关键词检索, 通配符检索
    q = parser.parse(query)
    results = searcher.search(q)
    return results
def search_by_time(query):  # 按时间排序
    return sorted(search(query), key=lambda x: x['news_time'])
def search_by_hot(query):  # 按热度排序
    return sorted(search(query), key=lambda x: x['news_total'])
def search_by_revelance(query):  # 按相关度排序
    return sorted(search(query), key=lambda x: x.score)
def complete_query(string): # 查询自动补齐
    return [item for item in wordlist if item.startswith(string)][:10]
def recommend_news(query):  # 相关搜索推荐; 返回相关文档中的 tfidf/idf 最大的词项
    docs = list(sorted(search(query), key=lambda x: x.score))[:10]
    # docs = list(sorted(search('苹果'), key=lambda x: x.score))[:10]
    # print([list(sorted(tfidf_dic[item['news_id']], key=lambda x: tfidf_dic[item['news_id']][x]))[-1] for item in docs])
    # print([list(sorted(tfidf_dic[item['news_id']], key=lambda x: x]))[-1] for item in docs])
def search_with_snippet(query):  # snippet 生成
    results = search(query)
    return [hit.highlights('news_body') for hit in results]
def preview(news_id):  # 结果预览
    return ' '.join(items_dic[news_id]['news_body'])
def similar_news(news_id):  # 相似新闻; 找同一篇新闻中 tfidf 最高的词再进行搜索
    items = sorted(tfidf_dic[news_id], key=lambda x: tfidf_dic[news_id][x])[-3:]
    return [item for item in search(''.join(items))]
def hotest_news(num):  # 最热社会新闻
    return list(sorted(items, key=lambda x: x.get('news_total', 0)))[:num]
if __name__ == '__main__':
    searcher, parser, items, items_dic, documents_dic, tfidf_dic, wordlist, word_idf_dic = init_search()
    # test 通配符, 关键词
    for hit in search('苹果'): print(hit)
    # test search_by_time
    for hit in search('苹果'): print(hit['news_time'])
    for hit in search_by_time('苹果'): print(hit['news_time'])
    # test search_by_hot
    for hit in search('苹果'): print(hit['news_total'])
    for hit in search_by_hot('苹果'): print(hit['news_total'])
    # test search_by_revelance
    for hit in search('苹果'): print(hit.score)
    for hit in search_by_revelance('苹果'): print(hit.score)
    # test complete_query
    print(complete_query('苹'))  # ['苹果', '苹果公司', '苹果园', '苹果树', '苹果电脑', '苹果醋']
    # test search_with_snippet
    print(search_with_snippet('苹果'))
    # test preview
    print(preview('fxzczfc6652525'))
    # test similar_news
    print(similar_news('fxzczfc6652525')[0]['news_body'])
    print(similar_news('fxzczfc6652525')[1]['news_body'])
    # test hotest_news()
    for hit in hotest_news(10): print(hit['news_title'])
    for hit in hotest_news(10): print(hit['news_body'])
    for hit in hotest_news(10): print(hit['news_time'])
