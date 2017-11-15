#!/usr/bin/python3
# coding: utf-8
for idx, i in enumerate(range(2, 5)): print(idx, i)  # 会同时输出索引和值
# 0 2
# 1 3
# 2 4
for i, e in enumerate(range(2, 5), 3): print(i, e)  # enumerate(iterable[, start]); 可以修改 start
# 3 2
# 4 3
# 5 4
##################################################################
## enumerate 不能处理 dict 类型的
for i, e in enumerate({'hello': 3, 'world':4, 'jrp': 6}): print(i, e)
# 0 hello
# 1 world
# 2 jrp
from collections import Counter
for i, e in enumerate(Counter(['cat', 'dog', 'cat'])): print(i, e)
# 0 cat
# 1 dog
##################################################################
## operator
# operator 模块提供的 itemgetter 函数用于获取对象的哪些维的数据, 参数为一些序号(即需要获取的数据在对象中的序号), 下面看例子
import operator
a = [1, 2, 3]
b = operator.itemgetter(1)  # 定义函数 b, 获取对象的第 1 个域的值
print(b(a))  # 2
b = operator.itemgetter(1, 0)   # 定义函数 b, 获取对象的第 1 个域和第 0 个的值
print(b(a))  # (2, 1)
# 要注意, operator.itemgetter 函数获取的不是值, 而是定义了一个函数, 通过该函数作用到对象上才能获取值
# 用 operator 函数进行多级排序
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10),]
print(sorted(students))  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]; 默认是按 name, grade, age 一次往后排
print(sorted(students, key=operator.itemgetter(1, 2)))  # [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]; sort by grade then by age
print(sorted(students, key=operator.itemgetter(2, 1)))  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]; sort by age then by grade
# 对字典排序
d = {'data1': 3, 'data2': 1, 'data3': 2, 'data4': 4}
print(sorted(d.items(), key=operator.itemgetter(1)))  # [('data2', 1), ('data3', 2), ('data1', 3), ('data4', 4)]
print(sorted(d.items(), key=operator.itemgetter(1), reverse=True))  # [('data4', 4), ('data1', 3), ('data3', 2), ('data2', 1)]
# 对 list 排序, 并取出 index
print(max(enumerate([3, 4, 2, 1]), key=operator.itemgetter(1)))
##################################################################
## reversed(sequence) -> reverse iterator over values of the sequence
print(list(reversed([1, 2, 3])))  # [3, 2, 1]
print(list(reversed((1, 2, 3))))  # [3, 2, 1]; 因为最后 list() 列表化了
# print(list(reversed({'a': 1, 'b': 2})))  # 'dict' object is not reversible
