#!/usr/bin/python3
# coding: utf-8
# 来自现有数据创建
import numpy as np
##################################################################
# numpy.asarray(a, dtype=None, order=None)  # 此函数类似于 numpy.array, 除了它有较少的参数
# a 任意形式的输入参数, 比如列表、列表的元组、元组、元组的元组、元组的列表
# dtype 数据的类型; order 'C'为按行的 C 风格数组, 'F'为按列的 Fortran 风格数组
# 将列表转换为 ndarray
x = [1, 2, 3]; a = np.asarray(x); print(a)  # [1 2 3]
x = [1, 2, 3]; a = np.asarray(x, dtype=float); print(a)  # [1. 2. 3.]
x = (1, 2, 3); a = np.asarray(x); print(a)  # [1 2 3]
x = [(1, 2, 3), (4, 5)]; a = np.asarray(x); print(a)  # [(1, 2, 3) (4, 5)]
##################################################################
# numpy.frombuffer(buffer, dtype=float, count=-1, offset=0); 此函数将缓冲区解释为一维数组, 暴露缓冲区接口的任何对象都用作参数来返回 ndarray
# buffer 任何暴露缓冲区借口的对象; dtype 返回数组的数据类型, 默认为 float;
# count 需要读取的数据数量, 默认为-1, 读取所有数据; offset 需要读取的起始位置, 默认为0
s = 'Hello World'; a = np.frombuffer(s, dtype='S1'); print(a)  # 'str' object has no attribute '__buffer__'
# ['H'  'e'  'l'  'l'  'o'  ' '  'W'  'o'  'r'  'l'  'd']
##################################################################
# numpy.fromiter(iterable, dtype, count=-1); 此函数从任何可迭代对象构建一个 ndarray 对象, 返回一个新的一维数组
# iterable 任何可迭代对象; dtype 返回数组的数据类型; count 需要读取的数据数量, 默认为-1, 读取所有数据
list = range(5)  # [0,  1,  2,  3,  4]; 使用 range 函数创建列表对象
it = iter(list)  # 从列表中获得迭代器
x = np.fromiter(it, dtype =  float); print(x)  # [0.   1.   2.   3.   4.]; 使用迭代器创建 ndarray
