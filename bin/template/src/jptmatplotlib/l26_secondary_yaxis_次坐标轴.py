#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
# 次坐标, 就是有两个 y 轴
x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 * y1  # y1 和 y2 相互倒置

fig, ax1 = plt.subplots()  # 获取 figure 默认的坐标系 ax1

ax2 = ax1.twinx()    # mirror the ax1; 对 ax1 调用 twinx() 方法, 生成如同镜面效果后的 ax2
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b-')  # 将 y1, y2 分别画在 ax1, ax2 上

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='g')
ax2.set_ylabel('Y2 data', color='b')

plt.show()
