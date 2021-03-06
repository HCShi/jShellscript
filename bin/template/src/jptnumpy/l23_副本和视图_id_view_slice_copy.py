#!/usr/bin/python3
# coding: utf-8
# 在执行函数时, 其中一些返回输入数组的副本, 而另一些返回视图; 当内容物理存储在另一个位置时, 称为副本
# 另一方面, 如果提供了相同内存内容的不同视图, 我们将其称为视图
# 简单的赋值不会创建数组对象的副本, 相反, 它使用原始数组的相同 id() 来访问它; id() 返回 Python 对象的通用标识符, 类似于 C 中的指针
# 此外, 一个数组的任何变化都反映在另一个数组上; 例如, 一个数组的形状改变也会改变另一个数组的形状
import numpy as np
a = np.arange(6); print(a)  # [0 1 2 3 4 5]
print(id(a))  # 139747815479536
b = a; print(b)  # [0 1 2 3 4 5]
print(id(b))  # 139747815479536; b 拥有相同 id()
b.shape = 3, 2; print(b)  # [[0 1] [2 3] [4 5]]
print(a)  # [[0 1] [2 3] [4 5]]; a 的形状也修改了
##################################################################
# 视图或浅复制: NumPy 拥有 ndarray.view() 方法, 它是一个新的数组对象, 并可查看原始数组的相同数据
# 与前一种情况不同, 新数组的维数更改不会更改原始数据的维数
a = np.arange(6).reshape(3, 2); print(a)  # [[0 1] [2 3] [4 5]]
b = a.view(); print(b)  # [[0 1] [2 3] [4 5]]; 创建 a 的视图
print(id(a))  # 140424307227264
print(id(b))  # 140424151696288; 两个数组的 id() 不同
b.shape = 2, 3
print(b)  # [[0 1 2] [3 4 5]]
print(a)  # [[0 1] [2 3] [4 5]]; 修改 b 的形状, 并不会修改 a
##################################################################
# 数组的切片也会创建视图
a = np.array([[10, 10], [2, 3], [4, 5]]); print(a)  # [[10 10] [ 2 3] [ 4 5]]
s = a[:, :2]; print(s)  # [[10 10] [ 2 3] [ 4 5]]; 创建切片
##################################################################
# 深复制; ndarray.copy() 函数创建一个深层副本, 它是数组及其数据的完整副本, 不与原始数组共享
a = np.array([[10, 10], [2, 3], [4, 5]]); print(a)  # [[10 10] [ 2 3] [ 4 5]]
b = a.copy(); print(b)  # [[10 10] [ 2 3] [ 4 5]]; 创建 a 的深层副本; b 与 a 不共享任何内容
print(b is a)  # False; 我们能够写入 b 来写入 a 吗
print  '修改 b 的内容：'
b[0, 0] = 100; print(b)  # [[100 10] [ 2 3] [ 4 5]]
print(a)  # [[10 10] [ 2 3] [ 4 5]]; a 保持不变
