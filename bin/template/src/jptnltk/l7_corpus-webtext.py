#!/usr/bin/python3
# coding: utf-8
from nltk.corpus import webtext
##################################################################
## fileids(), raw()
print(type(webtext))  # <class 'nltk.corpus.reader.plaintext.PlaintextCorpusReader'>
print(webtext.fileids())  # ['firefox.txt', 'grail.txt', 'overheard.txt', 'pirates.txt', 'singles.txt', 'wine.txt']
for fileid in webtext.fileids(): print(fileid, webtext.raw(fileid)[:65], '...')  # 输出每篇文章的前 65 个字符
# firefox.txt Cookie Manager: "Don't allow sites that set removed cookies to se...
