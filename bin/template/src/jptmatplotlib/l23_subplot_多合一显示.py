#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
##################################################################
## example 1: 大小相等
plt.figure(figsize=(6, 4))
# plt.subplot(n_rows, n_cols, plot_num); 下面两种图像窗口分列的书写方式
plt.subplot(2, 2, 1); plt.plot([0, 1], [0, 1])  # 两行两列, 第 1 个位置创建一个小图
plt.subplot(222);     plt.plot([0, 1], [0, 2])
plt.subplot(223);     plt.plot([0, 1], [0, 3])
plt.subplot(224);     plt.plot([0, 1], [0, 4])
plt.tight_layout()  # 表示紧凑显示图像
##################################################################
## example 2: 大小不相等
plt.figure(figsize=(6, 4))
plt.subplot(2, 1, 1); plt.plot([0, 1], [0, 1])  # figure splits into 2 rows, 1 col, plot to the 1st sub-fig
plt.subplot(234); plt.plot([0, 1], [0, 2])  # figure splits into 2 rows, 3 col, plot to the 4th sub-fig
plt.subplot(235); plt.plot([0, 1], [0, 3])  # figure splits into 2 rows, 3 col, plot to the 5th sub-fig
plt.subplot(236); plt.plot([0, 1], [0, 4])  # figure splits into 2 rows, 3 col, plot to the 6th sub-fig
plt.tight_layout()
plt.show()
