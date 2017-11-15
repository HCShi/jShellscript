#!/usr/bin/python3
# coding: utf-8
# The Reuters Corpus contains 10,788 news documents totaling 1.3 million words. The documents have been classified into 90 topics,
# and grouped into two sets, called "training" and "test"; thus, the text with fileid 'test/14826' is a document drawn from the test set.
# This split is for training and testing algorithms that automatically detect the topic of a document,
from nltk.corpus import reuters
##################################################################
## 简单查看
print(type(reuters))  # <class 'nltk.corpus.reader.plaintext.CategorizedPlaintextCorpusReader'>
print(len(reuters.fileids()))  # 10788
print(reuters.fileids()[:5])  # ['test/14826', 'test/14828', 'test/14829', 'test/14832', 'test/14833']
print(len(reuters.categories()))  # 90
print(reuters.categories()[:5])  # ['acq', 'alum', 'barley', 'bop', 'carcass']
print(reuters.categories('training/9865'))  # ['barley', 'corn', 'grain', 'wheat']; 都很短
print(reuters.categories(['training/9865', 'training/9880']))  # ['barley', 'corn', 'grain', 'money-fx', 'wheat']
print(len(reuters.fileids('barley')))  # 51
print(len(reuters.fileids(['barley', 'corn'])))  # 264
