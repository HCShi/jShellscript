#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features. 这样可以画二维图
y = iris.target
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

##################################################################
## 取 4 个属性中的 2 个属性, 这样能够用二维图展示出来
plt.figure(2, figsize=(8, 6))
plt.clf()
# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=iris.target, cmap=plt.cm.Set1, edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
##################################################################
## 三维图; 用 PCA 算法将 4 个属性将维成三个属性
# To getter a better understanding of interaction of the dimensions plot the first three PCA dimensions
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(iris.data)
print(X_reduced.shape, iris.data.shape)  # (150, 3) (150, 4)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y, cmap=plt.cm.Set1, edgecolor='k', s=40)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector"); ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector"); ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector"); ax.w_zaxis.set_ticklabels([])

plt.show()
##################################################################
## 总结:
# 1. 三维作图和二维相似, 都是 plot 和 scatter
# 2. iris 中的 X 是 (150, 4) 的矩阵, 4 个属性中取 3 个刚好可以作为 3 个维度的坐标; y 作为颜色的属性
