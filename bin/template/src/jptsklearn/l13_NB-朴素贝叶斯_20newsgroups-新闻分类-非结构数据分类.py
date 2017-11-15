#!/usr/bin/python3
# coding: utf-8
from sklearn.datasets import fetch_20newsgroups  # 这里的新闻需要下载
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
##################################################################
## 数据准备
categories = ["alt.atheism", "soc.religion.christian", "comp.graphics", "sci.med"]  # 选取需要下载的新闻分类
news = fetch_20newsgroups(subset='all', categories=categories)
print(len(news.data))  # 3759
X_train, X_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25, random_state=33)  # 75% training set, 25% testing set
##################################################################
## 将 train 和 test 同时数值化
vec = CountVectorizer()  # transfer data to vector
X_train = vec.fit_transform(X_train)
vec_test = CountVectorizer(vocabulary=vec.vocabulary_)  # 和 stopwords 作用刚好相反; 因为 test 中可能有 train 没有的词
X_test = vec_test.transform(X_test)
##################################################################
## training
mnb = MultinomialNB()  # initialize NB model with default config
mnb.fit(X_train, y_train)  # training model
y_predict = mnb.predict(X_test)  # run on test data
##################################################################
## performance
# ./l17_20newsgroups-Pipeline-将前面的分类器整合_SVM-NB-对比_结果评估_网格调参.py 中有更多的测试方法
print('The Accuracy is', mnb.score(X_test, y_test))  # The Accuracy is 0.964893617021
print(classification_report(y_test, y_predict, target_names=news.target_names))
