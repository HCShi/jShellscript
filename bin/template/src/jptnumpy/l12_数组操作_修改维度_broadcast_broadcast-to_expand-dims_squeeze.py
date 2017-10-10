#!/usr/bin/python3
# coding: utf-8
import numpy as np
##################################################################
# 3. 修改维度
# broadcast 产生模仿广播的对象; broadcast_to 将数组广播到新形状; expand_dims 扩展数组的形状; squeeze 从数组的形状中删除单维条目
##################################################################
# broadcast(arr1, arr2); 此功能模仿广播机制; 它返回一个对象, 该对象封装了将一个数组广播到另一个数组的结果, 该函数使用两个数组作为输入参数
# 这部分在 Python3 中不太好用
x = np.array([[1], [2], [3]]); y = np.array([4, 5, 6])
b = np.broadcast(x, y)  # 对 y 广播 x
r, c = b.iters  # 它拥有 iterator 属性, 基于自身组件的迭代器元组, 在 Python3 中已经没有了 !!!
print(r.next(), c.next())  # 1 4
print(r.next(), c.next())  # 1 5; 这两个在 Python3 中会报错
print(b.shape)  # (3, 3); shape 属性返回广播对象的形状
b = np.broadcast(x, y)  # 手动使用 broadcast 将 x 与 y 相加
c = np.empty(b.shape)
print(c.shape)  # (3, 3); 手动使用 broadcast 将 x 与 y 相加
c.flat = [u + v for (u,v) in b]
print(c)  # [[ 5. 6. 7.] [ 6. 7. 8.] [ 7. 8. 9.]]; 调用 flat 函数
print(x + y)  # [[5 6 7] [6 7 8] [7 8 9]]; x 与 y 的和, 获得了和 NumPy 内建的广播支持相同的结果
##################################################################
# numpy.broadcast_to(array, shape, subok); 将数组广播到新形状; 它在原始数组上返回只读视图; 它通常不连续;
# 如果新形状不符合 NumPy 的广播规则, 该函数可能会抛出 ValueError; 注意 - 此功能可用于 1.10.0 及以后的版本
a = np.arange(4).reshape(1, 4); print(a)  # [[0 1 2 3]]
print(np.broadcast_to(a,(4,4)))  # [[0  1  2  3] [0  1  2  3] [0  1  2  3] [0  1  2  3]]
##################################################################
# numpy.expand_dims(arr, axis); 函数通过在指定位置插入新的轴来扩展数组形状
# arr: 输入数组; axis: 新轴插入的位置
x = np.array(([1, 2], [3, 4])); print(x)  # [[1 2] [3 4]]
y = np.expand_dims(x, axis=0); print(y)  # [[[1 2] [3 4]]]
print(x.shape, y.shape)  # (2, 2) (1, 2, 2); 数组 x 和 y 的形状
# 在位置 1 插入轴
y = np.expand_dims(x, axis=1); print(y)  # [[[1 2]] [[3 4]]]; 在位置 1 插入轴之后的数组 y
print(x.ndim, y.ndim)  # 2 3
print(x.shape, y.shape)  # (2, 2) (2, 1, 2)
##################################################################
# numpy.squeeze(arr, axis); 函数从给定数组的形状中删除一维条目
# arr: 输入数组; axis: 整数或整数元组, 用于选择形状中单一维度条目的子集
x = np.arange(9).reshape(1, 3, 3); print(x)  # [[[0 1 2] [3 4 5] [6 7 8]]]
y = np.squeeze(x); print(y)  # [[0 1 2] [3 4 5] [6 7 8]]
print(x.shape, y.shape)  # (1, 3, 3) (3, 3)
