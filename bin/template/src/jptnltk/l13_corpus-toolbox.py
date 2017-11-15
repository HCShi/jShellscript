#!/usr/bin/python3
# coding: utf-8
from nltk.corpus import toolbox
##################################################################
## 简单测试
print(type(toolbox))  # <class 'nltk.corpus.reader.toolbox.ToolboxCorpusReader'>
print(toolbox.abspaths())  # []
print(toolbox.fileids())  # []; 两个居然都为空...
# ~/nltk_data/corpora/toolbox/ 在这个目录下, 手动找的
##################################################################
## words
rotokas_words = toolbox.words('rotokas.dic')
print(len(rotokas_words))  # 889
