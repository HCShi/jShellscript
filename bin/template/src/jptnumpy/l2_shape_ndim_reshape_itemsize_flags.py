#!/usr/bin/python3
# coding: utf-8
import numpy as np
##################################################################
# ndarray.shape; 这一数组属性返回一个包含数组维度的元组, 它也可以用于调整数组大小
a = np.array([[1, 2, 3], [4, 5, 6]]); print(a.shape, np.shape(a))  # (2, 3); 两种 shape 的方法
a = np.array([[1, 2, 3], [4, 5, 6]]); a.shape =  (3, 2); print(a)  # [[1, 2] [3, 4] [5, 6]]; 调整数组大小
a = np.array([[1,2,3],[4,5,6]]); print(a.reshape(3, 2))  # NumPy 也提供了 reshape 函数来调整数组大小
##################################################################
# ndarray.ndim; 这一数组属性返回数组的维数
a = np.arange(4); print(a, a.ndim)  # [0 1  2  3] 1; 等间隔数字的数组; 一维数组
b = np.arange(24).reshape(2, 4, 3); print(b)  # b 现在拥有三个维度
# [[[ 0,  1,  2]
#   [ 3,  4,  5]
#   [ 6,  7,  8]
#   [ 9, 10, 11]]
#   [[12, 13, 14]
#    [15, 16, 17]
#    [18, 19, 20]
#    [21, 22, 23]]]
##################################################################
# numpy.itemsize; 这一数组属性返回数组中每个元素的字节单位长度
x = np.array([1, 2, 3, 4, 5], dtype=np.int8); print(x.itemsize)  # 1; 数组的 dtype 为 int8(一个字节)
x = np.array([1, 2, 3, 4, 5], dtype=np.float32); print(x.itemsize)  # 4; 数组的 dtype 现在为 float32(四个字节)
##################################################################
# numpy.flags; ndarray 对象拥有以下属性
# C_CONTIGUOUS (C): 数组位于单一的、C 风格的连续区段内
# F_CONTIGUOUS (F): 数组位于单一的、Fortran 风格的连续区段内
# OWNDATA (O): 数组的内存从其它对象处借用
# WRITEABLE (W): 数据区域可写入.  将它设置为flase会锁定数据, 使其只读
# ALIGNED (A): 数据和任何元素会为硬件适当对齐
# UPDATEIFCOPY (U): 这个数组是另一数组的副本. 当这个数组释放时, 源数组会由这个数组中的元素更新
x = np.array([1, 2, 3, 4, 5]); print(x.flags)
# C_CONTIGUOUS: True
# F_CONTIGUOUS: True
# OWNDATA: True
# WRITEABLE: True
# ALIGNED: True
# UPDATEIFCOPY: False
