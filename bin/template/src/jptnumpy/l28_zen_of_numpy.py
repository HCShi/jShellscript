#!/usr/bin/python
# coding: utf-8
import numpy as np
x = np.arange(0, 10, 0.5); print(x)
mask = (5 < x) * (x < 7.5); print(mask)  # matirx with False and True)
print(x[mask])
indices = np.where(mask); print(indices)  # 使用 where 函数能将索引掩码转换成索引位置
A = np.array([[n + m * 10 for n in range(5)] for m in range(5)]); print(A)
##################################################################
## take 函数与高级索引（fancy indexing）用法相似 但是 take 也可以用在 list 和其它对象上
v2 = np.arange(-3, 3); print(v2)  # [-3 -2 -1  0  1  2]
row_indices = [1, 3, 5]
print(v2[row_indices])  # [-2  0  2]
print(v2.take(row_indices))  # [-2  0  2]
print(np.take([-3, -2, -1, 0, 1, 2], row_indices))  # [-2  0  2]
##################################################################
## choose 选取多个数组的部分组成新的数组
which = [1, 0, 1, 0]; choices = [[-2], [2], [-2], [2]]
print(np.choose(which, choices))  # [ 2 -2  2 -2]; choices 必须是多行的, which 会根据行来选择
##################################################################
## 标量运算
v1 = np.arange(0, 5)
print(v1 * 2)  # [0 2 4 6 8]
print(v1 + 2)  # [2 3 4 5 6]
print(A * 2, A + 2)
##################################################################
## Element-wise(逐项乘) 数组-数组 运算
print(A * A)  # 对应项相乘
print(v1 * v1)
print(A.shape, v1.shape)
print(A * v1)
##################################################################
## 矩阵代数
##################################################################
## 矩阵乘法, 两种方法
## 1.使用 dot 函数进行 矩阵－矩阵，矩阵－向量，数量积乘法
print(dot(A, A))  # 跟 A * A 不同
print(dot(A, v1))  # v1: 0, 1, 2, 3, 4
print(dot(v1, v1))  # 会自动转置
## 2.将数组对象映射到 matrix 类型
M = np.matrix(A)
v = np.matrix(v1).T  # make it a column vector, 转置
print(v)
print(M * M)
print(M * v)
print(v.T)
print(v.T * v)
print(v + M * v)
##################################################################
## 转置
v = np.matrix([1, 2, 3, 4, 5, 6])
print(shape(v), shape(v.T))
##################################################################
## 数组/矩阵 变换
C = np.matrix([[1j, 2j], [3j, 4j]])
print(C)
print(np.conjugate(C))  # 共轭矩阵
print(C.H)  # 共轭转置
##################################################################
## real 与 imag 能够分别得到复数的实部与虚部
print(np.real(C))
print(np.imag(C))
##################################################################
## angle 与 abs 可以分别得到幅角和绝对值
print(np.angle(C + 1))
print(np.abs(C))
##################################################################
## 矩阵计算
##################################################################
## 矩阵求逆
from scipy.linalg import *
print(inv(C))  # 等价于 C.I
print(C.I * C)
##################################################################
## 行列式
print(np.linalg.det(C))
print(np.linalg.det(C.I))
