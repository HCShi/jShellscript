#!/usr/bin/python3
# coding: utf-8
import numpy as np  # 导入数值计算模块
from sklearn.decomposition import PCA  # 导入 PCA 模块

data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])  # 新建一个 2 维数组
new_data = PCA(n_components=1).fit_transform(data)  # 降维成 1 维并返回值

print(data, data.shape)  # (4, 2); 输出原数据
print(new_data, new_data.shape)  # (4, 1); 输出降维后的数据
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

# [[ 4.24264069]
#  [ 1.41421356]
#  [-1.41421356]
#  [-4.24264069]]

##################################################################
## 总结:
# 1. 主成分分析的数学基原理非常简单, 通过对协方差矩阵进行特征分解, 从而得出主成分(特征向量) 与对应的权值(特征值)
#    然后剔除那些较小特征值 (较小权值) 对应的特征, 从而达到降低数据维数的目的
# 2. 降维就是从 (4, 2) 降到 (4, 1); 第二个维度变化了
