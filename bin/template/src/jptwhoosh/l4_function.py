#!/usr/bin/python3
# coding: utf-8
##################################################################
## 王斌老师课程大作业, 后端接口实现, 一堆垃圾代码...
## 后端接口写成 class 的方式比较方便...
import bson
import pickle
import whoosh
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from gensim.models import word2vec
from tmp_classify import test
from collections import Counter
import pymongo
class Search_Engine(object):
    def __init__(self):
        self.ix = open_dir('./tmp-homework')  # 在 ./tmp-homework-back 中进行备份
        self.searcher = self.ix.searcher()
        self.parser = QueryParser("news_body", schema=self.ix.schema)
        self.parser.add_plugin(whoosh.qparser.plugins.WildcardPlugin)
        self.items = list(bson.decode_file_iter(open('./tmp_news/sina.bson', 'rb')))
        self.items_dic = dict((item['news_id'], item) for item in self.items)
        with open('tmp_tfidf_dic.pkl', 'rb') as f:
            self.tfidf_dic = pickle.load(f)
        with open('tmp_wordlist.pkl', 'rb') as f:
            self.wordlist = pickle.load(f)
        with open('tmp_idflist.pkl', 'rb') as f:
            self.idflist = pickle.load(f)
        self.word_idf_dic = dict(zip(self.wordlist, self.idflist))
        # self.word2vec_model = word2vec.Word2Vec.load('/media/coder352/Documents/Share/data_set/word2vec/word2vec_wx')
        self.word2vec_model = word2vec.Word2Vec.load('/home/coder352/github/jData/Word2Vec/Word2Vec_Chinese_Model/word2vec_wx')
        # MongoDB Comment
        self.client = pymongo.MongoClient()  # client = MongoClient('localhost', 27017); 连接到 MongoDB 的默认主机与端口
        self.db = self.client["news"]  # mongorestore -h 127.0.0.1 -d test tmp_news; 这个命令导入的...
        self.db_comments = self.db.sinacmt
    def search(self, query):  # 关键词检索, 通配符检索
        q = self.parser.parse(query)
        results = self.searcher.search(q, limit=10)
        return results
    def search_by_time(self, query):  # 按时间排序
        return sorted(self.search(query), key=lambda x: x['news_time'], reverse=True)
    def search_by_hot(self, query):  # 按热度排序
        return sorted(self.search(query), key=lambda x: x['news_total'], reverse=True)
    def search_by_revelance(self, query):  # 按相关度排序
        return sorted(self.search(query), key=lambda x: x.score, reverse=True)
    def complete_query(self, string): # 查询自动补齐
        return [item for item in self.wordlist if item.startswith(string)][:10]
    def recommend_news(self, query):  # 相关搜索推荐; 返回相关文档中的 tfidf/idf 最大的词项
        docs = list(sorted(self.search(query), key=lambda x: x.score))[:10]
        # docs = list(sorted(search('苹果'), key=lambda x: x.score))[:10]
        # print([list(sorted(tfidf_dic[item['news_id']], key=lambda x: tfidf_dic[item['news_id']][x]))[-1] for item in docs])
        # print([list(sorted(tfidf_dic[item['news_id']], key=lambda x: x]))[-1] for item in docs])
    def search_with_snippet(self, query):  # snippet 生成
        results = self.search(query)
        return [hit.highlights('news_body') for hit in results]
    def preview(self, news_id):  # 结果预览
        return ' '.join(self.items_dic[news_id]['news_body'])
    def similar_news(self, news_id):  # 相似新闻; 找同一篇新闻中 tfidf 最高的词再进行搜索
        items = sorted(self.tfidf_dic[news_id], key=lambda x: self.tfidf_dic[news_id][x])[-2:]
        return [item for item in self.search(''.join(items))]
    def hotest_news(self, num):  # 最热社会新闻
        return list(sorted(self.items, key=lambda x: x.get('news_total', 0)))[:num]
    def similar_word(self, query):  # 查找相关词语
        return [item[0] for item in self.word2vec_model.most_similar(query)]
    def comment_analyse(self, news_id):  # 一篇新闻中积极评论的数量
        return Counter([test.getscore(item['content']) for item in self.db_comments.find_one({"newsid": news_id})['comment_list']])
if __name__ == '__main__':
    se = Search_Engine()
    # test 通配符, 关键词
    for hit in se.search('苹果'): print(hit)
    for hit in se.search('香蕉'): print(hit)
    for hit in se.search('香*'): print(hit)
    # test search_by_time
    for hit in se.search('苹果'): print(hit['news_time'])
    for hit in se.search_by_time('苹果'): print(hit['news_time'])
    # test search_by_hot
    for hit in se.search('苹果'): print(hit['news_total'])
    for hit in se.search_by_hot('苹果'): print(hit['news_total'])
    # test search_by_revelance
    for hit in se.search('苹果'): print(hit.score)
    for hit in se.search_by_revelance('苹果'): print(hit.score)
    # test complete_query
    print(se.complete_query('苹'))  # ['苹果', '苹果公司', '苹果园', '苹果树', '苹果电脑', '苹果醋']
    # test search_with_snippet
    print(se.search_with_snippet('苹果'))
    print(se.search_with_snippet('香蕉'))
    print(se.search_with_snippet('香*'))
    # test preview
    print(se.preview('fymvuyt0333763'))
    # test similar_news
    print(len(se.similar_news('fymvuyt0333763')))
    print(se.similar_news('fymvuyt0333763')[2]['news_body'])
    # test hotest_news()
    for hit in se.hotest_news(10): print(hit['news_title'])
    for hit in se.hotest_news(10): print(hit['news_body'])
    for hit in se.hotest_news(10): print(hit['news_time'])
    # test similar_word()
    print(se.similar_word('苹果'))
    # test getscore() 评论情感分析
    print(test.getscore("人家是万恶的资本主义, 万恶的"))
    # test db_comments
    print(len(se.db_comments.find_one({"newsid": "fyfqvmh9184647"})['comment_list']))
    # test good_comments_num()
    print(se.comment_analyse("fyfqvmh9184647")['中性'])

    # test doc
    for hit in se.search('苹果'): print(hit['news_time'])
    print([item.fields() for item in se.search('苹果')])
