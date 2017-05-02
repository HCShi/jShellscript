#!/usr/bin/python3
# coding: utf-8
import numpy as np
def angle(p0, p1=np.array([0, 0]), p2=None):
    '''compute angle (in degrees) for p0p1p2 corner. Inputs: p0, p1, p2 - points in the form of [x, y] or (x, y)
1. 输入一个点表示该点与原点连线和 x 轴角度 2. 输入两个参数表示两点连线与 x 轴夹角 3. 输入三点就是求 p0p1p2 夹角 '''
    if p2 is None:
        p2 = p1 + np.array([1, 0])
    v0, v1 = np.array(p0) - np.array(p1), np.array(p2) - np.array(p1)  # Vector: p1 -> p0, p1 -> p2
    angle = np.math.atan2(np.linalg.det([v0, v1]), np.dot(v0, v1))  # 两个向量的 叉积=|a||b|sin\theta 和 点积=|a||b|con\theta, 求与 x 轴夹角
    return np.degrees(angle)
print(angle((1, 1)), angle((1, 1), (0, 0)), angle((1, 1), (0, 0), (1, 0)))

# det() 对于 2×2 矩阵, 它是左上和右下元素的乘积与其他两个的乘积的差
# dot() 返回两个数组的点积, 对于二维向量, 其等效于矩阵乘法, 对于一维数组是向量内积
# atan2(y, x) 坐标原点为起点, 指向(x, y)的射线在坐标平面上与 x 轴正方向之间的角的角度
print(np.linalg.det([[1, 2], [3, 4]]))  # -2.0; 二维数组是参数
print(np.dot([1, 2], [3, 4]))  # 11; 两个一维数组
print(np.degrees(np.math.atan2(1, 0)))  # 90, (0, 1) 和 x 轴夹角
