#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)  # uniform 均匀分布
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)  # 因为有随机过程, 所以 Y1 和 Y2 并不一样
plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())
# 基本配置完毕
##################################################################
## 画饼状图, 修改颜色, 添加注记
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
for x, y in zip(X, Y1): plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')  # ha: horizontal alignment; va: vertical alignment
for x, y in zip(X, Y2): plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')
plt.show()
##################################################################
## 重点
# 1. uniform 均匀分布
# 2. 饼状图没有坐标轴
