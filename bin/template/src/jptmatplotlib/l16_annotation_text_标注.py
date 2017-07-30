#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
##################################################################
## 具体解释见前面的
# 设置 x, y 范围
x = np.linspace(-3, 3, 50); y = 2 * x + 1
plt.figure(num=1, figsize=(8, 5))
plt.plot(x, y)
ax = plt.gca()  # get current axis
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')  # 去掉 右侧和上侧 的坐标轴
ax.xaxis.set_ticks_position('bottom')  # x轴 刻度放到下面
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')  # y轴 刻度放到左面
ax.spines['left'].set_position(('data', 0))  # 将坐标轴放到中间, 而不是四周
##################################################################
## matplotlib 中的 annotation 有两种方法,  一种是用 plt 里面的 annotate, 一种是直接用 plt 里面的 text 来写标注
x0 = 1; y0 = 2 * x0 + 1  # 标注出点 (x0, y0) 的位置信息
plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)  # 画出一条垂直于 x 轴的虚线
plt.scatter([x0, ], [y0, ], s=50, color='b')  # 在 (x0, y0) 画一个圆点
# plt.scatter(x0, y0, s=50, color='b')  # 和上一句作用相同
##################################################################
## method 1:
# xy=(x0, y0) 这个点进行标注;
# xycoords='data': 基于数据的值来选位置;
# xytext=(+30, -30) 和 textcoords='offset points' 对于标注位置的描述 和 xy 偏差值;
# arrowprops 是对图中箭头类型的一些设置
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
##################################################################
## method 2:
# 其中 -3.7, 3 是选取 text 的位置, 空格需要用到转字符 \ , fontdict 设置文本字体
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})
plt.show()
