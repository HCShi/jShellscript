#!/usr/bin/python3
# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
# 获得 x, y 的取值范围
x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2
# figure() 的作用范围是到下一个 figure() 为止; 每一个 figure() 是一个独立的图像窗口
##################################################################
## 定义第一个 figure; 并使用 plt.plot(x, y1) 画曲线
# plt.figure()  # 第一个 figure() 可以省略
plt.plot(x, y1)
##################################################################
## 第二个 figure
plt.figure(num=3, figsize=(8, 5))  # 编号为 3; 大小为 (8, 5)
plt.plot(x, y2)  # 画曲线, 下面又画了一条线, 一个 figure 上有两条线
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')  # plot the second curve in this figure with certain parameters
##################################################################
## 会将所有的 figure 放出来
plt.show()
##################################################################
## plt.show() 阻塞后再次画出
plt.figure(num=4, figsize=(8, 5))  # 编号为 4
plt.plot(x, y2)
plt.show()
##################################################################
## 总结:
# 1. 每次的 plt.show() 都会阻塞, 直到关闭窗口
# 2. plt.show() 之前定义多个 figure() 可以同时画出多个窗口
# 3. subplot() 可以将多幅图放到一个窗口
