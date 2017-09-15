#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
def f(x, y): return x + y  # 高程函数
##################################################################
## 数据集
x, y = [1, 2, 3], [4, 5, 6]
X, Y = np.meshgrid(x, y)  # meshgrid 在二维平面中将每一个 x 和每一个 y 分别对应起来, 编织成栅格
tmp = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]  # 中间 凹进去
print(X, '\n', Y)
# [[1 2 3] [1 2 3] [1 2 3]]
# [[4 4 4] [5 5 5] [6 6 6]]
print(f(X, Y)) # [[5 6 7] [6 7 8] [7 8 9]]
##################################################################
## plt.contourf 把颜色加进去
# X, Y, f(X,Y); 透明度 0.75, 并将 f(X, Y) 的值对应到 color map 的暖色组中寻找对应颜色
# use plt.contourf to filling contours; X, Y and value for (X, Y) point
plt.figure(); plt.contourf(X, Y, tmp, 8, alpha=.75, cmap=plt.cm.hot)  # 8 代表等高线的密集程度
plt.figure(); plt.contourf(X, Y, X, 8, alpha=.75, cmap=plt.cm.hot)  # 8 代表等高线的密集程度
plt.figure(); plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)  # 8 代表等高线的密集程度
##################################################################
## plt.contour 添加等高线
# X, Y, f(X, Y) 颜色选黑色, 线条宽度选 0.5;
# use plt.contour to add contour lines
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)  # 8 代表等高线的密集程度
##################################################################
## adding label
plt.clabel(C, inline=True, fontsize=10)  # inline 控制是否将 Label 画在线里面, 字体大小为 10; 内容默认为 高度
# plt.xticks(()); plt.yticks(())  # 并将坐标轴隐藏
plt.show()
##################################################################
## 重点
# f(x, y) = x + y:
# [6, 6, 6]|[7, 8, 9]
# [5, 5, 5]|[6, 7, 8]
# [4, 4, 4]|[5, 6, 7]
# ---------------------------
#          |[1, 2, 3]
#          |[1, 2, 3]
#          |[1, 2, 3]
# 1. contourf() 是填充颜色的, (X, Y, f(X, Y), 8) 中 X, Y 没什么用, 必须是 meshgrid 的返回值才能很好的表示
#    f(X, Y) 是高程, 具体的放置位置见上面的表示
#    8 才是决定有几种颜色, 和几条等值线
# 2. plt.cm.hot 中, 数值越小, 颜色越深
# 3. 所谓等值线, 是指由函数值相等的各点连成的平滑曲线;
#    等值线可以直观地表示二元函数值的变化趋势, 例如等值线密集的地方表示函数值在此处的变化较大
# 4. x, y 轴的范围还是 [1, 2, 3], [4, 5, 6] 原始的范围
