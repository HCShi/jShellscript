#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
# 设置基本信息
x = np.linspace(-3, 3, 50)
y = 0.1 * x
plt.figure()
plt.plot(x, y, linewidth=10)
plt.ylim(-2, 2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
##################################################################
## 设置 x 轴和 y 轴 的刻度数字进行透明度设置
# label.set_fontsize(12) 重新调节字体大小;
# bbox 设置目的内容的透明度相关参;
# facecolor 调节 box 前景色;
# edgecolor 设置边框, 本处设置边框为无;
# alpha 设置透明度
for label in ax.get_xticklabels() + ax.get_yticklabels():  # 直接遍历所有的 tick
    label.set_fontsize(20)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.2))
plt.show()
