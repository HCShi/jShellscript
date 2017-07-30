#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt  # 一般只会用到 pyplot 这个子模块
import numpy as np
##################################################################
## 定义 x, y 的取值范围
# plt.figure()  # figure() 只有一个的话可以省略, 还可以放后面...
x = np.linspace(-1, 1, 50)  # (-1, 1) 中间分为 50 份
# y = 2 * x + 1
y = x ** 2
##################################################################
## 画图
# plt.figure()  # 这里的两个 figure() 都可以省略, 效果相同...
plt.plot(x, y)  # 画 (x, y) 曲线
plt.show()  # 显示图像
