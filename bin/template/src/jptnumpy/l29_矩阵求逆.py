#!/usr/bin/python3
# coding: utf-8
import numpy as np
a = np.eye(3); print(a)  # eye 生成单位矩阵, 是 ndarry 类型的
print(np.mat(a).I)  # 用 np.mat 将 ndarry 转换为 matrix, 并且求逆
print(np.linalg.inv(Mat))  # 另一种求逆的方法
