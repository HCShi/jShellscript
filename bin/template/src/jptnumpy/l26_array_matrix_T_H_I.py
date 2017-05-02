#!/usr/bin/python3
# coding: utf-8
# Numpy matrices 必须是 2 维的, 但是 numpy arrays (ndarrays) 可以是多维, Matrix 是 Array 的一个小的分支, 包含于 Array, 所以 matrix 拥有 array 的所有特性
##################################################################
# 1. 相对简单的乘法运算符号, 例如, a 和 b 是两个 matrices, 那么 a*b, 就是矩阵积
# array 运算得到的是 a.*b, 点积, 逐个元素运算
import numpy as np
a = np.mat('4 3; 2 1'); b = np.mat('1 2; 3 4')
print(a, b)  # [[4 3] [2 1]], [[1 2] [3 4]]
print(a * b)  # [[13 20] [ 5  8]]; np.dot(a, b); [[4*1 + 3*3, 4*2 + 3*4], [2*1 + 1*3, 2*2 + 1*4]]
print(np.array(a) * np.array(b))  # [[4 6] [6 4]]; [[4*1, 3*2], [2*3, 1*4]]
print(np.dot(np.array(a), np.array(b)))  # [[13 20] [ 5  8]]
##################################################################
# 2. matrix 和 array 都可以通过 objects 后面加 .T 得到其转置; matrix 后面加 .H 得到共轭矩阵, 加 .I 得到逆矩阵
print(a.T, a.H, a.I)
# print(np.array([[1, 2], [3, 4]]).I)  # 会报错
##################################################################
# 3. 运算符的作用也不一样
print(a**2)  # [[22 15] [10  7]]; 矩阵相乘
print(np.array(a)**2)  # [[16  9] [ 4  1]]; 逐个元素求平方
##################################################################
# 4. 问题就出来了, 如果一个程序里面既有 matrix 又有 array, 会让人脑袋大
# 但是如果只用 array, 你不仅可以实现 matrix 所有的功能, 还减少了编程和阅读的麻烦
# 当然你可以通过下面的两条命令轻松的实现两者之间的转换: np.asmatrix 和 np.asarray
##################################################################
# 5. numpy 中的 array 与 numpy 中的 matrix, matlab 中的 matrix 的最大的不同是
# 在做归约运算时, array 的维数会发生变化, 但 matrix总是保持为 2 维, 例如下面求平均值的运算
m = np.mat([[1, 2], [2, 3]]); print(m)  # matrix([[1, 2], [2, 3]]); 在交互式环境中会显示 matrix()
mm = m.mean(1); print(mm)  # matrix([[ 1.5], [ 2.5]])
print(mm.shape)  # (2, 1)
print(m - mm)  # matrix([[-0.5,  0.5], [-0.5,  0.5]])
a = np.array([[1,2],[2,3]]); print(a)  # array([[1, 2], [2, 3]])
am = a.mean(1)
print(am.shape)  # (2,)
print(am)  # array([ 1.5,  2.5])
print(a - am)  # array([[-0.5, -0.5], [ 0.5,  0.5]]); wrong
print(a - am[:, np.newaxis])  # array([[-0.5,  0.5], [-0.5,  0.5]]); right
