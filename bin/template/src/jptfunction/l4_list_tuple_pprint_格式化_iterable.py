#!/usr/bin/python3
# coding: utf-8
##################################################################
## 两种列表生成式方式: list() 和 [x for x in range(1, 3)]
# x for x in range(1, 3) 是生成器, list() 和 [] 将其转化为列表; 必须保证每一步的 for 的结果都是可迭代的
print([(a, b) for a, b in [('a', 'b'), ('c', 'd')]])               # [('a', 'b'), ('c', 'd')]
print([(x[0], x[1]) for x in [('a', 'b', 'c'), ('d', 'e', 'f')]])  # [('a', 'b'), ('d', 'e')]; 去除列表中元素的一部分
print([m for n in [('a', 'b'), ('c', 'd')] for m in n])            # ['a', 'b', 'c', 'd']; 嵌套取出
print(list(k + '=' + v for k, v in {'x': 'A', 'y': 'B'}.items()))  # ['y=B', 'x=A'], items() 生成的是 dict_items([('y', 'B'), ('x', 'A')])
print([x * x for x in range(1, 3) if x % 2 == 0])  # [4]
print([m + n for m in 'a' for n in 'de'])          # ['ad', 'ae'], 全排列
print([s.lower() for s in 'HELLO'])        # ['h', 'e', 'l', 'l', 'o']
print([s.lower() for s in ['HE', 'LLO']])  # ['he', 'llo']
print([1 if a == 0 else 0 for a in range(5)])  # [1, 0, 0, 0, 0]; 嵌套 if; ** 这里的 if 后面一定要有 else **
# data = [word for raw in passwd if re.search(r'(\d+\-\d+\-\d+)', raw) for word in re.search(r'(\d+)', raw).groups()]
#     匹配 passwd 中的生日信息, research 可能返回 None, 所以要先加一个 if 判断
# for link in self.links: res.append((self.nodes[link.fo].name, self.nodes[link.to].name))  # 和下面那句话进行了等价的转换
# res.extend([(self.nodes[link.fo].name, self.nodes[link.to].name) for link in self.links])
# clean_mess = [word for word in line.split() if word.lower() not in stopwords.words('english')]  # 去掉一行话里的停用词
print([[i, j, k] for i in range(3) for j in range(3) for k in range(3)])
# a, b = 1, 2; [a += b for _ in range(3)]  # 会报错, 生成器中不能有 =
print([[0 for col in range(3)] for row in range(4)])  # 生成 4 x 3 的零矩阵

# 计算操作, 将 += 提取出来
import numpy as np
a = [[1, 2], [3, 4]]; b = [[1, 2], [3, 4]]; matrix = np.array([[0, 0], [0, 0]]); matrix2 = [[0, 0], [0, 0]]
for i in range(len(a)):  # matrix2 为了说明 numpy.array() 和 普通 list 的区别
    for j in range(len(b[0])):
        matrix[i][j] += np.sum([a[i][j] * b[k][j] for k in range(len(b))])  # 矩阵乘法, 转换为下面一行
matrix += [[np.sum([a[i][j] * b[k][j] for k in range(len(b))]) for j in range(len(b[0]))] for i in range(len(a))]
matrix2 += [[np.sum([a[i][j] * b[k][j] for k in range(len(b))]) for j in range(len(b[0]))] for i in range(len(a))]

# [] 和 ()
a = []; print([a.append(i) for i in range(3)]); print(a)  # [None, None, None] [0, 1, 2]; 生成器输出 None
a = []; print((a.append(i) for i in range(3))); print(a)  # <generator> []; 输出生辰器对象, a 还是空

