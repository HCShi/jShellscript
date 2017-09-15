#!/usr/bin/python3
# coding: utf-8
fn = lambda x: x * x; print(fn(3))  # 匿名函数
from functools import reduce
##################################################################
# map() 接收两个参数, 函数 和 Iterable, map() 将传入的函数依次作用到序列的每个元素, 并把结果作为新的 Iterator 返回
print(list(map(lambda x: x * x, list(range(1, 4)))))  # [1, 4, 9], Iterator 是惰性序列, list() 让它把整个序列都计算并返回一个 list
day, month, year = map(int, '2017-02-10'.split('-')); print(day, month, year)
# 将 float list -> int list
a = [1.2, 1.8, 0.8]; print(list(map(round, a)))  # [1, 2, 1]
# Python3 中移除了 'Tuple parameter unpacking' 的用法
print(list(map(lambda x: x[0] * x[1], zip([1, 2], [3, 4]))))
# print(list(map(lambda (x, y): x * y, zip([1, 2], [3, 4]))))  # python3 会报错, python2 可以这样写
##################################################################
# reduce() 接收两个参数, 函数 和 Iterable, reduce() 把函数作用在一个序列 [x1, x2, x3, ...] 上, reduce 把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
print(reduce(lambda x, y: x * 10 + y, map(lambda x: x * x, list(range(1, 4)))))  # 149
print(reduce(lambda x, y: x + y[0], [(2, 4), (1, 3)], 0))  # 3, 结构体部分相加的
##################################################################
# filter() 接收两个参数, 函数 和 Iterable, filter() 把传入的函数依次作用于每个元素, 然后根据返回值是 True 还是 False 决定保留还是丢弃该元素
print(list(filter(lambda x: x % 2 == 1, list(range(1, 10)))))  # 筛选出 奇数
print(''.join(filter(lambda x: x and x.strip(), 'a b')))  # 将空格去掉, 并返回 str, 也不用加 list 强制转型
##################################################################
# sorted(), 返回值 list
print(sorted([1, -2], key=abs))  # 默认升序, 按绝对值排序
print(sorted(['ab', 'AC'], key=str.lower, reverse=True))  # 默认 'Z' < 'a', 关键字: 忽略大小写, 反序
print(sorted([('a', 3), ('b', 2)], key=lambda x: x[1]))
##################################################################
# zip()
a, b = ['a', 'b', 'c'], [1, 2, 3]; print(a, b)
c = list(zip(a, b)); print(c)
a, b = zip(*c); print(a, b)  # 能将 元素分开, 但是会是 tuple 格式
print(list(a), list(b))  # 转化为 list
##################################################################
# 总结:
# 1. Iterable, 可迭代的, 包括 list, str 等
# 2. map(), filter(), reduce() 三个函数的参数都是 (fn, Iterable)
# 3. map(), filter(), zip(), range() 四个函数的返回值是 惰性的Iterable, 使用时没区别, 打印时需要 list(), ''.join() 的强制转型
# 4. 函数原型: map(lambda x:, Iterable), reduce(lambda x, y:, Iterable), filter(lambda x: Ture or Flase, Iterable)
# 5. lambda 只能写函数定义和返回值
# 6. zip(*c) 好神奇
