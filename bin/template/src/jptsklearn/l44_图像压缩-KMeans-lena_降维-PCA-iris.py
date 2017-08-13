#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
from sklearn import cluster
##################################################################
# KMeans 图像压缩
# 聚类的一个典型应用就是对图片进行色调分离, 这里以经典的 lena 图片进行操作...; lena 因为证书问题被去掉了...
from scipy import misc
# lena = misc.lena().astype(np.float32)
lena = misc.face().astype(np.float32); print(lena.shape)  # (768, 1024, 3); 其实是一只小棕熊
plt.gray(); plt.imshow(lena); plt.show()  # 显示图片
X = lena.reshape((-1, 1)); print(X.shape)  # (2359296, 1); We need an (n_sample, n_feature) array

k_means = cluster.KMeans(n_clusters=5)
k_means.fit(X)
values = k_means.cluster_centers_.squeeze(); print(values)  # [ 113.17304993   25.68023682  202.42715454   71.94200134  155.77253723]
labels = k_means.labels_; print(labels, labels.shape, np.unique(labels))  # [0 0 0 ..., 0 4 3] (2359296,) [0 1 2 3 4]
lena_compressed = np.choose(labels, values); print(lena_compressed.shape)  # (2359296,)
lena_compressed.shape = lena.shape; print(lena_compressed)  # 竟然通过修改 shape 属性, 就可以该数据的形状...
print(lena_compressed.shape)  # (768, 1024, 3)
plt.gray(); plt.imshow(lena_compressed); plt.show()
##################################################################
## PCA 降维
# 如果空间中的数据点看上去几乎就在一个平面上, 这意味着数据的某一个特征几乎可以由另两个特征计算得到, 这种时候我们就可以进行数据降维
# iris 数据就可以进行数据降维
# 这里使用主成分分析 (PCA: Principal Component Analysis)
from sklearn import decomposition
# pca = decomposition.PCA(n_components=2); pca.fit(iris.data); X = pca.transform(iris.data)  # 这三句合成一句
X = decomposition.PCA(n_components=2).fit_transform(iris.data)

print(iris.data.shape, X.shape)  # (150, 4) (150, 2); 从 四维 降到了 二维
print(iris.target, iris.target.shape, np.unique(iris.target))  # (150,), [0 1 2]

# 可视化
plt.scatter(X[:, 0], X[:, 1], c=iris.target)
plt.show()
# 降维除了可以用在数据可视化上, 还可以通过对数据进行预处理提高监督学习处理数据的效率
