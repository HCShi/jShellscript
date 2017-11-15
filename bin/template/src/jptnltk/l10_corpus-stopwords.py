#!/usr/bin/python3
# coding: utf-8
from nltk.corpus import stopwords
##################################################################
## 简单测试
print(type(stopwords))  # <class 'nltk.corpus.reader.wordlist.WordListCorpusReader'>
print(len(stopwords.fileids()))  # 16; 支持 16 种语言
print(stopwords.fileids()[:5])  # ['danish', 'dutch', 'english', 'finnish', 'french']
print(len(stopwords.words('english')))  # 153 个停用词
print(stopwords.words('english')[:5])  # ['i', 'me', 'my', 'myself', 'we']
