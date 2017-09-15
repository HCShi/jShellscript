#!/usr/bin/python3
# coding: utf-8
from sklearn import cluster           # 导入聚类模块
from matplotlib import pyplot as plt  # 导入绘图模块
import pandas as pd                   # 导入数据处理模块
import numpy as np                    # 导入数值计算模块
# 然后, 从 cluster 模块中, 导入各聚类方法; 如 K-Means 等方法需要提前确定类别数量, 也就是 K 值;
# 判断的方法很简单, 如果聚类方法中包含 n_clusters= 参数, 即代表需要提前指定; 这里我们统一确定 K = 3

# 对聚类方法依次命名
cluster_names = ['KMeans', 'MiniBatchKMeans', 'AffinityPropagation', 'MeanShift', 'SpectralClustering', 'AgglomerativeClustering', 'Birch', 'DBSCAN']
# 确定聚类方法相应参数
cluster_estimators = [
    cluster.KMeans(n_clusters=3),
    cluster.MiniBatchKMeans(n_clusters=3),
    cluster.AffinityPropagation(),
    cluster.MeanShift(),
    cluster.SpectralClustering(n_clusters=3),
    cluster.AgglomerativeClustering(n_clusters=3),
    cluster.Birch(n_clusters=3),
    cluster.DBSCAN()
]
# 读取数据集 csv 文件
data = pd.read_csv("data_blobs.csv", header=0)
X = data[['x', 'y']]
Y = data['class']

plot_num = 1  # 为绘制子图准备
# 不同的聚类方法依次运行
for name, algorithm in zip(cluster_names, cluster_estimators):
    algorithm.fit(X)  # 聚类
    if hasattr(algorithm, 'labels_'): algorithm.labels_.astype(np.int)  # 判断方法中是否由 labels_ 参数, 并执行不同的命令
    else: algorithm.predict(X)

    # 绘制子图
    plt.subplot(2, len(cluster_estimators) / 2, plot_num)
    plt.scatter(data['x'], data['y'], c=algorithm.labels_)

    # 判断方法中是否有 cluster_centers_ 参数, 并执行不同的命令
    if hasattr(algorithm, 'cluster_centers_'):
        centers = algorithm.cluster_centers_
        plt.scatter(centers[:, 0], centers[:, 1], marker="p", edgecolors="red")  # 有中心点的将其画出来

    # 绘制图标题
    plt.title(name)
    plot_num += 1

plt.show() # 显示图


##################################################################
## 总结:
# 1. 如 K-Means 等方法需要提前确定类别数量, 也就是 K 值;
#    判断的方法很简单, 如果聚类方法中包含 n_clusters= 参数, 即代表需要提前指定; 这里我们统一确定 K = 3
# 2. 在我们指定 n_clusters=3 的方法中, 除了 SpectralClustering 出现了三个特征点飘逸, 其他几种方法的结果几乎是一致的
#    除此之外, 在没有指定 n_clusters 的聚类方法中, Mean Shift 对于此数据集的适应性较好; 而亲和传播聚类方法在默认参数下, 竟然确定出了几十个类别
# 3. 具体的区别还要看 实验楼的相关说明
