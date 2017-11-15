#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
x = np.array([i for i in range(1, 101)]); y = 100 / x  # y = 1/x
plt.subplot(2, 2, 1); plt.plot(x, y); plt.grid(True)
plt.subplot(2, 2, 2); plt.loglog(x, y)
x1 = np.log10(x); y1 = np.log10(y)  # 检查是否是真的取对数
plt.subplot(2, 2, 3); plt.plot(x1, y1); plt.grid(True)
plt.show()

x = np.array([i for i in range(1, 101)]); y = np.exp(x)  # y = e^x
plt.subplot(2, 2, 1); plt.plot(x, y); plt.grid(True)
plt.subplot(2, 2, 2); plt.loglog(x, y); plt.grid(True)
x1 = np.log10(x); y1 = np.log10(y)  # 检查是否是真的取对数
plt.subplot(2, 2, 3); plt.plot(x1, y1); plt.grid(True)
plt.show()

x = np.array([i for i in range(1, 101)]); y = x**2  # y = e^x
plt.subplot(2, 2, 1); plt.plot(x, y); plt.grid(True)
plt.subplot(2, 2, 2); plt.loglog(x, y); plt.grid(True)
x1 = np.log10(x); y1 = np.log10(y)  # 检查是否是真的取对数
plt.subplot(2, 2, 3); plt.plot(x1, y1); plt.grid(True)
plt.show()
##################################################################
## loglog() Make a plot with log scaling on both the *x* and *y* axis.
# 默认是以 10 为底
# 绘制双对数坐标图形, 绘制双对数坐标图形, 其 x 轴和 y 轴均按常用对数的刻度进行绘制, 调用形式与 plot 函数类似
# loglog(Y): 绘制向量 Y; 如果 Y 为实数, 相当于 loglog(1: length(Y),Y)
# loglog(X1, Y1, …): 同时绘制多条曲线, 函数将为不同曲线自动选择不同颜色, 以示区别
# loglog(X1, Y1, S): 字符串 S 指定了绘图的线型、节点符号和颜色, 取值及含义见 6.1.1 小节的表 6-1 、表 6-2
# loglog(…, 'PropertyName', PropertyValue): 绘制曲线, 并设置曲线的 PropertyName 属性值为 PropertyValue
##################################################################
## 总结:
# 1. y = 1/x; (x, y) 同时取对数, 结果是 线性的
# 2. y = e^x 同时取对数, 可以放缓弯曲程度
# 3. y = x^2 同时取对数, 得到线性结果
