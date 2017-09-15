#!/usr/bin/python3
# coding: utf-8
from matplotlib import pyplot as plt
from sklearn.cluster import k_means
from sklearn.metrics import silhouette_score  # 导入轮廓系数计算模块
import pandas as pd
file = pd.read_csv("cluster_data.csv", header=0)
##################################################################
## 肘部法则
index, inertia = [], []  # 横坐标, 距离总和
for i in range(9):
    model = k_means(file, n_clusters=i + 1)
    index.append(i + 1)
    inertia.append(model[2])
plt.plot(index, inertia, "-o")  # 绘制出 '肘部' 与 '聚类 K 值' 变化的折线图
##################################################################
## 轮廓系数
index2, silhouette = [], []  # 横坐标, 轮廓系数列表
for i in range(8):  # K 从 2 ~ 10 聚类
    model = k_means(file, n_clusters=i + 2)
    index2.append(i + 2)
    silhouette.append(silhouette_score(file, model[1]))  # 直接计算轮廓系数的方法
plt.figure(); plt.plot(index2, silhouette, "-o")  # 我们可以很清楚的看出, K=3 对应的轮廓系数数组最大, 也更接近于 1
plt.show()

# 绘制出轮廓系数与聚类 K 值变化的折线图
##################################################################
## 总结:
# 肘部法则
# 1. 当我们的 K 值增加时, 也就是类别增加时, 这个数值应该是会降低的;
#    直到聚类类别的数量和样本的总数相同时, 也就是说一个样本就代表一个类别时, 这个数值会变成 0
# 2. model 第三个数组表示样本距最近聚类中心的距离总和
# 3. 畸变程度最大的点被称之为「肘部」; 这里的「肘部」明显是 K=3; 这也说明, 将样本聚为 3 类的确是最佳选择

# 轮廓系数
# 1. 轮廓系数综合了聚类后的两项因素: 内聚度和分离度;
#    内聚度就指一个样本在簇内的不相似度, 而分离度就指一个样本在簇间的不相似度
# 2. silhouette_score(file, model[1]) 直接计算轮廓系数的方法
# 3. 轮廓系数越接近于 1, 代表聚类的效果越好
