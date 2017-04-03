#!/usr/bin/python3
# coding: utf-8
# 要先运行 ~/miniconda3/pkgs/vibes-bin-0.2.2a1-0/bin/VIBes_viewer
from vibes import *
vibes.beginDrawing()      # initiate the connection with the viewer
vibes.newFigure("myfig")  # create a new figure named myfig
vibes.drawCircle(0, 0, 2)   # (cx, cy, R) draw a circle at (0, 0) with radius 2

vibes.drawBox(0, 1, 0, 1, color='red[blue]')  # (x.lb, x.ub, y.lb, y.ub), draw a blue square with a red border
# vibes.drawBox(0,1, 0,1, color='r[b]')  # 这个是简写
# 参数不是对角的两点, 而是 x 轴范围, y 轴范围, 所以画出来一定是矩形

vibes.drawBox(0, 2, 0, 3, color='[#000000]')  # RGB
vibes.drawBox(1, 5, 2, 4, color='[#AAAA2277]')  #RGBA

# vibes.closeFigure()  # 不带参数就是关闭当前的, 这两句关闭的语句并没有多大用, 因为画完以后会阻塞在那里, 强行关闭后相当于执行这两句话了
vibes.endDrawing()     # end the connection with the viewer
# 其他的去看 Github 上的 API 吧, 挺详细的
