#!/usr/bin/python3
# coding: utf-8
## 读数据库
import bson
import sys
print(sys.modules.keys())
from whoosh.index import create_in, open_dir
from whoosh.fields import TEXT, ID, STORED, KEYWORD, NUMERIC, Schema
from whoosh.qparser import QueryParser
from jieba.analyse import ChineseAnalyzer
import jieba
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
analyzer = ChineseAnalyzer()
##################################################################
## 分析 bson 数据
items = list(bson.decode_file_iter(open('./tmp.bson', 'rb'))); print(len(items))  # 14128; 读取 BSON 文件
print(items[0].keys())  # dict_keys(['_id', 'news_id', 'news_url', 'news_from', 'news_channel', 'news_title', 'news_source', 'news_time', 'news_body', 'news_keywords', 'flag', 'news_show', 'news_total'])
print(items[0]['news_id'])  # fxzczfc6652525
print(items[0]['news_keywords'])  # ['陕西', '公厕爆炸']
print(items[0]['news_show'])  # 0
print(set([len(item['news_title']) for item in items if item.get('news_title', 0) != 0]))
# {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31}; 这些都是 str 长度
print(set([len(item['news_body']) for item in items])) # {0, 1, 2, 3, 4, 5, ..., 159, 169, 178, 244}; 居然还能分成 244 段...
print(set([len([''.join(item['news_body'])]) for item in items])) # {1}; 清净多了
print(set([str(item.keys()) for item in items]))  # 好多缺失值
# {"dict_keys(['_id', 'news_id', 'news_url', 'news_from', 'news_channel', 'news_title', 'news_source', 'news_time', 'news_body', 'news_keywords', 'flag'])",
#  "dict_keys(['_id', 'news_id', 'news_url', 'news_from', 'news_channel', 'news_title', 'news_source', 'news_time', 'news_body', 'news_keywords', 'flag', 'news_show', 'news_total'])",
#  "dict_keys(['_id', 'news_id', 'news_url', 'news_from', 'news_channel', 'news_title', 'news_source', 'news_time', 'news_body', 'flag', 'news_show', 'news_total'])",
#  "dict_keys(['_id', 'news_id', 'news_url', 'news_from', 'news_channel', 'news_title', 'news_time', 'news_body', 'news_keywords', 'flag', 'news_show', 'news_total'])",
#  "dict_keys(['_id', 'news_id', 'news_url', 'news_from', 'news_channel', 'news_title', 'news_body', 'flag', 'news_show', 'news_total'])",
#  "dict_keys(['_id', 'news_id', 'news_url', 'news_from', 'news_channel', 'news_body', 'flag', 'news_show', 'news_total'])"}
print(items[0]['news_total'])  # 0
# news_id 新闻唯一标识
# news_url 新闻url
# news_from 这个新闻是从哪个新闻网上爬下来的，比如这个就是sina
# news_channel 新闻频道
# news_title 新闻标题
# news_source 新闻的原网站
# news_time 时间
# news_body 新闻正文
# news_keywords 关键词
# flag news 统一都是
# news_show 评论数
# news_total 评论参与人数
##################################################################
## 建立反向索引字典
print([item['_id'] for item in items[:5]])  # [ObjectId('5a2071f060382362972a3633'), ObjectId('5a2071f160382362972a3637'), ObjectId('5a2071f260382362972a3639'), ObjectId('5a2071f260382362972a3640'), ObjectId('5a2071f360382362972a3644')]
print([item['news_id'] for item in items[:5]])  # ['fxzczfc6652525', 'fxzczfc6668350', 'fxzczff3648988', 'fxzczff3529321', 'fxzkhfx4602766']
# 两个 id 都不是整数的
items_dic = dict((item['news_id'], item) for item in items)
print(len(items_dic.keys()))  # 14128
print(items_dic['fxzczfc6652525'])  # {'_id': ObjectId('5a2071f060382362972a3633'), 'news_id': 'fxzczfc6652525', 'news_url': '... }
##################################################################
## 在每篇文档中构建每个词 tf-idf 权重词典
documents_dic = dict((item['news_id'], ' '.join(jieba.lcut(''.join(item['news_body'])))) for item in items)  # 也很慢啊...; 2min
print(list(documents_dic.values())[0])  # 原 标题 ： 横山 发生 一起 公厕 垮塌 事故 1....; 用空格分开的 str
with open('tmp_document-dict.pkl', 'wb') as f: pickle.dump(documents_dic, f)
with open('tmp_document-dict.pkl', 'rb') as f: documents_dic = pickle.load(f)  # 进行了一下保存
print(list(documents_dic.values())[0])  # ['原', '标题', '：', '横山', '发生', '一起', '公厕', ...]
## 建立词袋
count_vec = CountVectorizer()
X = count_vec.fit_transform(documents_dic.values()); print(X)  # toarray() 会爆内存...
print(type(X))  # <class 'scipy.sparse.csr.csr_matrix'>
print(X[0].nonzero()[1])  # 不是 0 的项
print(X.shape[0])  # 14128
wordlist = count_vec.get_feature_names(); print(len(wordlist), wordlist[:5])  # 172365 ['00', '000', '000002', '00006', '00008']
with open('tmp_wordlist.pkl', 'wb') as f: pickle.dump(wordlist, f)
with open('tmp_wordlist.pkl', 'rb') as f: wordlist = pickle.load(f)
print(list(count_vec.vocabulary_)[:5])  # ['标题', '横山', '发生', '一起', '公厕']
## tfidf
tfidf_tra = TfidfTransformer()
tfidf = tfidf_tra.fit_transform(X)  # toarray 也会爆内存
print(type(tfidf[0]))  # <class 'scipy.sparse.csr.csr_matrix'>
print(tfidf[0])
print(tfidf.shape[0])  # 14128
print(tfidf[0, 77671])  # 0.0834230652963
print(tfidf[0].nonzero()[1])
idflist = tfidf_tra.idf_; print(len(idflist), idflist[:5])  # 172365 [ 5.78530008  8.25339961  9.86283752  9.86283752  9.86283752]
with open('tmp_idflist.pkl', 'wb') as f: pickle.dump(idflist, f)
with open('tmp_idflist.pkl', 'rb') as f: idflist = pickle.load(f)
print(idflist[count_vec.vocabulary_['标题']])  # 1.52656686567
print(list(wordlist[idx] for idx in tfidf[0].nonzero()[1]))
## 根据文档来统计每个词的 tfidf
tfidf_array = [[tfidf[i, idx] for idx in tfidf[i].nonzero()[1]] for i in range(tfidf.shape[0])]  # 计算挺慢的
print(len(tfidf_array), tfidf_array[0])  # 14128
## 将 tfidf 写回字典
tfidf_values = [dict(zip(list(wordlist[idx] for idx in tfidf[i].nonzero()[1]), tfidf_array[i])) for i in range(tfidf.shape[0])]
tfidf_dic = dict(zip(documents_dic.keys(), tfidf_values))
print(list(tfidf_dic.values())[0])
with open('tmp_tfidf_dic.pkl', 'wb') as f: pickle.dump(tfidf_dic, f)
with open('tmp_tfidf_dic.pkl', 'rb') as f: tfidf_dic = pickle.load(f)  # 进行了一下保存
##################################################################
## 建索引
schema = Schema(news_id=STORED, news_url=STORED, news_from=STORED, news_channel=STORED, news_title=TEXT(stored=True, analyzer=analyzer),
                news_source=STORED, news_time=STORED, news_body=TEXT(stored=True, analyzer=analyzer),
                news_keywords=STORED, flag=STORED, news_show=STORED, news_total=STORED)
ix = create_in("./tmp-homework", schema)
writer = ix.writer()
for item in items:
    writer.add_document(news_id=item.get('news_id', 'null'), news_url=item.get('news_url', 'null'), news_from=item.get('news_from', 'null'),
                        news_channel=item.get('news_channel', 'null'), news_title=item.get('news_title', 'null'), news_source=item.get('news_source', 'null'),
                        news_time=item.get('news_time', 'null'), news_body=''.join(item.get('news_body', 'null')), news_keywords=item.get('news_keywords', ['null']),
                        flag=item.get('flag', 'null'), news_show=item.get('news_show', '0'), news_total=item.get('news_total', '0'))
writer.commit()  # 还是比较慢的, 跑了 3min, 先保存一下
ix = open_dir('./tmp-homework-back')  # 在 ./tmp-homework-back 中进行备份
##################################################################
## 进行查询
searcher = ix.searcher()
parser = QueryParser("news_body", schema=ix.schema)
q = parser.parse('公厕')
results = searcher.search(q); print(results)
for hit in results: print(hit.highlights("news_body"))
