#!/usr/bin/python3
# coding: utf-8
##################################################################
## LinearRegression 在回归的模型中, 目标值是输入值的线性组合
# y = w0 + w1*x1 + w2*x2 + ... + wp*xp
# 其中 w = (w_1,..., w_p) 作为 coef_(因数), w_0 作为 intercept_(截距)
# 线性回归拟合一个线性模型, 根据最小二乘法最小化样本与模型的残差
from sklearn import linear_model
clf = linear_model.LinearRegression()
clf.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])  # X = [[0, 0], [1, 1], [2, 2]]; y = [0, 1, 2]
print(clf.coef_)  # [ 0.5,  0.5]; 1*0.5 + 1*0.5 = 1

##################################################################
## knn 分类器 (k-nearest neighbors)
# 最简单的分类算法就是最近邻居算法: 给一个新的数据, 取在 n 维空间中离它最近的样本的标签作为它的标签, 这里的 n 由样本的特征数量决定
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier()
knn.fit(iris.data, iris.target)
print(knn.predict([[0.1, 0.2, 0.3, 0.4]]))  # [0]

##################################################################
## KMeans 聚类
# 如果鸢尾花卉数据样本并没有包括它的目标值在里面, 而我们只知道有三种鸢尾花而已, 那么就可以使用无监督算法来对样本进行聚类分组
# 最简单的聚类算法是 k-means 算法, 它将数据分成 k 类, 将一个样本分配到一个类中时,
# 分配依据是该样本与所分配类中已有样本的均值 (可以想象该类中已分配样本的质心的位置) 的距离
# 同时因为新加入了一个样本, 均值也会更新 (质心的位置发生变化)
# 这类操作会持续几轮直至类收敛, 持续的轮数由 max_iter 决定
# http://www.naftaliharris.com/blog/visualizing-k-means-clustering/ 这里有一个演示, 能直观地感受 k-means 算法
from sklearn import cluster, datasets
iris = datasets.load_iris()
k_means = cluster.KMeans(n_clusters=3)  # 分成 3 类
print(k_means.fit(iris.data))  # KMeans(copy_x=True, init='k-means++', ...
# 分别抽取打印 k-means 的分类结果与数据的实际结果
print(k_means.labels_[::10])  # [0 0 0 0 0 1 1 1 1 1 2 2 2 2 2]
print(iris.target[::10])      # [0 0 0 0 0 1 1 1 1 1 2 2 2 2 2]
