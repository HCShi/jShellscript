#!/usr/bin/python3
# coding: utf-8
# load() 和 save() 函数处理 numPy 二进制文件 (带 npy 扩展名); loadtxt() 和 savetxt() 函数处理正常的文本文件
# NumPy 为 ndarray 对象引入了一个简单的文件格式
# 这个 npy 文件在磁盘文件中, 存储重建 ndarray 所需的数据、图形、dtype 和其他信息, 以便正确获取数组, 即使该文件在具有不同架构的另一台机器上
# numpy.save() 文件将输入数组存储在具有 npy 扩展名的磁盘文件中
import numpy as np
a = np.array([1, 2, 3, 4, 5])
np.save('tmp', a)  # 为了从 outfile.npy 重建数组, 请使用 load() 函数, vim 打开是乱码
b = np.load('tmp.npy'); print(b)  # array([1, 2, 3, 4, 5])
# save() 和 load() 函数接受一个附加的布尔参数 allow_pickles
# Python 中的 pickle 用于在保存到磁盘文件或从磁盘文件读取之前, 对对象进行序列化和反序列化
##################################################################
# savetxt(); 以简单文本文件格式存储和获取数组数据, 是通过 savetxt() 和 loadtx() 函数完成的
# savetxt() 和 loadtxt() 数接受附加的可选参数, 例如页首, 页尾和分隔符
a = np.array([1, 2, 3, 4, 5])
np.savetxt('tmp.txt', a)  # vim 打开是科学计数法表示的
b = np.loadtxt('tmp.txt'); print(b)  # [ 1.  2.  3.  4.  5.]
