#!/usr/bin/python3
# coding: utf-8
import numpy as np
##################################################################
# numpy.empty(shape, dtype=float, order='C'); 它创建指定形状和 dtype 的未初始化数组
# Shape 空数组的形状, 整数或整数元组; Dtype 所需的输出数组类型, 可选; Order 'C'为按行的 C 风格数组, 'F'为按列的 Fortran 风格数组
x = np.empty([3, 2], dtype=int); print(x)  # [[22649312 1701344351] [1818321759 1885959276] [16779776 156368896]]; 数组元素为随机值, 因为它们未初始化
##################################################################
# numpy.zeros(shape, dtype=float, order='C'); 返回特定大小, 以 0 填充的新数组
x = np.zeros(5); print(x)  # [ 0. 0. 0. 0. 0.]
x = np.zeros((5,), dtype=np.int); print(x)  # [0  0  0  0  0]
x = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')]); print(x)  # [[(0,0)(0,0)] [(0,0)(0,0)]]; 自定义类型
##################################################################
# numpy.ones(shape, dtype=None, order='C')  # 返回特定大小, 以 1 填充的新数组
x = np.ones(5); print(x)  # [ 1.  1.  1.  1.  1.]
x = np.ones([2, 2], dtype=int); print(x)  # [[1  1] [1  1]]
