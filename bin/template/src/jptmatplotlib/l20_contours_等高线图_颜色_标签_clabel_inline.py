#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
# the height function
def f(x, y): return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)
##################################################################
## 数据集即三维点 (x, y) 和对应的高度值, 共有 256 个点
n = 256
n = 3
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)  # meshgrid 在二维平面中将每一个 x 和每一个 y 分别对应起来, 编织成栅格
##################################################################
## plt.contourf 把颜色加进去
# X, Y, f(X,Y); 透明度 0.75, 并将 f(X, Y) 的值对应到 color map 的暖色组中寻找对应颜色
# use plt.contourf to filling contours; X, Y and value for (X, Y) point
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)  # 8 代表等高线的密集程度
##################################################################
## plt.contour 添加等高线
# X, Y, f(X, Y) 颜色选黑色, 线条宽度选 0.5;
# use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)  # 8 代表等高线的密集程度
##################################################################
## adding label
plt.clabel(C, inline=True, fontsize=10)  # inline 控制是否将 Label 画在线里面, 字体大小为 10
plt.xticks(()); plt.yticks(())  # 并将坐标轴隐藏
plt.show()
##################################################################
## 重点
# 1. meshgrid 好奇葩的函数
# 2. f() 函数中 exp()
# 3. 去掉坐标轴
