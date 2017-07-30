#!/usr/bin/python3
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 还要额外添加一个模块, 即 Axes 3D; 3D 坐标轴显示
##################################################################
## 定义一个图像窗口, 在窗口上添加 3D 坐标轴
fig = plt.figure()
ax = Axes3D(fig)
##################################################################
## 给进 X 和 Y 值; 并将 X 和 Y 编织成栅格; 计算每一个 (X, Y) 的高程 Z
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
# height value
Z = np.sin(R)
##################################################################
## 做出一个三维曲面, 并将一个 colormap rainbow 填充颜色, 之后将三维图像投影到 XY 平面上做一个等高线图
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
"""
        Argument      Description
        ============= ================================================
        *X*, *Y*, *Z* Data values as 2D arrays
        *rstride*     Array row stride (step size), defaults to 10; 代表 row 的跨度
        *cstride*     Array column stride (step size), defaults to 10; 代表 column 的跨度
        *color*       Color of the surface patches
        *cmap*        A colormap for the surface patches.
        *facecolors*  Face colors for the individual patches
        *norm*        An instance of Normalize to map values to colors
        *vmin*        Minimum value to map
        *vmax*        Maximum value to map
        *shade*       Whether to shade the facecolors
        ============= ================================================
"""
##################################################################
## 添加 XY 平面的等高线; I think this is different from contours.py
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
"""
        Argument    Description
        ==========  ================================================
        *X*, *Y*,   Data values as numpy.arrays
        *Z*
        *zdir*      The direction to use: x, y or z (default); 如果 zdir 选择了 x, 那么效果将会是对于 XZ 平面的投影
        *offset*    If specified plot a projection of the filled contour
                    on this position in plane normal to zdir
        ==========  ================================================
"""
ax.set_zlim(-2, 2)
plt.show()
