#!/usr/bin/python3
# coding: utf-8
from nltk.corpus import cmudict  # 存放着英语发音规则
##################################################################
## 简单查看
print(cmudict.fileids())  # ['cmudict']
print(type(cmudict))  # <class 'nltk.corpus.reader.cmudict.CMUDictCorpusReader'>
print(len(cmudict.words()))  # 133737; 个英语单词
print(cmudict.words()[:5])  # ['a', 'a.', 'a', 'a42128', 'aaa']
##################################################################
## entries()
entries = nltk.corpus.cmudict.entries()
print(len(entries))  # 133737
print(entries[:5])  # [('a', ['AH0']), ('a.', ['EY1']), ('a', ['EY1']), ('a42128', ['EY1', 'F', 'AO1', 'R', 'T', 'UW1', 'W', 'AH1', 'N', 'T', 'UW1', 'EY1', 'T']), ('aaa', ['T', 'R', 'IH2', 'P', 'AH0', 'L', 'EY1'])]
for entry in entries[42371:42374]: print(entry)
# ('fir', ['F', 'ER1'])
# ('fire', ['F', 'AY1', 'ER0'])
# ('fire', ['F', 'AY1', 'R'])
##################################################################
## dict()
prondict = nltk.corpus.cmudict.dict()
print(prondict['fire'])  # [['F', 'AY1', 'ER0'], ['F', 'AY1', 'R']]
print(prondict['blog'])  # 没有 blog, 会报错
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'blog'
prondict['blog'] = [['B', 'L', 'AA1', 'G']]  # 自己添加
print(prondict['blog'])  # [['B', 'L', 'AA1', 'G']]
