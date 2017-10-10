#!/usr/bin/python3
# coding: utf-8
from sklearn import preprocessing
##################################################################
## 1. OneHotEncoder() 将变量的特征值转换为稀疏矩阵
x = np.array([[1, 2, 3], [2, 5, 6]])
one_hot_encoder = preprocessing.OneHotEncoder()
print(one_hot_encoder.fit_transform(x))  # 稀疏表示形式
print(one_hot_encoder.fit_transform(x).toarray())
print(one_hot_encoder.fit_transform(x).todense())  # 密集表示形式, 同 .toarray()
# x 有三个特征: 第一个特征的取值为 1、2, 第二特征的取值为 2、5, 第三个特征的取值为 3、6;
# 可知三个特征的最大特征值分别为 2、5、6, 每个特征的取值都必须在 range(n_values[i]) 范围内, 因此 n_values=[3, 6, 7]
print(one_hot_encoder.n_values_)  # [3, 6, 7]; n_values_ 属性: 取每个特征的最大特征值 +1
print(one_hot_encoder.feature_indices_)  # [0,  3,  9, 16]; feature_indices_ 属性: n_values_ 的累计
print(one_hot_encoder.active_features_)  # [ 1,  2,  5,  8, 12, 15]; active_features_ 属性
