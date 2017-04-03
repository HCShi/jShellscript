#!/usr/bin/python3
# coding: utf-8
##################################################################
# 2. 翻转操作
# transpose 翻转数组的维度; ndarray.T 和 self.transpose() 相同
# rollaxis 向后滚动指定的轴; swapaxes 互换数组的两个轴
##################################################################
# numpy.transpose(arr, axes); 翻转给定数组的维度; 如果可能的话它会返回一个视图
# arr: 要转置的数组; axes: 整数的列表, 对应维度, 通常所有维度都会翻转
a = np.arange(12).reshape(3, 4); print(a)  # [[ 0 1 2 3] [ 4 5 6 7] [ 8 9 10 11]]
print(np.transpose(a))  # [[ 0 4 8] [ 1 5 9] [ 2 6 10] [ 3 7 11]]; 转置数组
##################################################################
# numpy.ndarray.T; 该函数属于 ndarray 类, 行为类似于 numpy.transpose
a = np.arange(12).reshape(3, 4); print(a)  # [[ 0 1 2 3] [ 4 5 6 7] [ 8 9 10 11]]
print(a.T)  # [[ 0 4 8] [ 1 5 9] [ 2 6 10] [ 3 7 11]]; 转置数组
##################################################################
# numpy.rollaxis(arr, axis, start=0); 向后滚动特定的轴, 直到一个特定位置
# arr: 输入数组; axis: 要向后滚动的轴, 其它轴的相对位置不会改变; start: 默认为零, 表示完整的滚动, 会滚动到特定位置
a = np.arange(8).reshape(2, 2, 2); print(a)  # [[[0 1] [2 3]] [[4 5] [6 7]]]
print(np.rollaxis(a, 2))  # [[[0 2] [4 6]] [[1 3] [5 7]]]; 将轴 2 滚动到轴 0 (宽度到深度)
print(np.rollaxis(a, 2, 1))  # [[[0 2] [1 3]] [[4 6] [5 7]]]; 将轴 0 滚动到轴 1 (宽度到高度)
##################################################################
# numpy.swapaxes(arr, axis1, axis2); 交换数组的两个轴; 对于 NumPy v1.10, 返回交换后数组的试图
# arr: 要交换其轴的输入数组; axis1: 对应第一个轴的整数; axis2: 对应第二个轴的整数
a = np.arange(8).reshape(2, 2, 2); print(a)  # [[[0 1] [2 3]] [[4 5] [6 7]]]
print(np.swapaxes(a, 2, 0))  # [[[0 4] [2 6]] [[1 5] [3 7]]]; 现在交换轴 0 (深度方向) 到轴 2 (宽度方向)
