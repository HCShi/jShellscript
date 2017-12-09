#!/usr/bin/python3
# coding: utf-8
# 种类	                   速度  最坏情况	工作空间	稳定性
# 'quicksort' (快速排序)     1   O(n^2)	       0         否
# 'mergesort' (归并排序)     2   O(n*log(n))   ~n/2	     是
# 'heapsort'  (堆排序)       3   O(n*log(n))    0         否
import numpy as np
##################################################################
## numpy.sort(a, axis, kind, order); 返回输入数组的排序副本
# a 要排序的数组; axis 沿着它排序数组的轴, 如果没有数组会被展开, 沿着最后的轴排序; kind 默认为'quicksort'
# order 如果数组包含字段, 则是要排序的字段
a = np.array([[3, 7], [9, 1]]); print(a)  # [[3 7] [9 1]]
print(np.sort(a))  # [[3 7] [1 9]]
print(np.sort(a, axis=0))  # [[3 1] [9 7]]; 沿轴 0 排序
# 在 sort 函数中排序字段
dt = np.dtype([('name', 'S10'), ('age', int)])
a = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt); print(a)  # [('raju', 21) ('anil', 25) ('ravi', 17) ('amar', 27)]
print(np.sort(a, order='name'))  # [('amar', 27) ('anil', 25) ('raju', 21) ('ravi', 17)]; 按 name 排序
##################################################################
## numpy.argsort(a, axis=-1, kind='quicksort', order=None);
## 对输入数组沿给定轴执行间接排序, 并使用指定排序类型返回数据的索引数组, 这个索引数组用于构造排序后的数组
x = np.array([3, 1, 2]); print(x)  # [3 1 2]
y = np.argsort(x); print(y)  # [1 2 0]
print(x[y])  # [1 2 3]
for i in y: print(x[i],)  # 1 2 3
##################################################################
## numpy.lexsort(keys, axis=-1); 使用键序列执行间接排序; 键可以看作是电子表格中的一列, 该函数返回一个索引数组, 使用它可以获得排序数据
# 注意, 最后一个键恰好是 sort 的主键
nm = ('raju', 'anil', 'ravi', 'amar')
dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
ind = np.lexsort((dv, nm)); print(ind)  # [3 1 0 2]
print([nm[i]  +  ", "  + dv[i]  for i in ind])  # ['amar, f.y.', 'anil, s.y.', 'raju, f.y.', 'ravi, s.y.'];  使用这个索引来获取排序后的数据
##################################################################
## NumPy 模块有一些用于在数组内搜索的函数, 提供了用于找到最大值, 最小值以及满足给定条件的元素的函数
## numpy.argmax(a, axis=None, out=None) 和 numpy.argmin(a, axis=None, out=None); 这两个函数分别沿给定轴返回最大和最小元素的索引
a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]]); print(a)  # [[30 40 70] [80 20 10] [50 90 60]]
print(np.argmax(a))  # 7
print(a.flatten())  # [30 40 70 80 20 10 50 90 60]
maxindex = np.argmax(a, axis=0); print(maxindex)  # [1 2 0]; 沿轴 0 的最大值索引, 以列为单位, axis=0 一般都是和 pandas 中的数据一样
maxindex = np.argmax(a, axis=1); print(maxindex)  # [2 0 1]; 沿轴 1 的最大值索引, 以行为单位
minindex = np.argmin(a); print(minindex)  # 5
print(a.flatten()[minindex])  # 10; 展开数组中的最小值
minindex = np.argmin(a, axis=0); print(minindex)  # [0 1 1]; 沿轴 0 的最小值索引
minindex = np.argmin(a, axis=1); print(minindex)  # [0 2 0]; 沿轴 1 的最小值索引：
##################################################################
## numpy.nonzero(a); 函数返回输入数组中非零元素的索引
a = np.array([1, 0, 1, 0]); print(np.nonzero(a))  # (array([0, 2]),); 一维数组直接就是索引
a = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]]); print(a)  # [[30 40 0] [ 0 20 10] [50 0 60]]
print(np.nonzero(a))  # (array([0, 0, 1, 1, 2, 2]), array([0, 1, 1, 2, 0, 2]))
# 二维数组
a = np.array([[1, 0, 1], [1, 0, 0]]); print(np.nonzero(a))  # (array([0, 0, 1]), array([0, 2, 0])); a[0, 0], a[0, 2] 和 a[1, 0] 的值不为 0
## 使用由 nonzero() 转换之后的元组作为下标对象
print(a[np.nonzero(a)])  # [1, 1, 1]
b = np.arange(3 * 4 * 5).reshape(3, 4, 5); print(b)
print(b[np.nonzero(a)])  # [[ 0  1  2  3  4] [10 11 12 13 14] [20 21 22 23 24]]; 分别取 [0, 0] [0, 2] [1, 0]
tmp = np.arange(6); print(np.sum(tmp[np.nonzero(np.arange(6))]))  # 15 = 1 + 2 + 3 + 4 + 5; 求非零和
tmp = np.arange(6); print(np.nonzero(np.arange(6))[0].size)  # 5; 求非零个数, array 外面套着 ()
##################################################################
## numpy.where(condition, [x, y]); 函数返回输入数组中满足给定条件的元素的索引, x if cond else y
x = np.arange(9.).reshape(3, 3); print(x)  # [[ 0. 1. 2.] [ 3. 4. 5.] [ 6. 7. 8.]]
y = np.where(x > 3); print(y)  # (array([1, 1, 2, 2, 2]), array([1, 2, 0, 1, 2])); 返回的是一个 [x], [y] 的集合, 类似于稀疏矩阵
print(x[y])  # [ 4. 5. 6. 7. 8.]
print(np.where(x > 3, 1, 0))  # [[0 0 0] [0 1 1] [1 1 1]]; 这里返回的不是系数矩阵...
# where 返回一个原数组大小的矩阵, [x, y] 是三元表达式里面的 x if cond else y; 具体见上面, 不知道怎么解释
##################################################################
## numpy.extract(condition, arr); 函数返回满足任何条件的元素
x = np.arange(9.).reshape(3, 3); print(x)  # [[ 0. 1. 2.] [ 3. 4. 5.] [ 6. 7. 8.]]
condition = np.mod(x, 2) == 0  # 定义条件
print(condition)  # [[ True False True] [False True False] [ True False True]]; 按元素的条件值
print(np.extract(condition, x))  # [ 0. 2. 4. 6. 8.]
