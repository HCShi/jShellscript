#!/usr/bin/python3
# coding: utf-8
##################################################################
## 一: copy; numpy 中有 np.copy(), a.copy(), 实现相同的功能
import copy
# Python 中的对象之间赋值时是按引用传递的, 如果需要拷贝对象, 需要使用标准库中的 copy 模块
# copy.copy 浅拷贝, 只拷贝父对象, 不会拷贝对象的内部的子对象
# copy.deepcopy 深拷贝, 拷贝对象及其子对象
a = [1, 2, 3, 4, ['a', 'b']]  # 原始对象
b = a  # 赋值, 传对象的引用
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)
a[4].append('c')
print(a)  # [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print(b)  # [1, 2, 3, 4, ['a', 'b', 'c'], 5]
print(c)  # [1, 2, 3, 4, ['a', 'b', 'c']]
print(d)  # [1, 2, 3, 4, ['a', 'b']]
##################################################################
## 二: Python 函数传递
a = 3
def hello(a): a = 4
hello(a); print(a)  # 3; 标量不会被修改

a = [1, 2, 3]
def hello(a): a[2] = 4
hello(a); print(a)  # [1, 2, 4]; 向量被修改了...
