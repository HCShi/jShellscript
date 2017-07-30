#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# matplotlib 的 subplot 还可以是分格的, 这里介绍三种方法
##################################################################
## method 1: subplot2grid
plt.figure()
##################################################################
## plt.subplot2grid 来创建第 1 个小图
# (3, 3) 表示将整个图像窗口分成 3 行 3 列, (0, 0) 表示从第 0 行第 0 列开始作图, colspan=3 表示列的跨度为 3, rowspan=1 表示行的跨度为 1
# colspan 和 rowspan 缺省, 默认跨度为 1
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)  # stands for axes
ax1.plot([1, 2], [1, 2])  # 画小图
ax1.set_title('ax1_title')  # 设置小图的标题
##################################################################
## 创建剩下几个小窗
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))  # ax4 和 ax5, 使用默认 colspan, rowspan; 默认值为 1
ax4.scatter([1, 2], [2, 2])  # 使用 ax4.scatter 创建一个散点图, 使用 ax4.set_xlabel 和 ax4.set_ylabel 来对 x 轴和 y 轴命名
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')
ax5 = plt.subplot2grid((3, 3), (2, 1))
##################################################################
## method 2: gridspec
# 使用 plt.figure() 创建一个图像窗口, 使用 gridspec.GridSpec 将整个图像窗口分成 3 行 3 列
plt.figure()
gs = gridspec.GridSpec(3, 3)
# use index from 0
ax6 = plt.subplot(gs[0, :])  # 表示这个图占第 0 行和所有列
ax7 = plt.subplot(gs[1, :2])  # 表示这个图占第 1 行和第 2 列前的所有列
ax8 = plt.subplot(gs[1:, 2])  # 表示这个图占第 1 行后的所有行和第 2 列
ax9 = plt.subplot(gs[-1, 0])  # 表示这个图占倒数第 1 行和第 0 列
ax10 = plt.subplot(gs[-1, -2])  # 表示这个图占倒数第 1 行和倒数第 2 列
##################################################################
## method 3: easy to define structure
# plt.subplots 建立一个 2 行 2 列的图像窗口
# sharex=True 表示共享 x 轴坐标, sharey=True 表示共享 y 轴坐标.
# ((ax11, ax12), (ax13, ax14)) 表示第 1 行从左至右依次放 ax11 和 ax12, 第 2 行从左至右依次放 ax13 和 ax14
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1,2], [1,2])  # 创建一个散点图

plt.tight_layout()  # 表示紧凑显示图像
plt.show()
