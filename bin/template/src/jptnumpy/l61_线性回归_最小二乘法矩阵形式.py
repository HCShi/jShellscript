#!/usr/bin/python3
# coding: utf-8
import numpy as np
X = [[1, 2],
     [1, 6],
     [1, 9],
     [1, 13]]
Y = [[4],
     [8],
     [12],
     [21]]
X, Y = np.mat(X), np.mat(Y)  # 转化为 matrix 类型, 方便操作
W = (np.dot(np.dot(np.dot(X.T, X).I, X.T), Y))
W = X.T.dot(X).I.dot(X.T).dot(Y)
W = np.dot(X.T, X).I.dot(X.T).dot(Y)  # 三种书写方式, 带括号的用 np.dot() 更加形象
print(W)  # X (4, 2), Y (4,1), W (2, 1)
# [[-0.23076923]
#  [ 1.53076923]]
##################################################################
## 总结:
# 1. X * W = Y  -> W = (X^T * X)^-1 * X^T * Y
# 2. matrix 类型数据可以 .I 求逆
# 3. matrix 和 array 都可以通过 objects 后面加 .T 得到其转置; matrix 后面加 .H 得到共轭矩阵, 加 .I 得到逆矩阵
##################################################################
## 最小二乘法测试 iris 数据集
from sklearn import datasets
from sklearn.metrics import accuracy_score
import random
# 准备数据
iris = datasets.load_iris()
iris = list(zip(iris.data, iris.target))  # 将 iris 打乱
random.shuffle(iris)
x, y = zip(*iris[:30])  # 取前 30 个
x, y = np.mat(list(x)), np.mat(list(y)).T
# 计算 w
w = np.dot(x.T, x).I.dot(x.T).dot(y); print(w)
result = list(map(int, x.dot(w)))  # 取整
print(accuracy_score(result, y))  # 0.766666666667
