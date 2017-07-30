#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
# legend 就是曲线的 label
##################################################################
## 解释见 axis.py
x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2
plt.figure()
plt.xlim((-1, 2))
plt.ylim((-2, 3))
new_sticks = np.linspace(-1, 2, 5)
plt.xticks(new_sticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
##################################################################
## legend 图例为了帮我们展示出每个数据对应的图像名称, 更好的让读者认识到你的数据结构
## 对图中的两条线绘制图例, 首先我们设置两条线的类型等信息 (蓝色实线与红色虚线)
l1, = plt.plot(x, y2, label='linear line')  # l1, 要以 , 结尾, 因为 plt.plot() 返回一个列表
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='square line')
# the "," is very important in here l1, = plt... and l2, = plt... for this step
##################################################################
## legend 将要显示的信息来自于上面代码中的 label
plt.legend(loc='upper right')  # 根据 label 自动生成图例; loc 表示图例的位置
# 会被下面的设置覆盖
##################################################################
## 分别重新设置 label; 需要设置 l1, =  和 l2, =
plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')
"""legend( handles=(line1, line2, line3),
           labels=('label1', 'label2', 'label3'),
           'upper right')
    The *loc* location codes are::
          'best' : 0,          (currently not supported for figure legends)
          'upper right'  : 1,
          'upper left'   : 2,
          'lower left'   : 3,
          'lower right'  : 4,
          'right'        : 5,
          'center left'  : 6,
          'center right' : 7,
          'lower center' : 8,
          'upper center' : 9,
          'center'       : 10,"""

plt.show()
