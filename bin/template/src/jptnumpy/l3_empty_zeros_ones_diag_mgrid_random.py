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
# shape 可以是三维的
print(np.zeros((2, 4, 3), dtype="uint8"))  # 构造全 0 矩阵, ** uint8 ** 对应灰度图像
canvas = np.zeros((2, 4, 3)); print(canvas.shape, (canvas.shape[1] / 2, canvas.shape[0] / 2))  # (2, 4, 3) (2.0, 1.0) the last truple is the center of canvas
##################################################################
# numpy.ones(shape, dtype=None, order='C')  # 返回特定大小, 以 1 填充的新数组
x = np.ones(5); print(x)  # [ 1.  1.  1.  1.  1.]
x = np.ones([2, 2], dtype=int); print(x)  # [[1  1] [1  1]]
##################################################################
# mgrid
print(np.mgrid[0:3, 0:3])  # two matrix, 一个横向, 一个纵向
##################################################################
# diag, 参数是一维数组是, 生成矩阵; 参数是矩阵时, 提取对角线
print(np.diag([1, 2, 3]), '\n', np.diag([1, 1, 1]), '\n', np.diag([1, 2, 3], k = 1))  # 对角线是 1, 2, 3; 对角线是 1, 1, 1; 外层嵌套一层 0, 4 x 4
A = np.array([[n + m * 10 for n in range(5)] for m in range(5)])
print(A)  # [[ 0  1  2  3  4] [10 11 12 13 14] [20 21 22 23 24] [30 31 32 33 34] [40 41 42 43 44]]
print(np.diag(A))  # [ 0 11 22 33 44]; 使用 diag 函数能够提取出数组的对角线
print(np.diag(A, -1))  # [10 21 32 43]; 对角线下面的一条斜线
##################################################################
# random 和 python 标准库中的 random 用法类似, 但是更快
print(np.random.rand(3, 3))  # Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1)
print(np.random.randn())  # 返回一个正态分布(高斯分布) 的数据
print(np.random.randn(3, 3))  # A (d0, d1, ..., dn)-shaped array of floating-point samples from the standard normal distribution
# randint(low, high=None, size=None, dtype='l'); size output shape
print(np.random.randint(5), np.random.randint(5, 200))  # 生成 1 个 [0, 5) 和 [5, 200) 的随机数
print(np.random.randint(0, high=256, size=(3,)).tolist())  # 生成 3 个 [0, 256) 的随机数, tolist() 不是很懂, argument is not numeric 时候用很管用

print(np.random.random((10, 10)))
print(np.random.random(3))  # 指定维数快速生成随机数
##################################################################
## 函数总结
rand(d0, d1, ..., dn)               # Random values in a given shape.
randn(d0, d1, ..., dn)              # Return a sample (or samples) from the “standard normal” distribution.
randint(low[, high, size, dtype])	# Return random integers from low (inclusive) to high (exclusive).
random_integers(low[, high, size])	# Random integers of type np.int between low and high, inclusive.
random_sample([size])               # Return random floats in the half-open interval [0.0, 1.0).
random([size])                      # Return random floats in the half-open interval [0.0, 1.0). 产生随机矩阵, 如 random.random([2,3]) 产生一个 2x3 维的随机数
ranf([size])                        # Return random floats in the half-open interval [0.0, 1.0).
sample([size])                      # Return random floats in the half-open interval [0.0, 1.0).
choice(a[, size, replace, p])       # Generates a random sample from a given 1-D array
bytes(length)                       # Return random bytes.
