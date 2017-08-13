#!/usr/bin/python3
# coding: utf-8
from sklearn import datasets
import numpy as np
##################################################################
## iris 安德森鸢尾花卉数据集是一类多重变量分析的数据集, 其数据集包含了 150 个样本, 都属于鸢尾属下的三个亚属, 分别是山鸢尾、变色鸢尾和维吉尼亚鸢尾
## 四个特征被用作样本的定量分析, 它们分别是 花萼和花瓣 的 长度和宽度
# This data sets consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica) petal and sepal length, stored in a 150x4 numpy.ndarray
# The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width.
iris = datasets.load_iris()  # 加载数据集
print(dir(iris))  # ['DESCR', 'data', 'feature_names', 'target', 'target_names']
print(iris.target_names)  # ['setosa' 'versicolor' 'virginica']
print(iris.feature_names)  # ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

# 数据存储在 .data 成员中, 它是一个 (n_samples, n_features) numpy 数组
print(iris.data.shape)  # (150, 4)
print(iris.data[0])  # [ 5.1  3.5  1.4  0.2]

# 每一个样本的类别存储在 .target 属性中, 它是一个一维数组
print(iris.target.shape)  # (150,)
print(np.unique(iris.target))  # [0 1 2]  # 显示数据集中有哪些类别

# The below plot uses the first two features.
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
X = iris.data[:, :2]  # we only take the first two features; Numpy 可以很任性的截取一个 子矩阵
Y = iris.target
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
# plt.show()  # 这里直接画是 二维的, 不好看, 下面是画三维的; 详细介绍见 jptmatplotlib
# To getter a better understanding of interaction of the dimensions
# plot the first three PCA dimensions
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=Y,
           cmap=plt.cm.Paired)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])
plt.show()
##################################################################
## digits 手写数字数据集包含了来自 44 个作者的 250 个样本, 通常被用作手写数字预测
# This dataset is made up of 1797 8x8 images. Each image, like the one shown below, is of a hand-written digit. In order to utilize an 8x8 figure like this, we’d have to first transform it into a feature vector with length 64.
digits = datasets.load_digits()  # 加载数据集
print(dir(digits))  # ['DESCR', 'data', 'images', 'target', 'target_names']
print(digits.images.shape)  # (1797, 8, 8)
print(digits.data.shape)  # (1797, 64); data 是 image 的一个变形
print(digits.target_names)  # [0 1 2 3 4 5 6 7 8 9]

print(digits.data[0].shape)  # (64,)
print(digits.data)  # 查看底层数据
# [[  0.   0.   5. ...,   0.   0.   0.]
#  [  0.   0.   0. ...,  10.   0.   0.]
#  [  0.   0.   0. ...,  16.   9.   0.]
#  ...,
#  [  0.   0.   1. ...,   6.   0.   0.]
#  [  0.   0.   2. ...,  12.   0.   0.]
#  [  0.   0.  10. ...,  12.   1.   0.]]
print(digits.target)  # [0, 1, 2, ..., 8, 9, 8]; 查看数据集目标值
# 绘制最有一副图, 8
import matplotlib.pyplot as plt
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
