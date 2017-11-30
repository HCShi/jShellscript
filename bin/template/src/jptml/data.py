#!/usr/bin/python3
# coding: utf-8
import random
import numpy as np
np.random.seed(100)
from sklearn.model_selection import train_test_split
from sklearn import datasets
import pandas as pd
from keras.utils import np_utils
from keras.datasets import mnist
# 专为一些模型做测试用的数据集
# X_train, y_train, X_test, y_test 使用这种命名风格
##################################################################
## 二分类问题
## iris 数据集很小, 适合一些基本机器学习算法
iris = datasets.load_iris()  # 加载数据集, 4 个 feather, 3 个 label
dataset = np.hstack((iris.data, iris.target.reshape(-1, 1))); print(dataset[0])  # [ 5.1  3.5  1.4  0.2  0. ]
df = pd.DataFrame(dataset, columns=['f1', 'f2', 'f3', 'f4', 'label'])
df = df.loc[df['label'] != 2]; print(df.shape, df.describe())  # (100, 5); 已经没有 2 的标签了, 去掉一个属性, 变成 2 分类
df = df.as_matrix()  # Keras 中可能会报错, 所以这里要设置为 matrix
X_train, X_test, y_train, y_test = train_test_split(df[:, :-1], df[:, -1], test_size=0.3)
y_train = np_utils.to_categorical(y_train); print(y_train[0])  # [ 0.  1.]; 上面白换成整形了
y_test = np_utils.to_categorical(y_test); print(y_test[0])  # [ 1.  0.]
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)  # (70, 4) (70, 2) (30, 4) (30, 2)
print(X_train[:10], y_train[:10])
##################################################################
## 二分类问题
## mnist 较大数据集, 适合深度学习算法
(X_train, y_train), (X_test, y_test) = mnist.load_data()  # 不用切分了
print(type(X_train))  # <class 'numpy.ndarray'>
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)  # (60000, 28, 28) (60000,) (10000, 28, 28) (10000,)
# 将其 3 维变 2 维 ((60000,28,28) 变 (60000, 784)), 并进行归一化
X_train = X_train.reshape(X_train.shape[0], -1) / 255
X_test = X_test.reshape(X_test.shape[0], -1) / 255
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)  # (60000, 784) (60000,) (10000, 784) (10000,)
print(set(y_train))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; 多分类的, 下面转化为 二分类
## 变为 二分类
dataset = np.hstack((X_train, y_train.reshape(-1, 1))); print(dataset.shape)  # (60000, 785)
df_train = pd.DataFrame(dataset, columns=[['l'+str(id) for id in range(784)] + ['label']]); print(df_train.shape)  # (60000, 785)
data_train = df_train.loc[df_train.label < 1.5].as_matrix(); print(data_train.shape)  # (12665, 785)
X_train, y_train = data_train[:, :-1], data_train[:, -1]; print(X_train.shape, y_train.shape)  # (12665, 784) (12665,)
print(set(y_train))  # {0.0, 1.0}
# 处理 test
dataset = np.hstack((X_test, y_test.reshape(-1, 1))); print(dataset.shape)  # (10000, 785)
df_test = pd.DataFrame(dataset, columns=[['l'+str(id) for id in range(784)] + ['label']]); print(df_test.shape)  # (10000, 785)
data_test = df_test.loc[df_test.label < 1.5].as_matrix(); print(data_test.shape)  # (2115, 785)
X_test, y_test = data_test[:, :-1], data_test[:, -1]; print(X_test.shape, y_test.shape)  # (2115, 784) (2115,)
print(set(y_test))  # {0.0, 1.0}
## y 变为 categorical
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
print(X_train[1].shape, y_train[0])  # (784,) [ 1.  0.]
##################################################################
## 多分类问题
