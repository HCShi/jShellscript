#!/usr/bin/python3
# coding: utf-8
import numpy as np
from matplotlib import pyplot as plt  # pyplot() 是 matplotlib 库中最重要的函数, 用于绘制 2D 数据
##################################################################
# 方程
x = np.arange(1, 11)
y =  2 * x +  5  # 绘制方程 y = 2x + 5
plt.title("Matplotlib demo")
plt.xlabel(" x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y, "ob")  # 要显示圆来代表点, 而不是上面示例中的线, 'o' 圆标记, 'b' blue;
plt.show()
# ndarray 对象 x 由 np.arange() 函数创建为 x 轴上的值; y 轴上的对应值存储在另一个数组对象 y 中, 这些值使用 matplotlib 软件包的 pyplot 子模块的 plot() 函数绘制
##################################################################
# 绘制正弦波
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.title("sine wave form")
plt.plot(x, y)
plt.show()
##################################################################
# subplot() 函数允许你在同一图中绘制不同的东西
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)  # 计算正弦和余弦曲线上的点的 x 和 y 坐标
plt.subplot(2, 1, 1)  # 建立 subplot 网格, 高为 2, 宽为 1; 激活第一个 subplot
plt.plot(x, y_sin)  # 绘制第一个图像
plt.title('Sine')
plt.subplot(2, 1, 2)  # 将第二个 subplot 激活, 并绘制第二个图像
plt.plot(x, y_cos)
plt.title('Cosine')
plt.show()
##################################################################
# bar() 来生成条形图
x = [5, 8, 10]
y = [12, 16, 6]
x2 = [6, 9, 11]
y2 = [6, 15, 7]
plt.bar(x, y, align='center')
plt.bar(x2, y2, color='g', align='center')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()
