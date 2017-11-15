#!/usr/bin/python3
# coding: utf-8
import numpy as np
from keras.datasets import imdb
import matplotlib.pyplot as plt
# 数据介绍
# The dataset is "the Large Movie Review Dataset" often referred to as the IMDB dataset.
# The data was also used as the basis for a Kaggle competition titled “Bag of Words Meets Bags of Popcorn” in late 2014 to early 2015.
# 做 Kaggle 题目 Bag of Words Meets Bags of Popcorn 时, 发现和 Keras 用的是同一套数据...; 具体的题目代码见 jptml
# Keras provides access to the IMDB dataset built-in.
# The keras.datasets.imdb.load_data() allows you to load the dataset in a format that is ready for use in neural network and deep learning models.
# The words have been replaced by integers that indicate the absolute popularity of the word in the dataset.
#     The sentences in each review are therefore comprised of a sequence of integers.
# 所有的词已经替换成它出现的次数
# Calling imdb.load_data() the first time will download the IMDB dataset to your computer and store it in your home directory
#     under ~/.keras/datasets/imdb.npz als a 11 megabyte file.
# Usefully, the imdb.load_data() provides additional arguments including the number of top words to load (where words with a lower integer
#     are marked as zero in the returned data), the number of top words to skip (to avoid the “the”‘s) and the maximum length of reviews to support.
##################################################################
## load the dataset
(X_train, y_train), (X_test, y_test) = imdb.load_data()
X = np.concatenate((X_train, X_test), axis=0)  # hstack
y = np.concatenate((y_train, y_test), axis=0)
##################################################################
## summarize size, class, num_words
print(X_train.shape, X_test.shape)  # (25000,) (25000,); 各占一半
print(len(X_train[0]), len(X_train[1]))  # 218 189; 和下面的相同
print(type(X), type(X[0]))  # <class 'numpy.ndarray'> <class 'list'>
print(len(X[0]), len(X[1]))  # 218 189; 每行长度不同, 所有才会有下面的 (50000,)
print(X.shape)  # (50000,)
print(y.shape)  # (50000,)
print(np.hstack(X).shape)  # (11737946,); 总共有这么多的单词
print(np.unique(y, return_counts=True))  # (array([0, 1]), array([25000, 25000])); 可以发现, 各占一半
print(len(np.unique(np.hstack(X))))  # 88585 个 唯一单词, 还不到 100, 000 个单词
print(len(np.unique(X)))  # 49580; 为什么不一样, 不知道...
# Summarize average review length
result = [len(x) for x in X]
print("Mean %.2f words (%f)" % (np.mean(result), np.std(result)))  # Mean 234.76 words (172.911495)
plt.boxplot(result)
plt.show()
# Looking a box and whisker plot for the review lengths in words,
# we can probably see an exponential distribution that we can probably cover
#     the mass of the distribution with a clipped length of 400 to 500 words.
