#!/usr/bin/python3
# coding: utf-8
from matplotlib import pyplot as plt
# x, y, cls = [1, 2], [3, 4], [0, 1]
x, y, cls = range(10), range(10), range(10)  # 两种不同的设置 x, y, cls 的方法

plt.scatter(x, y, c=cls)  # 设置了 c, 而没有设置 cmap, 会使用默认的 colormap
plt.show()
from matplotlib.colors import ListedColormap  # 加载色彩模块
cm_color = ListedColormap(['red', 'yellow'])  # 指定两种颜色
plt.scatter(x, y, c=cls, cmap=cm_color)  # 设置 cmap 参数并重新绘图
plt.show()
##################################################################
## 总结:
# 1. scatter(x, y, c, cmap) 中 c 与 cmap 的 shape 可以不相同
# 2. cmap=None 为默认值, 可以只设置 c, 不设置 cmap
