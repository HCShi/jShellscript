#!/usr/bin/python3
# coding: utf-8
# set 是一组 key 的集合, 但是不存储 value, key 不能重复
s = set([1, 1, 2, 3]); print(s)  # 创建 set, 需要提供 list 作为输入集合
s.add(4); s.remove(2); print(s)
s1 = set([1, 2, 3]); s2 = set([2, 3, 4]); print(s1 & s2, s1 | s2)  # 数学运算
##################################################################
## 添加元素
print(set() | {'hello'})  # {'hello'}
