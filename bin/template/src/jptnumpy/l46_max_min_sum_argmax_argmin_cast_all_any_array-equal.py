#!/usr/bin/python3
# coding: utf-8
import numpy as np
##################################################################
## max, min, argmax, argmin
a = np.array([1, 2, 3]); print(a)
print(a.max(), a.min(), a.sum(), a.argmax(), a.argmin())  # 3 1 6 2 0; 最大值, 最小值, 最大值索引, 最小值索引
a = np.random.random((10, 10)); print(a.max(0))  # 可以根据坐标轴来筛选大小
# 标准库中也有 max(), min(), sum()
a = [1, 2, 3, 4, 5]
print(sum(a), max(a), min(a))  # 15, 5, 1
##################################################################
## cast
b = np.array(range(4)); print(b)  # [0 1 2 3]
y = 2 >= b; print(y)  # [ True  True  True False]
# 很多种方法让 y 变为 int
print(1 * y)  # [1 1 1 0]
print(y.astype(int))  # [1 1 1 0]
print([int(i) for i in y])  # [1, 1, 1, 0]
print([i * 1 for i in y])  # [1, 1, 1, 0]
print(list(map(int, y)))  # [1, 1, 1, 0]
print(list(map(lambda x: 1 if x else 0, y)))  # [1, 1, 1, 0]
##################################################################
## all(), any(), array_equal
a, b, c = np.array([1, 2, 3]), np.array([1, 2, 3]), np.array([1, 2, 4])
a, b = np.arange(6).reshape(2, 3), np.arange(6).reshape(2, 3)
c, d = np.arange(1, 7).reshape(3, 2), np.arange(6).reshape(3, 2)
print(a == b)  # [[ True  True  True] [ True  True  True]]
print(a == c)  # False
print(a == d)  # False

# 这样直接对比不好, 如果 False, 后台会 raise error, 虽然不影响程序运行
# all() Test whether all array elements along a given axis evaluate to True.
# any() Test whether any array element along a given axis evaluates to True
print((a == b).all())  # True; a 和 b 中所有对应元素均相等, 如果均相等, 返回 true, 只要有一个不相等, 返回 false
print((a == c).any())  # True

# print(a.array_equal(b))  # 不能这样写
print(np.array_equal(a, b))  # True
print(np.array_equal(a, c))  # False
# 推荐 np.array_equal() 写法
