#!/usr/bin/python3
# coding: utf-8
import numpy as np
from matplotlib import pyplot as plt  # pyplot() 是 matplotlib 库中最重要的函数, 用于绘制 2D 数据
##################################################################
# 方程 line
x = np.arange(1, 11); y =  2 * x +  5  # 绘制方程 y = 2x + 5; ndarray 对象 x 由 np.arange() 函数创建为 x 轴上的值; y 轴上的对应值存储在另一个数组对象 y 中
plt.subplot(2, 2, 1); plt.plot(x, y, "ob"); plt.title("function demo"); plt.xlabel(" x axis caption"); plt.ylabel("y axis caption")
# 要显示圆来代表点, 而不是上面示例中的线, 'o' 圆标记, 'b' blue; 下面的 'm' 表示品红, 'x' 表示 x 号画图, 顺序可以反
##################################################################
# subplot(x, y, n) 长 x 个, 高 y 个, 在第 n 个里面画图; 函数允许你在同一图中绘制不同的东西
x = np.arange(0, 3 * np.pi, 0.1); y_sin = np.sin(x); y_cos = np.cos(x)  # 计算正弦和余弦曲线上的点的 x 和 y 坐标
plt.subplot(2, 2, 2); plt.plot(x, y_sin, 'mx', label='h1, theta_1=0'); plt.title('Sine'); plt.legend('upper left')  # 使用 label 属性后, 必须调用 legend()
plt.subplot(2, 2, 3); plt.plot(x, y_cos); plt.title('Cosine')
##################################################################
# bar() 来生成条形图
x = [5, 8, 10]; y = [12, 16, 6];
x2 = [6, 9, 11]; y2 = [6, 15, 7]
plt.subplot(2, 2, 4); plt.bar(x, y, align='center'); plt.bar(x2, y2, color='g', align='center')  # 可以将两个 plt.plot()/bar() 塞到一个 subplot() 中
plt.title('Bar graph'); plt.ylabel('Y axis'); plt.xlabel('X axis'); plt.grid(True)
##################################################################
## savefig() 保存图像
plt.savefig('tmp.jpg')
plt.show()
##################################################################
## 总结:
# 1. label, title, grid 这些属性只对上一个 plot() 管用, 如果前面没有, 就对下一个起作用
# 2. 每次 plt.show() 都会把缓存的图像一次性画出来
