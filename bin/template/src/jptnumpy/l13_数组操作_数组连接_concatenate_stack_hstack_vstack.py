#!/usr/bin/python3
# coding: utf-8
import numpy as np
##################################################################
# 4. 数组的连接
# concatenate 沿着现存的轴连接数据序列; stack 沿着新轴连接数组序列
# hstack 水平堆叠序列中的数组 (列方向); vstack 竖直堆叠序列中的数组 (行方向)
a = np.array([[1, 2], [3, 4]]); print(a)  # [[1 2] [3 4]]
b = np.array([[5, 6], [7, 8]]); print(b)  # [[5 6] [7 8]]
##################################################################
# numpy.concatenate((a1, a2, ...), axis=0); 数组的连接是指连接; 用于沿指定轴连接相同形状的两个或多个数组
# a1, a2, ...: 相同类型的数组序列; axis: 沿着它连接数组的轴, 默认为 0
print(np.concatenate((a, b)))  # [[1 2] [3 4] [5 6] [7 8]]; 沿轴 0 连接两个数组
print(np.concatenate((a, b), axis=1))  # [[1 2 5 6] [3 4 7 8]]; 沿轴 1 连接两个数组
##################################################################
# numpy.stack(arrays, axis); 沿新轴连接数组序列; 此功能添加自 NumPy 版本 1.10.0; 需要提供以下参数
# arrays: 相同形状的数组序列; axis: 返回数组中的轴, 输入数组沿着它来堆叠
print(np.stack((a, b), 0))  # [[[1 2] [3 4]] [[5 6] [7 8]]]; 沿轴 0 堆叠两个数组
print(np.stack((a, b), 1))  # [[[1 2] [5 6]] [[3 4] [7 8]]]; 沿轴 1 堆叠两个数组
##################################################################
# numpy.hstack; numpy.stack 函数的变体, 通过堆叠来生成水平的单个数组
print(np.hstack((a, b)))  # [[1 2 5 6] [3 4 7 8]]; 水平堆叠
print(np.hstack(b))  # [5 6 7 8]; 本身的横向合并
print(np.hstack(b.T))  # [5 7 6 8]
c = np.array([[1, 2], [2, 3], 3]); print(c, c.shape)  # [[1, 2] [2, 3] 3] (3,)
print(np.hstack(c), np.hstack(c).shape)  # [1 2 2 3 3] (5,); 原来省略是这个意思啊
# print(np.unique(c))  # '>' not supported between instances of 'int' and 'list'; 讲道理应该是可以的
print(np.unique(np.hstack(c)))  # [1 2 3]; 记得在 keras 中 imdb 的数据没有 hstack() 也可以求 unique(); 迷...
##################################################################
# numpy.vstack; numpy.stack 函数的变体, 通过堆叠来生成竖直的单个数组
print(np.vstack((a, b)))  # [[1 2] [3 4] [5 6] [7 8]]; 竖直堆叠
print(np.vstack(b))  # [[5 6] [7 8]]
##################################################################
## np.array; 增加维度
# concatenate vstack hstack 等方法并不能修改数组本身的维度
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.array([a, b])[0])
