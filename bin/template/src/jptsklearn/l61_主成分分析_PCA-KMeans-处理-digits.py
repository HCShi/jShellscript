#!/usr/bin/python3
# coding: utf-8
from sklearn import datasets
from matplotlib import pyplot as plt
from sklearn import decomposition
from sklearn.cluster import KMeans
import numpy as np
##################################################################
## 准备数据
digits_data = datasets.load_digits()
X = digits_data.data; print(X.shape)  # (1797, 64)
y = digits_data.target
##################################################################
## 使用 PCA 将数据降维到 二维
estimator = decomposition.PCA(n_components=2)
reduce_data = estimator.fit_transform(X); print(reduce_data.shape)  # (1797, 2)
##################################################################
## 使用 KMeans 进行分类
model = KMeans(n_clusters=10)
model.fit(reduce_data)
##################################################################
## 计算聚类过程中的决策边界
x_min, x_max = reduce_data[:, 0].min() - 1, reduce_data[:, 0].max() + 1
y_min, y_max = reduce_data[:, 1].min() - 1, reduce_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, .05), np.arange(y_min, y_max, .05))
print(xx.shape, yy.shape)  # (1192, 1298) (1192, 1298)
result = model.predict(np.c_[xx.ravel(), yy.ravel()])
## 将决策边界绘制出来
result = result.reshape(xx.shape)
plt.contourf(xx, yy, result, cmap=plt.cm.Greys)
## 这里是将 reduce_data 点绘制出来
plt.scatter(reduce_data[:, 0], reduce_data[:, 1], c=y, s=15)
## 绘制聚类中心点
center = model.cluster_centers_
plt.scatter(center[:, 0], center[:, 1], marker='p', linewidths=2, color='b', edgecolors='w', zorder=20)
## 图像参数设置
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.show()
# 图中, 不同的色块区域代表一类; 这里色块的颜色没有意义, 只表示类别
# 散点代表数据, 散点的颜色表示数据原始类别
# 我们可以看出, 虽然原始数据已经从 16 维降维 2 维, 但某几个数字的依旧有明显的成团现象
##################################################################
## 总结:
# 1. 主成分分析旨在降低数据的维数, 通过保留数据集中的主要成分来简化数据集, 降低模型学习时间
# 2. 之前, 我们用支持向量机完成了分类, 即预测哪一张图像代表哪一个数字; 现在, 我们采用相同的数据集完成聚类分析, 即将全部数据集聚为 10 个类别
# 3. 由于原数据集维度达到 64, 所以这里要进行 PCA 降维
# 4. PCA 一般和 KMeans 结合使用; 先降维, 再聚类
