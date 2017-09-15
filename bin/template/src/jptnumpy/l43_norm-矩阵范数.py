#!/usr/bin/python3
# coding: utf-8
import numpy as np
import numpy.linalg as la
a=np.array([[complex(1, -1), 3], [2, complex(1, 1)]]); print(a)
print(la.norm(a, ord=2) )         # 计算矩阵 2 的范数
print(la.linalg.norm(a, ord=1) )  # 计算矩阵 1 的范数
print(la.norm(a, ord=np.inf) )    # 矩阵无穷的范数
