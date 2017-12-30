#!/usr/bin/python3
# coding: utf-8
## 读数据库
import bson
import sys
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
# items = list(bson.decode_file_iter(open('./tmp.bson', 'rb'))); print(len(items))  # 14128; 读取 BSON 文件
items = list(bson.decode_file_iter(open('./tmp_news/sina.bson', 'rb'))); print(len(items))  # 140639; 读取 BSON 文件
print(items[0].keys())  # dict_keys(['_id', 'news_id', 'news_url', 'news_from', 'news_time2', 'news_channel', 'news_title', 'news_source', 'news_time', 'news_body', 'news_keywords', 'news_show', 'news_total'])
print(items[0]['news_id'])  # fxzczfc6652525
print(items[0]['news_keywords'])  # ['陕西', '公厕爆炸']
print(items[0]['news_show'])  # 0
print(items[0]['news_time'])  # 2017年05月17日23:48
print(items[0]['news_time2'])  # 1495036111; 时间戳
print(set([len(item['news_title']) for item in items if item.get('news_title', 0) != 0]))
# {6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37}; 这些都是 str 长度
print(set([len(item['news_body']) for item in items])) # {0, 1, 2, 14, 15, 16, ..., 353, 982, 478, 1004}; 居然还能分成 1004 段...
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
print([item['_id'] for item in items[:5]])  # [ObjectId('5a3663a1a59616fda3af13cc'), ObjectId('5a3663a1a59616fda3af13ce'), ObjectId('5a3663a1a59616fda3af13d0'), ObjectId('5a3663a1a59616fda3af13d2'), ObjectId('5a3663a1a59616fda3af13d4')]
print([item['news_id'] for item in items[:5]])  # ['fyfkqks4242207', 'fyfkqks4232805', 'fyfkqks4232961', 'fyfkqks4232721', 'fyfekhi8022264']
# 两个 id 都不是整数的
items_dic = dict((item['news_id'], item) for item in items)
print(len(items_dic.keys()))  # 140639
print(items_dic['fyfkqks4242207'])  # {'_id': ObjectId('5a3663a1a59616fda3af13cc'), 'news_id': 'fyfkqks4242207', 'news_url': 'http://news.sina.com.cn/c/nd/2017-05-17/doc-ifyfkqks4242207.shtml', 'news_from': 'sina', 'news_time2': 1495036111, 'news_channel': 'gn', 'news_title': '中国阿根廷将互发10年有效签证 阿申请入亚投行', 'news_source': '新浪体育', 'news_time': '2017年05月17日23:48\t\t', 'news_body': ['原标题：中国、阿根廷就互发10年有效签证达成一致', '央视网消息：今天，陪同总统参加完“一带一路”国际合作高峰论坛的阿根廷外交部长马尔科拉和中方外长王毅，在北京共同主持召开了中阿政府间常设委员会第二次会议，这是中国和阿根廷两国政府间规格最高、涵盖面最广的双边合作机制。', '会议听取了两国委员会政治、农业、防务、林业及森林资源与生态保护、科技、卫生与医学科学、文化、核能、航天9个分委会的工作汇报，并决定在两国委员会框架内增设教育、体育、旅游分委会。', '中阿双方就互发10年多次有效旅游、商务签证达成一致。王毅指出，双方应以共建“一带一路”为契机，对接发展战略，深化经贸、人文各领域交流。马尔科拉表示，阿根廷申请加入亚洲基础设施投资银行，愿积极参与“一带一路”建设，有效落实两国政府间共同行动计划，造福两国人民。', '中阿政府间常设委员会第一次会议2015年在北京召开。双方商定，第三次会议将于2019年在阿根廷布宜诺斯艾利斯举行。', '责任编辑：李鹏 '], 'news_keywords': ['阿根廷', '签证', '亚投行'], 'news_show': 0, 'news_total': 0}
##################################################################
## 在每篇文档中构建每个词 tf-idf 权重词典
documents_dic = dict((item['news_id'], ' '.join(jieba.lcut(''.join(item['news_body'])))) for item in items)  # 运行半个小时...
print(list(documents_dic.values())[0])  # 原 标题 ： 中国 、 阿根廷 就 互发...; 用空格分开的 str, 因为 CountVectorizer 是接受这种的数据
with open('tmp_document-dict.pkl', 'wb') as f: pickle.dump(documents_dic, f)
with open('tmp_document-dict.pkl', 'rb') as f: documents_dic = pickle.load(f)  # 进行了一下保存, 其实并不需要保存, 因为要用的是下面的 tfidf_dic
print(list(documents_dic.values())[0])  # 原 标题 ： 中国 、 阿根廷 就 互发...
## 建立词袋
count_vec = CountVectorizer()
X = count_vec.fit_transform(documents_dic.values()); print(X)  # toarray() 会爆内存...
print(type(X))  # <class 'scipy.sparse.csr.csr_matrix'>
print(X[0].nonzero()[1])  # 不是 0 的项
print(X.shape[0])  # 140639
wordlist = count_vec.get_feature_names(); print(len(wordlist), wordlist[:5])  # 558373 ['00', '000', '0000', '000000', '0000000']
with open('tmp_wordlist.pkl', 'wb') as f: pickle.dump(wordlist, f)
with open('tmp_wordlist.pkl', 'rb') as f: wordlist = pickle.load(f)
print(list(count_vec.vocabulary_)[:5])  # ['标题', '中国', '阿根廷', '互发', '10']
## tfidf
tfidf_tra = TfidfTransformer()
tfidf = tfidf_tra.fit_transform(X)  # toarray 也会爆内存
print(type(tfidf[0]))  # <class 'scipy.sparse.csr.csr_matrix'>
print(tfidf[0])
print(tfidf.shape[0])  # 140639
print(tfidf[0, 77671])  # 0.0; 毕竟是稀疏矩阵...
print(tfidf[0].nonzero()[1])
print(tfidf[0, 76093])  # 0.0854599863109
idflist = tfidf_tra.idf_; print(len(idflist), idflist[:5])  # 558373 [  4.96750144   7.28943831   9.80943628  11.75534642  12.16081153]
with open('tmp_idflist.pkl', 'wb') as f: pickle.dump(idflist, f)
with open('tmp_idflist.pkl', 'rb') as f: idflist = pickle.load(f)
print(idflist[count_vec.vocabulary_['标题']])  # 2.02992947662
print(list(wordlist[idx] for idx in tfidf[0].nonzero()[1]))  # ['标题', '中国', '阿根廷', '互发', '1', ...]
## 根据文档来统计每个词的 tfidf
tfidf_array = [[tfidf[i, idx] for idx in tfidf[i].nonzero()[1]] for i in range(tfidf.shape[0])]  # 半个多小时
with open('tmp_tfidf-array.pkl', 'wb') as f: pickle.dump(tfidf_array, f)
with open('tmp_tfidf-array.pkl', 'rb') as f: tfidf_array = pickle.load(f)
print(len(tfidf_array), tfidf_array[0])  # 140639
## 将 tfidf 写回字典, 这里只统计 tfidf 排名靠前的 10 个, 后面的不关心...
tfidf_values = [dict(list(sorted(zip(list(wordlist[idx] for idx in tfidf[i].nonzero()[1]), tfidf_array[i]), key=lambda x: -x[1]))[:10]) for i in range(tfidf.shape[0])]  # 挺快的
tfidf_dic = dict(zip(documents_dic.keys(), tfidf_values))
print(list(tfidf_dic.values())[0])
with open('tmp_tfidf_dic.pkl', 'wb') as f: pickle.dump(tfidf_dic, f)
with open('tmp_tfidf_dic.pkl', 'rb') as f: tfidf_dic = pickle.load(f)  # 进行了一下保存
# 上面建的这些 dict, 都是进行相似查询时用到的, 所以更新新闻的时候只对齐进行下面的索引即可...;
# 意思是上面的代码只执行一遍就行了, 以后的每日更新只单纯建立索引就行了
##################################################################
## 建索引
schema = Schema(news_id=STORED, news_url=STORED, news_from=STORED, news_channel=STORED, news_title=TEXT(stored=True, analyzer=analyzer),
                news_source=STORED, news_time=STORED, news_time2=STORED, news_body=TEXT(stored=True, analyzer=analyzer),
                news_keywords=STORED, flag=STORED, news_show=STORED, news_total=STORED)
