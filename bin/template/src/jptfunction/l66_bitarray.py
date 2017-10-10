#!/usr/bin/python3
# coding: utf-8
from bitarray import bitarray
a = bitarray(10); print(a)  # 初始化一个有 10 个 bit 位的数组，初始值为 bitarray('0110100000')
a[1:8] = 1; print(a)  # 可以像操作 list 一样操作 bitarray 对象
if not a.all(): print("not all bits are True.")  # 当 bitarray 中所有的元素都为 1 时，all() 返回为 True
