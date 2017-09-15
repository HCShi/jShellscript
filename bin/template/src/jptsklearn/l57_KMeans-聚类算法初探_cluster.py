#!/usr/bin/python3
# coding: utf-8
from matplotlib import pyplot as plt
from sklearn.cluster import k_means  # scikit-learn 中的聚类算法都包含在 sklearn.cluster 方法
import pandas as pd  # pandas 主要是加载 csv
##################################################################
## 加载数据, 并进行绘制
file = pd.read_csv("cluster_data.csv", header=0)
X = file['x']
y = file['y']
plt.figure(); plt.scatter(X, y);  # 第一次画, 都是一样的颜色
##################################################################
## KMeans 初探
model = k_means(file, n_clusters=3)
print(model, '\n', model[0], '\n', model[1].shape, '\n', model[2])
# model[0]: [[ 0.26098231  0.14011151] [ 0.28288786  0.37671499] [ 0.1040997   0.28663691]]
# model[1]: (735,)
# model[2]: 3.34955881191
# model 输出的结果包含三个数组; 其中, 第一个数组表示三个聚类中心点坐标; 第二个数组表示样本聚类后类别;
# 第三个数组表示样本距最近聚类中心的距离总和
##################################################################
## 接下来, 我们就将聚类的结果绘制出来
cluster_centers = model[0]  # 聚类中心数组
cluster_labels = model[1]  # 聚类标签数组
plt.figure()
plt.scatter(X, y, c=cluster_labels)  # 第二次画, 绘制样本并按聚类标签标注颜色
for center in cluster_centers:  # 绘制聚类中心点, 标记成五角星样式, 以及红色边框
    plt.scatter(center[0], center[1], marker="p", edgecolors="red")
plt.show()  # 显示图
##################################################################
## 总结:
# 1. 两次 plot, 可以很清楚的看到结果对比
# 2. model 输出的结果包含三个数组;
#    第一个数组表示三个聚类中心点坐标;
#    第二个数组表示样本聚类后类别;
#    第三个数组表示样本距最近聚类中心的距离总和
