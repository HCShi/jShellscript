#!/usr/bin/python3
# coding: utf-8
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
##################################################################
## iris: 数值特征, 多分类
# iris 安德森鸢尾花卉数据集是一类多重变量分析的数据集, 其数据集包含了 150 个样本, 都属于鸢尾属下的三个亚属, 分别是山鸢尾、变色鸢尾和维吉尼亚鸢尾
# 四个特征被用作样本的定量分析, 它们分别是 花萼和花瓣 的 长度和宽度
# This data sets consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) petal and sepal length, stored in a 150x4 numpy.ndarray
# The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width.
iris = datasets.load_iris()
data, target = datasets.load_iris(True); print(data.shape, target.shape)  # (150, 4) (150,); 可以直接这样玩
print(dir(iris))  # ['DESCR', 'data', 'feature_names', 'target', 'target_names']; 和其他数据集相比真少
print(iris.target_names)  # ['setosa' 'versicolor' 'virginica']
print(iris.feature_names)  # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
print(iris.data.shape, iris.data[0])  # (150, 4) [ 5.1  3.5  1.4  0.2]
print(iris.target.shape, set(iris.target))  # (150,) {0, 1, 2}; 只有 3 类
## plot
plt.scatter(iris.data[:, 0], iris.data[:, 1]); plt.show()  # 不同特征之间没有颜色区分
plt.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target); plt.show()  # 颜色不太好看
plt.scatter(iris.data[:, 0], iris.data[:, 1], c=Y, cmap=plt.cm.Paired); plt.show()  # 有两块揉在一块了, 要用三维图像
# 用其中三种属性画 三维图
ax = Axes3D(plt.figure()); ax.scatter(iris.data[:, 0], iris.data[:, 1], iris.data[:, 2], c=iris.target); plt.show()
data = PCA(n_components=3).fit_transform(iris.data)
ax = Axes3D(plt.figure()); ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=iris.target); plt.show()
##################################################################
## digits: 和 mnist 比太小了, 不适合进行深度学习
# digits 手写数字数据集包含了来自 44 个作者的 250 个样本, 通常被用作手写数字预测
# This dataset is made up of 1797 8x8 images. Each image, like the one shown below, is of a hand-written digit.
# In order to utilize an 8x8 figure like this, we’d have to first transform it into a feature vector with length 64.
digits = datasets.load_digits()
print(dir(digits))  # ['DESCR', 'data', 'images', 'target', 'target_names']
print(digits.images.shape)  # (1797, 8, 8)
print(digits.data.shape)  # (1797, 64); data 是 image 的一个变形
print(digits.target_names)  # [0 1 2 3 4 5 6 7 8 9]
print(digits.target)  # [0, 1, 2, ..., 8, 9, 8]; 查看数据集目标值
## 绘制最有一副图, 8
plt.imshow(digits.images[-1]); plt.show()  # 好丑, 要美化
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r); plt.show()
##################################################################
## 总结:
# 1. datasets 的数据都是 numpy.ndarray 对象, 有 .T, 没有 .I, .H; 可以 np.mat() 变成 matrx 对象
