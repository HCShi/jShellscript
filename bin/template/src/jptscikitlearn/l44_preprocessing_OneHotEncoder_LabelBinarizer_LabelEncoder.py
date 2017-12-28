#!/usr/bin/python3
# coding: utf-8
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import LabelEncoder
##################################################################
## 1. OneHotEncoder() 将变量的特征值转换为稀疏矩阵
## OneHotEncoder().fit_transform(X, y=None)
## X : array-like, shape [n_samples, n_feature]: Input array of type int.
x = np.array([[1, 2, 3], [2, 5, 6]]); print(x)
one_hot_encoder = OneHotEncoder()
print(one_hot_encoder.fit_transform(x))  # 稀疏表示形式
print(one_hot_encoder.fit_transform(x).toarray())
# [[ 1.  0.  1.  0.  1.  0.]   # 代表 1(1, 0), 2(1, 0), 3(1, 0)
#  [ 0.  1.  0.  1.  0.  1.]]  # 代表 2, 5, 6
print(one_hot_encoder.fit_transform(x).todense())  # 密集表示形式, 同 .toarray()
# x 有三个特征: 第一个特征的取值为 1 、 2, 第二特征的取值为 2 、 5, 第三个特征的取值为 3 、 6;
# 可知三个特征的最大特征值分别为 2 、 5 、 6, 每个特征的取值都必须在 range(n_values[i]) 范围内, 因此 n_values=[3, 6, 7]
print(one_hot_encoder.n_values_)  # [3, 6, 7]; n_values_ 属性: 取每个特征的最大特征值 +1
print(one_hot_encoder.feature_indices_)  # [0,  3,  9, 16]; feature_indices_ 属性: n_values_ 的累计
print(one_hot_encoder.active_features_)  # [ 1,  2,  5,  8, 12, 15]; active_features_ 属性

# 更直观的例子
one_hot_encoder = OneHotEncoder()
one_hot_encoder.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
print(one_hot_encoder.transform([[0, 1, 3]]).toarray())
# [[ 1.  0.  0.  1.  0.  0.  0.  0.  1.]]
# fit 了 4 个数据 3 个特征, 而 transform 了 1 个数据 3 个特征. 第一个特征两种值(0: 10, 1: 01), 第二个特征三种值(0: 100, 1: 010, 2: 001),
#     第三个特征四种值(0: 1000, 1: 0100, 2: 0010, 3: 0001). 所以转换[0, 1, 3]为[ 1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.,  1.].
print(one_hot_encoder.n_values_)  # [2 3 4]; 第一个特征占两位, 第二个特征占三位, 第三个特征占四位
print(one_hot_encoder.feature_indices_)  # [0 2 5 9]; 第一个特征从 0 到 1, 第二个特征从 2 到 4, 第三个特征从 5 到 8
print(one_hot_encoder.active_features_)  # [0 1 2 3 4 5 6 7 8]


# keras.utils.np_utils.to_categorical(x) 只接受 vec, 感觉更像 one_hot, 区别见 jptkeras
print(one_hot_encoder.fit_transform(np.array([1, 2, 1]).reshape(-1, 1)).toarray())  # 行代表 samples, 列代表 features 个数
# [[ 1.  0.]
#  [ 0.  1.]
#  [ 1.  0.]]
##################################################################
## 2. LabelBinarizer()
x = ['jrp', 'sky', 'jrp', 'flower']
label_encoder = LabelBinarizer()
print(label_encoder.fit_transform(x))
# [[0 1 0]
#  [0 0 1]
#  [0 1 0]
#  [1 0 0]]
##################################################################
## 3. LabelEncoder()
x = ['jrp', 'sky', 'jrp', 'flower']  # 会按字典序先排一下
label_encoder = LabelEncoder()
print(label_encoder.fit_transform(x))  # [1 2 1 0]; 这个生成 1-d, 上面那个 2-d one-hot
