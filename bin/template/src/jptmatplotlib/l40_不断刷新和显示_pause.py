#!/usr/bin/python3
# coding: utf-8
##################################################################
## 准备数据
import numpy as np
x = np.linspace(-10, 10, 10)
y = np.square(x)
##################################################################
## 开始画图
import matplotlib.pyplot as plt
ax = plt.subplot(1, 1, 1)  # 这里一定要找到 ax 指针
plt.ion()  # Turn interactive mode on
plt.show()  # 在这里 show() 下面 pause(), 所以要在上面得到 ax 指针
for i in range(10):
    try: ax.lines.remove(lines[0])  # 因为第一次可能还没有 lines
    except Exception: pass
    y -= 10
    lines = ax.plot(x, y)  # 如果直接用 plt.plot(x, y) 会找不到原来的
    plt.pause(1)
##################################################################
## 另一种错误的方式
# y = np.square(x)
# plt.ion()
# plt.show()
# for i in range(10):
#     try: plt.lines.remove(lines[0])  # 因为第一次可能还没有 lines
#     except Exception: pass
#     y -= 10
#     lines = ax.plot(x, y)
#     plt.pause(1)
