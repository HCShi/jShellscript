#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
# 定义 x, y 的范围
x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2
##################################################################
## 进行基本绘制
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')  # plot the second curve in this figure with certain parameters
##################################################################
## xlim(): set x limits 坐标轴范围; xlabel(): 设置 x 轴名称
plt.xlim((-1, 2))  # plt.xlim(-1, 2); 两种写法
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')
##################################################################
## xticks(): x 轴刻度
new_ticks = np.linspace(-1, 2, 5)  # 这里和 xlim 没有冲突; xticks 表示的是坐标轴范围; xlim 表示图像范围
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],  # 对应刻度设置名称
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
# to use '$ $' for math text and nice looking, e.g. '$\pi$'
plt.show()
