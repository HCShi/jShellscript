#!/usr/bin/python3
# coding: utf-8
import numpy as np
##################################################################
## numpy.apply_along_axis(func1d, axis, arr, *args, **kwargs)
a = np.array([[1., 2, 3], [4, 5, 6], [7, 8, 9]]); print(a)
print(np.apply_along_axis(lambda x: x + 1, 0, a))  # 不会写回去
print(np.apply_along_axis(lambda x: x + 1, 0, a[1]))  # [ 5.  6.  7.]; 这里不能 axis=1, 因为要按行
print(np.apply_along_axis(int, 0, a[1]))  # TypeError: only length-1 arrays can be converted to Python scalars; 竟然会错
print(np.apply_along_axis(lambda x: int(x), 0, a[1]))  # 还是上面的错误

##################################################################
## astype 可以实现一些操作
print(a[:, -1].astype(int))  # [3 6 9]
