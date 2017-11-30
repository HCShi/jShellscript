#!/usr/bin/python3
# coding: utf-8
import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
import matplotlib.pyplot as plt
# 手写数据集, 每张照片是 28x28, 多分类
##################################################################
## load datasets
(X_train, y_train), (X_test, y_test) = mnist.load_data()
##################################################################
## 数据预览
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)  # (60000, 28, 28) (60000,) (10000, 28, 28) (10000,); 这里 X 对自己认识比 imdb 清楚
print(X_train[0][0])  # [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
print(set(y_train))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
##################################################################
## 画出来
plt.imshow(X_train[0])
plt.show()
##################################################################
## 数据预处理
## 将其 3 维变 2 维 ((60000,28,28) 变 (60000, 784)), 并进行归一化
X_train = X_train.reshape(X_train.shape[0], -1) / 255.
X_test = X_test.reshape(X_test.shape[0], -1) / 255.
## 将多分类变为 one-hot, 一般在深度学习中会用 one-hot 这种类型的分类, svm 中直接用 0, 1, 2, 3
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)
print(X_train[1].shape, y_train[0])  # (784,) [ 0.  0.  0.  0.  0.  1.  0.  0.  0.  0.]
