#!/usr/bin/python3
# coding: utf-8
# Brown Corpus (布朗语料库): Brown Corpus of Standard American English 被认为是第一个可以在计算语言学处理中使用的通用英语语料库
#     它包含了一百万字 1961 年出版的美语文本; 它代表了通用英语的样本, 采样自小说, 新闻和宗教文本; 随后, 在大量的人工标注后, 诞生了词性标注过的版本
from nltk.corpus import brown
print(len(brown.fileids()))  # 500; 个 文档
print(brown.fileids()[:5])  # ['ca01', 'ca02', 'ca03', 'ca04', 'ca05']
print(len(brown.words()))  # 1161192; 总共 1161192 个单词
print(brown.words()[:5])  # ['The', 'Fulton', 'County', 'Grand', 'Jury']; 打印前 5 个单词
print(len(brown.words('ca01')))  # 2242; 一片文档还是比较少的
##################################################################
## 标记数据
print(brown.tagged_words()[:3])  # [('The', 'AT'), ('Fulton', 'NP-TL'), ('County', 'NN-TL')]; 打印前 3 个单词的标注
##################################################################
## categories
print(len(brown.categories()))  # 15; 个分类
print(brown.categories())  # ['adventure', 'belles_lettres', 'editorial', 'fiction', 'government', 'hobbies', 'humor', 'learned', 'lore', 'mystery', 'news', 'religion', 'reviews', 'romance', 'science_fiction']
print(len(brown.words(categories='news')))  # 100554; 统一类数据的单词
print(len(brown.sents(categories=['news', 'editorial', 'reviews'])))  # 9371
# brown 包括标记数据 和 非标记数据
print(len(brown.words()))  # 1161192
print(len(brown.words(categories=brown.categories())))  # 1161192; 所有数据都在 categories 里面
##################################################################
## 路径
print(brown.abspath('ca01'))  # /home/coder352/nltk_data/corpora/brown/ca01
print(brown.abspaths())  # 所有文档路径
##################################################################
## 类型
print(type(brown))  # <class 'nltk.corpus.reader.tagged.CategorizedTaggedCorpusReader'>
print(type(brown.words()))  # <class 'nltk.corpus.reader.util.ConcatenatedCorpusView'>
print(type(brown.words('ca01')))  # <class 'nltk.corpus.reader.tagged.TaggedCorpusView'>
