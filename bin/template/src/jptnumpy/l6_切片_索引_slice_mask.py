#!/usr/bin/python3
# coding: utf-8
# 三种可用的索引方法类型: 字段访问, 基本切片 和 高级索引
import numpy as np
##################################################################
# slice(start, stop, step); 将 start, stop 和 step 参数提供给内置的 slice 函数来构造一个 Python slice 对象
a = np.arange(10); s = slice(2, 7, 2); print(a[s])  # [2  4  6]; 切片对象传递 ndarray, 对它的进行切片, 从索引 2 到 7, 步长为 2
a = np.arange(10); b = a[2:7:2]; print(b)  # [2  4  6]; 由冒号分隔的切片参数(start:stop:step)直接提供给 ndarray 对象, 也可以获得相同的结果
a = np.arange(10); b = a[5]; print(b)  # 5; 只输入一个参数, 返回与索引对应的单个项目
a = np.arange(10); print(a[2:])  # [2  3  4  5  6  7  8  9]; 如果使用 a:, 则从该索引向后的所有项目将被提取
a = np.arange(10); print(a[2:5])  # [2  3  4]; 如果使用两个参数(以 : 分隔), 则对两个索引(不包括停止索引)之间的元素以默认步骤进行切片
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]]); print(a[1:])  # [[3 4 5] [4 5 6]]; 多维数组切片

# 反转
a = np.arange(10); print(a[::-1])  # [9 8 7 6 5 4 3 2 1 0]
a = np.arange(8).reshape(2, 2, 2); print(a[::-1])  # [[[4 5] [6 7]] [[0 1] [2 3]]]; depth 翻转, h, w 不变
a = np.arange(8).reshape(2, 2, 2); print(a[:, ::-1])  # [[[2 3] [0 1]] [[6 7] [4 5]]]; d 不变, height 翻转, w 不变
a = np.arange(8).reshape(2, 2, 2); print(a[:, :, ::-1])  # [[[1 0] [3 2]] [[5 4] [7 6]]]; d, h 不变, width 翻转
# 用两只手各个方向摆放, 然后不用转动, 直接交换位置来模拟
# [depth, height, width] 是默认的顺序, a[0] 表示是第一张二维图, a[1, 1] 表示第二张二维图的第二行
plt.subplot(223).imshow(img[:, :, ::-1])  # BGR-RGB, 速度更快; 图像 读入/显示 一般按照 [height, width, depth] 的顺序来进行

# 切片还可以包括省略号 (...), 来使选择元组的长度与数组的维度相同. 如果在行位置使用省略号, 它将返回包含行中元素的 ndarray
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a[..., 1])  # [2 4 5]; 第二列元素
print(a[1, ...])  # [3 4 5]; 第二行元素
print(a[..., 1:])  # 第二列及其剩余元素; [[2 3] [4 5] [5 6]]
##################################################################
x = np.arange(0, 10, 0.5);
mask = (5 < x) * (x < 7.5); print(mask)  # matirx with False and True
print(x[mask])
