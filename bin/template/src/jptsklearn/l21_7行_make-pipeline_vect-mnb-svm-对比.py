#!/usr/bin/python3
# coding: utf-8
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
##################################################################
## 7 行, 前面几篇写的太啰嗦了, 这里才符合 Python ~, 介绍看前面的
vect = TfidfVectorizer(stop_words='english', token_pattern=r'\b\w{2,}\b', min_df=1, max_df=0.1, ngram_range=(1,2))
mnb = MultinomialNB(alpha=2)
svm = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, max_iter=5, random_state=42)
mnb_pipeline = make_pipeline(vect, mnb)
svm_pipeline = make_pipeline(vect, svm)
mnb_cv = cross_val_score(mnb_pipeline, X, y, scoring='accuracy', cv=5)
svm_cv = cross_val_score(svm_pipeline, X, y, scoring='accuracy', cv=5)
##################################################################
## 检测结果
print('\nMultinomialNB Classifier\'s Accuracy: %0.5f\n' % mnb_cv.mean())
print('\nSVM Classifier\'s Accuracy: %0.5f\n' % svm_cv.mean())
##################################################################
## 总结:
# 1. 这里的数据没有, 所以不能运行; 尝试了 iris, digits, 返现要用文本数据, 以后再试吧
