#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
# 设置 x, y 范围
x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1; y2 = x ** 2
##################################################################
## 见上一个的解释
plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')  # plot the second curve in this figure with certain parameters
plt.xlim((-1, 2)); plt.ylim((-2, 3))
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           ['$really\ bad$', '$bad$', '$normal$', '$good$', '$really\ good$'])
##################################################################
## 删掉 顶部和右侧 的坐标轴
## gca(): 坐标轴信息; spines(): 设置边框; set_color() 默认为白色
ax = plt.gca()  # gca = 'get current axis'; 获取当前坐标轴信息
ax.spines['right'].set_color('none')  # 将顶部和右侧的坐标轴删除; 然后就可以将左侧的移动到中间, 更加好看
ax.spines['top'].set_color('none')
##################################################################
## 设置剩下的 x 轴
## xaxis.set_ticks_position() 设置 x 坐标刻度 数字或名称 的位置; (所有位置: top, bottom, both, default, none)
## set_position() 设置边框位置
ax.xaxis.set_ticks_position('bottom')  # 默认就是 'bottom'
ax.spines['bottom'].set_position(('data', 0))  # y = 0 的位置; (位置所有属性: outward, axes, data)
# the 1st is in 'outward' | 'axes' | 'data';  # axes: percentage of y axis;  # data: depend on y data
##################################################################
## 设置剩下的 y 轴
ax.yaxis.set_ticks_position('left')  # ACCEPTS: [ 'left' | 'right' | 'both' | 'default' | 'none' ]
ax.spines['left'].set_position(('data', 0))
plt.show()
