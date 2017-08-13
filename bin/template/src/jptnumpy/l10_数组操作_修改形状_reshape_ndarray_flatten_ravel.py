#!/usr/bin/python3
# coding: utf-8
# NumPy 包中有几个例程用于处理 ndarray 对象中的元素; 它们可以分为以下类型:
import numpy as np
##################################################################
# 1. 修改形状
# reshape 不改变数据的条件下修改形状; flat 数组上的一维迭代器; flatten 返回折叠为一维的数组副本; ravel 返回连续的展开数组
##################################################################
# numpy.reshape(arr, newshape, order); 这个函数在不改变数据的条件下修改形状
# arr: 修改形状的数组; newshape: 整数或者整数数组, 新的形状应当兼容原有形状; order: 'C'为 C 风格, 'F'为 F 风格, 'A'为原顺序
a = np.arange(8); print(a)  # [0 1 2 3 4 5 6 7]
b = a.reshape(4, 2); print(b)  # [[0 1] [2 3] [4 5] [6 7]]
# 参数为 -1, 表示该维度未知, 总的兼容原始数据
z = np.array([[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]); print(z.shape)  # (3, 4)
print(z.reshape(-1), z.reshape(-1).shape)  # [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12], (12,); row 未知, 没有 column, 所以是向量
print(z.reshape(-1, 1), z.reshape(-1, 1).shape)  # (12, 1); row 未知, column 为 1
print(z.reshape(-1, 2), z.reshape(-1, 2).shape)  # (6, 2); row 未知, column 为 2, 所以 row 为 6
print(z.reshape(3, -1), z.reshape(3, -1).shape)  # (3, 4); column 是根据 row 算出来的
##################################################################
# numpy.ndarray.flat; 该函数返回数组上的一维迭代器, 行为类似 Python 内建的迭代器
a = np.arange(8).reshape(2, 4); print(a)  # [[0 1 2 3] [4 5 6 7]]
print(a.flat[6])  # 5; 返回展开数组中的下标的对应元素
##################################################################
# ndarray.flatten(order='C'); 返回折叠为一维的数组副本; order: 'C' 按行, 'F' 按列, 'A' 原顺序, 'k' 元素在内存中的出现顺序
a = np.arange(8).reshape(2, 4); print(a)  # [[0 1 2 3] [4 5 6 7]]
print(a.flatten())  # [0 1 2 3 4 5 6 7]; 展开的数组
print(a.flatten(order = 'F'))  # [0 4 1 5 2 6 3 7]; 以 F 风格顺序展开的数组
##################################################################
# numpy.ravel(a, order); 返回展开的一维数组, 并且按需生成副本; 返回的数组和输入数组拥有相同数据类型
a = np.arange(8).reshape(2, 4); print(a)  # [[0 1 2 3] [4 5 6 7]]
print(a.ravel())  # [0 1 2 3 4 5 6 7]; 调用 ravel 函数之后
print(a.ravel(order='F'))  # [0 4 1 5 2 6 3 7]; 以 F 风格顺序调用 ravel 函数之后