# 多维 []; 每一维中有一个变量可以放到前面, 后面用 for 解释; 其他的变量必须先定义, 才能用
a = [['he', 'she'], ['123', '234']]
print([[word for word in item] for item in a])  # [['he', 'she'], ['123', '234']]
print([word for item in a for word in item])  # ['he', 'she', '123', '234']
##################################################################
## 初始化矩阵, 在 ACM 中 DP 经常见到
dp = [[1] * 5] + [[0] * 5 for _ in range(2)]; print(dp)  # 首行为 5, 其余为 0
dp = [1] + [0] * 4; print(dp)  # 这里就是 一维的, 上面是 二维的...
##################################################################
## index()
print([1, 2, 3].index(2))  # 1
print([1, 2, 2].index(2))  # 1; 只索引第一个...
##################################################################
## append(), extend(), +; extend() = +
a = []; a.append(2); print(a)  # [2]; append 针对单个元素
a = []; a.extend([2]); print(a)  # [2]; extend 针对 list 元素
# 下面是容易弄混的
a = []; a.append([2]); print(a)  # [[2]]
a = [[]]; a.append([2]); print(a)  # [[], [2]]
a = [[]]; print(a + [2])  # [[], 2]
a = [[]]; print(a + [[2]])  # [[], [2]]; 结论是: + 和 extend 会去掉外面的一层 [], append() 什么都不会去掉
# list 之间的操作
a = [1, 2, 3]; a.append([4, 5]); print(a)  # [1, 2, 3, [4, 5]]
a = [1, 2, 3]; a.append((4, 5)); print(a)  # [1, 2, 3, (4, 5)]; 所以 append 一次只能加 1 个
a = [1, 2, 3]; a.extend([4, 5]); print(a)  # [1, 2, 3, 4, 5]
a = [1, 2, 3]; a.extend((4, 5)); print(a)  # [1, 2, 3, 4, 5]; extend 对于 tuple 也行
a = [1, 2, 3]; a += [4, 5]; print(a)  # [1, 2, 3, 4, 5]
a = [1, 2, 3]; a += (4, 5); print(a)  # [1, 2, 3, 4, 5]; + 对于 tuple 也行
a = [1, 2, 3]; a += [[4, 5]]; print(a)  # [1, 2, 3, [4, 5]]
a = [1, 2, 3]; a += ((4, 5)); print(a)  # [1, 2, 3, 4, 5]; 双层的 tuple 也可以...
# 操作 []
a = [1, 2, 3]; a.append([]); print(a)  # [1, 2, 3, []]
a = [1, 2, 3]; a.extend([]); print(a)  # [1, 2, 3]
a = [1, 2, 3]; a += []; print(a)  # [1, 2, 3]
a = [1, 2, 3]; a += [[]]; print(a)  # [1, 2, 3, []]
# 嵌套 list
a = [['hello', 'word']]; print(a)  # [['hello', 'word']]
a = [['hello', 'word']]; a += ['jrp']; print(a)  # [['hello', 'word'], 'jrp']
a = [['hello', 'word']]; a += [['jrp']]; print(a)  # [['hello', 'word'], ['jrp']]
a = [['hello', 'word']]; a.append('jrp'); print(a)  # [['hello', 'word'], 'jrp']
# 实战 ./l72_heapq.py 中实现 Heap 堆的 Huffman 树
a, b = [1, ['T', '']], [1, ['b', '']]; print(a[1:])  # [['T', '']]
print([a[0] + b[0]] + a[1:] + b[1:])  # [2, ['T', ''], ['b', '']]; +, extend() 会去掉外面一层 []
##################################################################
## pprint, list 格式化输出
lis = 'abcderg'  # 不足的是最后面的可能不是整倍数, 每行 3 个打印, format 只支持 utf-8(str)
print('\n'.join(['{!s:<10}{!s:<20}{!s:<}'.format(a, b, c) for (a, b, c) in list(zip(lis[::3], lis[1::3], lis[2::3]))]))
import sys, pprint;
pprint.pprint(sys.path, indent=4)  # 另一种自动格式化的输出方法
st = pprint.pformat(sys.path)  # 将 pprint 的输出重定向到变量
print("%s\n %-*s | %-*s | %-*s \n%s" % ("-" * 33, 6, "WIFIID", 13, "SSID OR BSSID", 6, "KEYNUM", "=" * 33))  # 类似于 prettytable
print('%s %%' % 'hello')  # 一个占位符, 后面不用加括号; %% 对 % 进行转义
##################################################################
## 去重
lis = [1, 3, 2, 2, 4]; from functools import reduce
print(list(set(lis)))  # 没有保持原来的顺序
newlis = list(set(lis)); newlis.sort(key=lis.index); print(newlis)  # 使用 index 排回原来的顺序
print(reduce(lambda x, y: x if y in x else x + [y], lis, []))  # 保持原来顺序
##################################################################
## 可以直接作用于 for 循环的对象统称为可迭代对象: Iterable, 包括两类
# 一类是集合数据类型, 如 list、tuple、dict、set、str 等, 一类是 generator, 包括生成器和带 yield 的 generator function
from collections import Iterable; print(isinstance([], Iterable))  # 判断是否是 Iterable
# 可以被 next() 函数调用并不断返回下一个值的对象称为迭代器: Iterator
# 生成器都是 Iterator 对象, 但 list、dict、str 虽然是 Iterable, 却不是 Iterator. 可以用 iter() 函数进行转换
from collections import Iterator; print(isinstance((x for x in range(10)), Iterator), isinstance(iter([]), Iterable))
##################################################################
## itertools
import itertools
for n in itertools.count(2):
    if(n == 5): break;  # 会创建一个无限的迭代器, 从 传入参数开始 打印自然数序列
    print(n)
# for n in itertools.cycle('ABC'): print(n)  # 字符 'A', 'B', 'C' 循环输出
for n in itertools.repeat('A', 3): print(n)  # 重复某一个字符, 可控制次数
