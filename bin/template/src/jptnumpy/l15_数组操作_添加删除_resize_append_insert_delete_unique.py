#!/usr/bin/python3
# coding: utf-8
##################################################################
# 6. 添加/删除元素
# resize 返回指定形状的新数组; append 将值添加到数组末尾; insert 沿指定轴将值插入到指定下标之前
# delete 返回删掉某个轴的子数组的新数组; unique 寻找数组内的唯一元素
##################################################################
# numpy.resize(arr, shape); 返回指定大小的新数组; 如果新大小大于原始大小, 则包含原始数组中的元素的重复副本
# arr: 要修改大小的输入数组; shape: 返回数组的新形状
a = np.array([[1, 2, 3], [4, 5, 6]]); print(a, a.shape)  # [[1 2 3] [4 5 6]] (2, 3)
b = np.resize(a, (3, 2)); print(b, b.shape)  # [[1 2] [3 4] [5 6]] (3, 2)
b = np.resize(a, (3, 3)); print(b)  # [[1 2 3] [4 5 6] [1 2 3]]; 要注意 a 的第一行在 b 中重复出现, 因为尺寸变大了
##################################################################
# numpy.append(arr, values, axis); 在输入数组的末尾添加值; 附加操作不是原地的, 而是分配新的数组; 此外, 输入数组的维度必须匹配否则将生成 ValueError
# arr: 输入数组; values: 要向 arr 添加的值, 比如和 arr 形状相同 (除了要添加的轴)
# axis: 沿着它完成操作的轴; 如果没有提供, 两个参数都会被展开
a = np.array([[1, 2, 3], [4, 5, 6]]); print(a)  # [[1 2 3] [4 5 6]]
print(np.append(a, [7, 8, 9]))  # [1 2 3 4 5 6 7 8 9]
print(np.append(a, [[7, 8, 9]], axis=0))  # [[1 2 3] [4 5 6] [7 8 9]]  # 沿轴 0 添加元素
print(np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1))  # [[1 2 3 5 5 5] [4 5 6 7 8 9]]; 沿轴 1 添加元素
##################################################################
# numpy.insert(arr, obj, values, axis); 在给定索引之前, 沿给定轴在输入数组中插入值; 如果值的类型转换为要插入, 则它与输入数组不同
# 插入没有原地的, 函数会返回一个新数组; 此外, 如果未提供轴, 则输入数组会被展开
# arr: 输入数组; obj: 在其之前插入值的索引; values: 要插入的值; axis: 沿着它插入的轴, 如果未提供, 则输入数组会被展开
a = np.array([[1, 2], [3, 4], [5, 6]]); print(a)  # [[1 2] [3 4] [5 6]]
print(np.insert(a, 3, [11, 12]))  # [ 1  2  3 11 12  4  5  6]; 未传递 Axis 参数, 在插入之前输入数组会被展开
# 传递了 Axis 参数, 会广播值数组来配输入数组
print(np.insert(a, 1, [11], axis=0))  # [[ 1  2] [11 11] [ 3  4] [ 5  6]]; 沿轴 0 广播
print(np.insert(a, 1, 11, axis=1))  # [[ 1 11  2] [ 3 11  4] [ 5 11  6]]; 沿轴 1 广播
##################################################################
# Numpy.delete(arr, obj, axis); 返回从输入数组中删除指定子数组的新数组; 与 insert() 函数的情况一样, 如果未提供轴参数, 则输入数组将展开
# arr: 输入数组; obj: 可以被切片, 整数或者整数数组, 表明要从输入数组删除的子数组; axis: 沿着它删除给定子数组的轴, 如果未提供, 则输入数组会被展开
a = np.arange(12).reshape(3, 4); print(a)  # [[ 0 1 2 3] [ 4 5 6 7] [ 8 9 10 11]]
print(np.delete(a, 5))  # [ 0 1 2 3 4 6 7 8 9 10 11]; 未传递 Axis 参数, 在插入之前输入数组会被展开
print(np.delete(a, 1, axis=1))  # [[ 0 2 3] [ 4 6 7] [ 8 10 11]]; 删除第二列
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.delete(a, np.s_[::2]))  # [ 2 4 6 8 10]; 包含从数组中删除的替代值的切片
##################################################################
# numpy.unique(arr, return_index, return_inverse, return_counts); 返回输入数组中的去重元素数组
# 该函数能够返回一个元组, 包含去重数组和相关索引的数组; 索引的性质取决于函数调用中返回参数的类型
# arr: 输入数组, 如果不是一维数组则会展开; return_index: 如果为 true, 返回输入数组中的元素下标
# return_inverse: 如果为 true, 返回去重数组的下标, 它可以用于重构输入数组
# return_counts: 如果为 true, 返回去重数组中的元素在原数组中的出现次数
a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9]); print(a)  # [5 2 6 2 7 5 6 8 2 9]
u = np.unique(a); print(u)  # [2 5 6 7 8 9]; 第一个数组的去重值
u, indices = np.unique(a, return_index=True); print(indices)  # [1 0 2 4 7 9]; 去重数组的索引数组
u, indices = np.unique(a, return_inverse=True); print(indices)  # [1 0 2 0 3 1 2 4 0 5]; 下标
print(u[indices])  # [5 2 6 2 7 5 6 8 2 9]; 使用下标重构原数组
u, indices = np.unique(a, return_counts=True); print(u, indices)  # [2 5 6 7 8 9] [3 2 2 1 1 1]; 返回唯一元素的重复数量
