#!/usr/bin/python3
# coding: utf-8
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()  # ax 可以得到 坐标轴
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))  # 得到图形对象
##################################################################
## 构造自定义动画函数 animate, 用来更新每一帧上各个x对应的y坐标值, 参数表示第 i 帧
def animate(i):
    line.set_ydata(np.sin(x + i/10.0))  # update the data
    return line,
# Init only required for blitting to give a clean slate; 构造开始帧
def init():
    line.set_ydata(np.sin(x))
    return line,
##################################################################
## 调用 FuncAnimation 函数生成动画
# fig 进行动画绘制的 figure
# func 自定义动画函数, 即传入刚定义的函数 animate
# frames 动画长度, 一次循环包含的帧数
# init_func 自定义开始帧, 即传入刚定义的函数 init
# interval 更新频率, 以 ms 计
# blit 选择更新所有点, 还是仅更新产生变化的点; 应选择 True, 但 mac 用户请选择 False, 否则无法显示动画
ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init,
                              interval=20, blit=False)
plt.show()
##################################################################
# 可以将动画以 mp4 格式保存下来, 但首先要保证你已经安装了 ffmpeg 或者 mencoder
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
