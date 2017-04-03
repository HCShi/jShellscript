#!/usr/bin/python3
# coding: utf-8
import numpy as np
def angle(p0, p1=np.array([0, 0]), p2=None):
    '''compute angle (in degrees) for p0p1p2 corner. Inputs: p0, p1, p2 - points in the form of [x, y] or (x, y)
1. 输入一个点表示该点与原点连线和 x 轴角度 2. 输入两个参数表示两点连线与 x 轴夹角 3. 输入三点就是求 p0p1p2 夹角 '''
    if p2 is None:
        p2 = p1 + np.array([1, 0])
    v0, v1 = np.array(p0) - np.array(p1), np.array(p2) - np.array(p1)  # Vector: p1 -> p0, p1 -> p2
    angle = np.math.atan2(np.linalg.det([v0, v1]), np.dot(v0, v1))
    return np.degrees(angle)
print(angle((1, 1)), angle((1, 1), (0, 0)), angle((1, 1), (0, 0), (1, 0)))
