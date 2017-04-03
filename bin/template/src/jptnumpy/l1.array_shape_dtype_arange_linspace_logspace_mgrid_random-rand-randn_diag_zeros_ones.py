#!/usr/bin/python3
# coding: utf-8
# 参见 极客学院: Numpy - 多维数组（上）
import numpy as np
##################################################################
# array
##################################################################
print(np.array(np.array([1, 2])))  # 可以多层嵌套
v, m = np.array([1, 2, 3, 4]), np.array([[1, 2], [3, 4]], dtype=complex)  # 创建数组时定义类型, complex don't need quote, but uint8 below need quote !!!
print(np.shape(v), np.shape(m), v.shape, v.dtype)  # (4,) (2, 2) (4,) int64; shape: 矩阵大小; dtype: 数据类型
print(np.array([1, 2]) + np.array([3, 4]))  # [4 6]
##################################################################
# 向量
##################################################################
print(np.arange(0, 5, 1), np.arange(-1, 1, 0.4))  # [0 1 2 3 4]; [-1.  -0.6 -0.2  0.2  0.6], 第三个参数是步长
print(np.linspace(0, 10, 5))  # [  0.    2.5   5.    7.5  10. ], 第三个参数是个数, 自动选择步长
print(np.logspace(0, 10, 2, base=np.e))  # [  1.00000000e+00   2.20264658e+04], 不是很懂为什么第 2 个数是 2202.xx
##################################################################
# 矩阵
##################################################################
print("######")
print(np.mgrid[0:3, 0:3])  # two matrix, 一个横向, 一个纵向
print(np.diag([1, 2, 3]), '\n', np.diag([1, 1, 1]), '\n', np.diag([1, 2, 3], k = 1))  # 对角线是 1, 2, 3; 对角线是 1, 1, 1; 外层嵌套一层 0, 4 x 4
# zeros(shape, dtype=None, order='C'); shape 可以是三维的
print(np.zeros((3, 3)), '\n', np.zeros((2, 4, 3), dtype="uint8"))  # 构造全 0 矩阵, ** uint8 ** 对应灰度图像
canvas = np.zeros((2, 4, 3)); print(canvas.shape, (canvas.shape[1] / 2, canvas.shape[0] / 2))  # (2, 4, 3) (2.0, 1.0) the last truple is the center of canvas
print(np.ones((3, 3)))    # matrix with all 1
##################################################################
# random
##################################################################
print(np.random.rand(3, 3))  # Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1)
print(np.random.randn(3, 3))  # A (d0, d1, ..., dn)-shaped array of floating-point samples from the standard normal distribution
# randint(low, high=None, size=None, dtype='l'); size output shape
print(np.random.randint(5), np.random.randint(5, 200))  # 生成 1 个 [0, 5) 和 [5, 200) 的随机数
print(np.random.randint(0, high=256, size=(3,)).tolist())  # 生成 3 个 [0, 256) 的随机数, tolist() 不是很懂, argument is not numeric 时候用很管用
