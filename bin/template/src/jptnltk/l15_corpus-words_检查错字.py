#!/usr/bin/python3
# coding: utf-8
from nltk.corpus import words
##################################################################
## 简单查看
print(type(words))  # <class 'nltk.corpus.reader.wordlist.WordListCorpusReader'>
print(words.fileids())  # ['en', 'en-basic'], 就两个
print(words.abspath('en'))  # /home/coder352/nltk_data/corpora/words/en
print(len(words.words('en')))  # 235886; 个英语单词
print(type(words.words('en')))  # <class 'list'>
print([word for word in words.words('en') if len(word) == 1])  # 26 个英文字母, 大小写
print(len(words.words('en-basic')))  # 2850; 个英语基础词汇
##################################################################
## 查看 gutenberg 中的错别字
def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)
print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt')))
# ['abbeyland', 'abhorred', 'abilities', 'abounded', 'abridgement', 'abused', 'abuses',
# 'accents', 'accepting', 'accommodations', 'accompanied', 'accounted', 'accounts',
# 'accustomary', 'aches', 'acknowledging', 'acknowledgment', 'acknowledgments', ...]
