#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
n = 1024    # data size
X, Y = np.random.normal(0, 1, n), np.random.normal(0, 1, n)  # 生成 1024 个呈标准正态分布的二维数据组(平均数是 0, 方差为 1) 作为一个数据集
T = np.arctan2(Y, X)    # for color value, later on; 每个点的颜色用 T 表示
# 数据集生成完毕, 现在来用 scatter plot 这个点集
##################################################################
## scatter()
plt.scatter(X, Y, s=75, c=T, alpha=.5)  # X 和 Y 作为 location, size=75, 颜色为 T, color map 用默认值, 透明度 alpha 为 50%
# x 轴显示范围定位 (-1.5, 1.5), 并用 xtick() 函数来隐藏 x 坐标轴, y 轴同理
plt.xlim(-1.5, 1.5); plt.xticks(())  # ignore xticks
plt.ylim(-1.5, 1.5); plt.yticks(())  # ignore yticks
plt.show()
##################################################################
## 亮点
# 1. T = np.arctan2(Y, X) 预先生成点的颜色
# 2. plt.xticks(()) 将坐标刻度省去
# 3. 随机正态分布的二维数组...
