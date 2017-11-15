#!/usr/bin/python3
# coding: utf-8
# https://github.com/EliasCai/sentiment/blob/master/sentiment_words.py#L78
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.text import text_to_word_sequence
from keras.preprocessing.text import one_hot
from keras.preprocessing.text import hashing_trick
##################################################################
## 1. text_to_word_sequence, one_hot, hashing_trick
texts = ['some thing to eat', 'some thing to drink']
print(text_to_word_sequence(texts[0]))  # ['some', 'thing', 'to', 'eat']; 简单的空格分开
print(one_hot(texts[0], 10))  # [5, 7, 5, 7]; (10 表示数字化向量为 10 以内的数字)
print(one_hot(texts[1], 10))  # [5, 7, 5, 5]; 因为内部调用了 hash, 所以能够在定了 (text, n) 之后对每个 str 赋值相同
# This is a wrapper to the `hashing_trick` function using `hash` as the hashing function, unicity of word to index mapping non-guaranteed.
##################################################################
## 2. Tokenizer: 索引就是出现的先后位置
# keras.preprocessing.text.Tokenizer(num_words=None, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\t\n', lower=True, split=" ", char_level=False)
# Tokenizer 是一个用于向量化文本, 或将文本转换为序列(即单词在字典中的下标构成的列表, 从 1 算起)的类.
# num_words: None 或整数, 处理的最大单词数量. 若被设置为整数, 则分词器将被限制为待处理数据集中最常见的 num_words 个单词
# char_level: 如果为 True, 每个字符将被视为一个标记
texts = ['some thing to eat', 'some thing to drink']
tmp_tokenizer = Tokenizer(num_words=None)  # num_words:None 或整数, 处理的最大单词数量; 少于此数的单词丢掉
tmp_tokenizer.fit_on_texts(texts)
# tmp_tokenizer.fit_on_texts(texts[0]); tmp_tokenizer.fit_on_texts(texts[1])  # 不能这样, 会按单个字母来统计
# 属性
print(tmp_tokenizer.word_counts)  # OrderedDict([('some', 2), ('thing', 2), ('to', 2), ('eat', 1), ('drink', 1)]); 在训练期间出现的次数
print(tmp_tokenizer.word_docs)  # {'thing': 2, 'eat': 1, 'to': 2, 'some': 2, 'drink': 1}; 在训练期间所出现的文档或文本的数量
print(tmp_tokenizer.word_index)  # {'some': 1, 'thing': 2, 'to': 3, 'eat': 4, 'drink': 5}; 排名或者索引
print(len(tmp_tokenizer.word_index))  # 5; 词典长度
print(tmp_tokenizer.index_docs)  # {2: 2, 4: 1, 3: 2, 1: 2, 5: 1}; 将 word_index 和 word_docs 合并
print(tmp_tokenizer.document_count)  # 2; 训练文档数
# 类方法
print(tmp_tokenizer.texts_to_sequences(texts))  # [[1, 2, 3, 4], [1, 2, 3, 5]]; 得到词索引
print(tmp_tokenizer.texts_to_matrix(texts))  # 矩阵化 = one_hot; one-hot 形式的码, 即仅记录词在词典中的下标
# [[ 0.  1.  1.  1.  1.  0.]
#  [ 0.  1.  1.  1.  0.  1.]]