ix = create_in("./tmp-homework", schema)
writer = ix.writer()
for item in items[::5]:  # 14w 条记录, 建了两个小时的索引, 占了 6G 硬盘(总共 120G 的 SSD, 剩的空间不多了), 还没建完索引...; 后来迫不得已, 进行了缩减...
    writer.add_document(news_id=item.get('news_id', 'null'), news_url=item.get('news_url', 'null'), news_from=item.get('news_from', 'null'),
                        news_channel=item.get('news_channel', 'null'), news_title=item.get('news_title', 'null'), news_source=item.get('news_source', 'null'),
                        news_time=item.get('news_time', 'null'), news_body=''.join(item.get('news_body', 'null')), news_keywords=item.get('news_keywords', ['null']),
                        flag=item.get('flag', 'null'), news_show=item.get('news_show', '0'), news_total=item.get('news_total', '0'),
                        news_time2=item.get('news_time2', 'null'))
writer.commit()  # 单独这条命令还是比较慢的...
ix = open_dir('./tmp-homework')  # 在 ./tmp-homework-back 中进行备份
##################################################################
## 进行查询
searcher = ix.searcher()
parser = QueryParser("news_body", schema=ix.schema)
q = parser.parse('公厕')
results = searcher.search(q); print(results)
for hit in results: print(hit.highlights("news_body"))
