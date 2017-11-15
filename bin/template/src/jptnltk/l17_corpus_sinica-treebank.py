#!/usr/bin/python3
# coding: utf-8
from nltk.corpus import sinica_treebank
##################################################################
## 简单测试
print(type(sinica_treebank))  # <class 'nltk.corpus.reader.sinica_treebank.SinicaTreebankCorpusReader'>
print(len(sinica_treebank.words()))  # 91627
print(sinica_treebank.words())  # ['一', '友情', '嘉珍', '和', '我', '住在', '同一條', '巷子', '我們', ...]
# 去 ~/nltk_data/corpora/sinica_treebank/ 里面直接看会有好多的其他字符
##################################################################
## 生成 中文拼音的 38k-cn-words-pinyin-sorted-by-frequency.txt
import re
from nltk import FreqDist
from pypinyin import pinyin, lazy_pinyin, Style
fd = FreqDist(sinica_treebank.words())
print(len(list(fd.keys())))  # 17273; 去重以后的结果
print(len(fd.most_common()))  # 17273
str = ''.join([x[0] for x in fd.most_common()]); print(len(str))  # 38844
str = re.sub('[^\u4e00-\u9fa5]', '', str); print(len(str))  # 38225; 去掉标点符号
with open('38k-cn-words-pinyin-sorted-by-frequency.txt', 'w') as f:
    f.write('\n'.join(lazy_pinyin(str)))
