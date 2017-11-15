#!/usr/bin/python3
# coding: utf-8
from nltk.corpus import inaugural
##################################################################
## 简单了解
print(type(inaugural))  # <class 'nltk.corpus.reader.plaintext.PlaintextCorpusReader'>
print(len(inaugural.fileids()))  # 56; 到 奥巴马 为止一共 56 个总统
print(inaugural.fileids()[:3])  # ['1789-Washington.txt', '1793-Washington.txt', '1797-Adams.txt']
##################################################################
## 输出美国总统的就职年份
print([fileid[:4] for fileid in inaugural.fileids()])  # ['1789', '1793', '1797', '1801', '1805', '1809', '1813', '1817', '1821', ...]
