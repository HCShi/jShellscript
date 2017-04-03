#!/usr/bin/python3
# coding: utf-8
from numpy import *
##################################################################
# 数组属性
M = random.rand(3,3)
print(M.itemsize)  # 8 每一个元素的字节数
print(M.nbytes)  # 72 总共的bytes
print(M.ndim)  # 2 维度
##################################################################
# 索引
print("######")
print(M[1, 1])  # 1.0
print(M[1])  # 1 x 3, 2th row
M[1, 1] = 1
M = diag([1, 1, 1])
print(M[1, :])  # 2th row
print(M[:, 1])  # 2th column
M[1, :] = 0
M[:, 2] = -1
print(M)
##################################################################
# 切片索引
A = array([1, 2, 3, 4, 5])
print(A)
print(A[1:3])  # 2, 3 左闭右开
A[1: 3] = [-2, -3]
print(A)
print(A[::])
print(A[::2])
print(A[:3])
print(A[3:])
print(A[-1])  # 从尾部开始, 5
print(A[-3:])  # -3, 4, 5
##################################################################
# 多维数组切片
A = array([[n + m * 10 for n in range(5)] for m in range(5)])
print(A)
print(A[1:4, 1:4])
print(A[::2, ::2])

##################################################################
print("# 高级索引")
##################################################################
row_indices = [1, 2, 3]
print(A[row_indices])
col_indices = [1, 2, -1] # remember, index -1 means the last element
print(A[row_indices, col_indices])

##################################################################
print("# 索引掩码")
##################################################################
B = array([n for n in range(5)])
print(B)
row_mask = array([True, False, True, False, False])
print(B[row_mask])
row_mask = array([1,0,1,0,0], dtype=bool)
print(B[row_mask])

##################################################################
print("# 比较操作符生成掩码")
##################################################################
x = arange(0, 10, 0.5)
print(x)
mask = (5 < x) * (x < 7.5)
print(mask)
print(x[mask])
