#!/usr/bin/python3
# coding: utf-8
# 参考: [[Scikit-learn 教程] 03.01 文本处理：分类与优化](https://jizhi.im/blog/post/sklearntutorial0302), 已存盘
## 获取数据
from sklearn.datasets import fetch_20newsgroups  # 20newsgroups 简介见 ./l14_数据获取-urllib-tarfile-loadfile_20newsgroups.py
categories = ["alt.atheism", "soc.religion.christian", "comp.graphics", "sci.med"]  # 选取需要下载的新闻分类
twenty_train = fetch_20newsgroups(subset="train", categories=categories, shuffle=True, random_state=42)  # 下载并获取训练数据, 也是先全部下载, 再提取部分
print(twenty_train.target_names)  # ['alt.atheism', 'comp.graphics', 'sci.med', 'soc.religion.christian']
## 一. 统计词语出现次数
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print(len(twenty_train.data))  # 2257; 篇文档
print(X_train_counts.shape)  # (2257, 35788); 35788 个单词
print(count_vect.vocabulary_.get(u'algorithm'))  # 4690; algorithm id
print(X_train_counts.toarray().sum(axis=0)[count_vect.vocabulary_.get('algorithm')])  # 90; algorithm 出现次数
## 二. 使用 tf-idf 方法提取文本特征
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf.shape)  # (2257, 35788)
##################################################################
## 以上是 ./l15_20newsgroups-文本特征提取.py 中的代码, 有详细解释
##################################################################
## 训练分类器
# 可以用于文本分类的机器学习算法有很多, 朴素贝叶斯算法 (Naïve Bayes) 就是其中一个优秀代表
# Scikit-learn 包含了朴素贝叶斯算法的多种改进模型, 最适于文本词数统计方面的模型叫做多项式朴素贝叶斯 (Multinomial Naïve Bayes)
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)  # target 已经在加载的时候自动数值化, target_names 中存放原始字符串
##################################################################
## 朴素贝叶斯预测结果
docs_new = ['Nvidia is awesome!']  # 预测用的新字符串, 你可以将其替换为任意英文句子

# 字符串处理, 提取特征值后才能进行预测
# 无论是什么机器学习方法, 都只能针对向量特征 (也就是一系列的数字组合) 进行分析, 因此在读取文本之后, 我们要将文本转化为数字化的特征向量.
X_new_counts = count_vect.transform(docs_new)  # 生成 [文档, 词汇] 矩阵
X_new_tfidf = tfidf_transformer.transform(X_new_counts)
print(X_new_counts.shape)  # (1, 35788)
print(X_new_counts, X_new_tfidf) # (0, 5953)	1 (0, 18474)	1; (0, 18474)	0.176124939041 (0, 5953)	0.984367820404
print(X_new_tfidf.max())
# 这里生成的 X_new_tfidf 就相当于 iris.data, 只是 iris.data 是整数矩阵, 这里好像都是小数, 但两者代表的都是特征属性 的值

# 进行预测
predicted = clf.predict(X_new_tfidf)
# 打印预测结果
for doc, category in zip(docs_new, predicted): print('%r => %s' % (doc, twenty_train.target_names[category]))
# 'Nvidia is awesome!' => comp.graphics
