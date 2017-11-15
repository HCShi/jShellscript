#!/usr/bin/python3
# coding: utf-8
from sklearn.datasets import fetch_20newsgroups
from sklearn.datasets.base import Bunch  # 引入 Bunch 类
import pickle  # 引入持久化类
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
##################################################################
## 导入数据
categories = ["alt.atheism", "soc.religion.christian", "comp.graphics", "sci.med"]  # 选取需要下载的新闻分类
data_set = fetch_20newsgroups(subset="train", categories=categories, shuffle=True, random_state=42)  # 下载并获取训练数据, 也是先全部下载, 再提取部分
print(data_set.target_names)  # ['alt.atheism', 'comp.graphics', 'sci.med', 'soc.religion.christian']
##################################################################
## 定义词袋数据结构
# tdm:tf-idf 计算后词袋
stpwrdlst = []  # 停用词表为 空
wordbag = Bunch(target_name=[], label=[], filenames=[], tdm=[], vocabulary={}, stpwrdlst=[])
wordbag.target_name = data_set.target_names
wordbag.label = data_set.target
wordbag.filenames = data_set.filenames
wordbag.stpwrdlst = stpwrdlst

vectorizer = CountVectorizer(stop_words=stpwrdlst)  # 使用 TfidfVectorizer 初始化向量空间模型--创建词袋
transformer = TfidfTransformer()  # 该类会统计每个词语的 tf-idf 权值
fea_train = vectorizer.fit_transform(data_set.data)  # 文本转为词频矩阵
print(fea_train.shape)  # (2257, 35788); 2257 篇文档, 35788 个单词

wordbag.tdm = fea_train  # 为 tdm 赋值
wordbag.vocabulary = vectorizer.vocabulary_
##################################################################
## 创建词袋的持久化
file_obj = open("tmp.data", "wb")
pickle.dump(wordbag, file_obj)
file_obj.close()
##################################################################
## 读取
with open('tmp.data', 'rb') as f: clf2 = pickle.load(f)
print(clf2.tdm.shape)  # (2257, 35788)
