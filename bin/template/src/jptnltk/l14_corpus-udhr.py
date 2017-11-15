#!/usr/bin/python3
# coding: utf-8
from nltk.corpus import udhr  # contains the Universal Declaration of Human Rights in over 300 languages
##################################################################
## 简单测试
print(type(udhr))  # <class 'nltk.corpus.reader.udhr.UdhrCorpusReader'>
print(len(udhr.fileids()))  # 310
print(udhr.fileids()[:2])  # ['Abkhaz-Cyrillic+Abkh', 'Abkhaz-UTF8']
print([lang for lang in udhr.fileids() if lang.startswith('English')])  # ['English-Latin1']
print(len(udhr.words('English-Latin1')))  # 1781
print(udhr.words('English-Latin1')[:5])  # ['Universal', 'Declaration', 'of', 'Human', 'Rights']
languages = ['Chickasaw', 'English', 'German_Deutsch', 'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']  # 这些是常用语言
