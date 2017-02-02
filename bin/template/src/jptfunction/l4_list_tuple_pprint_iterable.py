#!/usr/bin/python3
# coding: utf-8
# 两种列表生成式方式: list() 和 [x for x in range(1, 3)]
# x for x in range(1, 3) 是生成器, list() 和 [] 将其转化为列表
print([(a, b) for a, b in [('a', 'b'), ('c', 'd')]])  # [('a', 'b'), ('c', 'd')]
print(list(k + '=' + v for k, v in {'x': 'A', 'y': 'B'}.items()))  # ['y=B', 'x=A'], items() 生成的是 dict_items([('y', 'B'), ('x', 'A')])
print([x * x for x in range(1, 3) if x % 2 == 0])  # [4]
print([m + n for m in 'a' for n in 'de'])  # ['ad', 'ae'], 全排列
print([s.lower() for s in 'HELLO'])  # ['h', 'e', 'l', 'l', 'o']
print([s.lower() for s in ['HE', 'LLO']])  # ['he', 'llo']

# list 格式化输出
lis = 'abcderg'  # 不足的是最后面的可能不是整倍数, 每行 3 个打印, format 只支持 utf-8(str)
print('\n'.join(['{!s:<10}{!s:<20}{!s:<}'.format(a, b, c) for (a, b, c) in list(zip(lis[::3], lis[1::3], lis[2::3]))]))
import sys, pprint;
pprint.pprint(sys.path, indent=4)  # 另一种自动格式化的输出方法
st = pprint.pformat(sys.path)  # 将 pprint 的输出重定向到变量

# 去重
lis = [1, 3, 2, 2, 4]; from functools import reduce
print(list(set(lis)))  # 没有保持原来的顺序
print(reduce(lambda x, y: x if y in x else x + [y], lis, []))  # 保持原来顺序

# 可以直接作用于 for 循环的对象统称为可迭代对象: Iterable, 包括两类
# 一类是集合数据类型, 如 list、tuple、dict、set、str 等, 一类是 generator, 包括生成器和带 yield 的 generator function
from collections import Iterable; print(isinstance([], Iterable))  # 判断是否是 Iterable
# 可以被 next() 函数调用并不断返回下一个值的对象称为迭代器: Iterator
# 生成器都是 Iterator 对象, 但 list、dict、str 虽然是 Iterable, 却不是 Iterator. 可以用 iter() 函数进行转换
from collections import Iterator; print(isinstance((x for x in range(10)), Iterator), isinstance(iter([]), Iterable))
