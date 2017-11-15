#!/usr/bin/python3
# coding: utf-8
##################################################################
## bitarray
from bitarray import bitarray
a = bitarray(10); print(a)  # 初始化一个有 10 个 bit 位的数组, 初始值为 bitarray('0110100000')
a[1:8] = 1; print(a)  # 可以像操作 list 一样操作 bitarray 对象
if not a.all(): print("not all bits are True.")  # 当 bitarray 中所有的元素都为 1 时, all() 返回为 True
##################################################################
## bisect 排序模块; 使用这个模块以前确定是已经排好序的...
import bisect
## sort() 对原数据进行排序, 会修改原始数据
data = [4, 2, 9, 7]
data.sort(); print(data)  # [2, 4, 7, 9];

## insort() 插入结果不影响原有排序
bisect.insort(data, 3); print(data)  # [2, 3, 4, 7, 9]

## bisect() 其目的在于查找该数值将会插入的位置并返回, 而不会插入
print(bisect.bisect(data, 1))  # 0;
print(data)  # [2, 3, 4, 7, 9]

## bisect_left() 和 bisect_right() 该函数用入处理将会插入重复数值的情况, 返回将会插入的位置
print(bisect.bisect_left(data, 4))  # 2
print(bisect.bisect_right(data, 4))  # 3
print(data)  # [2, 3, 4, 7, 9]

## insort_left() 和 insort_right() 对应的插入函数
bisect.insort_left(data, 4); print(data)  # [2, 3, 4, 4, 7, 9]
data = [2, 3, 4, 7, 9]
bisect.insort_right(data, 4); print(data)  # [2, 3, 4, 4, 7, 9]
# 可见, 单纯看其结果的话, 两个函数的操作结果是一样的, 其实插入的位置不同而已
