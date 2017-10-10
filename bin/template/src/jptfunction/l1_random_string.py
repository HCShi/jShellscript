#!/usr/bin/python3
# coding: utf-8
# 很多黑科技参考 numpy.random
import random, string
import numpy as np
import time
random.seed(10)  # 不写这句话, 默认是系统时间, 现在自己指定了, 所以每次生成的随机数会一样
##################################################################
## ascii_letters 包含 大写和小写 的26个英文字母, 不包含数字及其它的字符
print(''.join(random.sample(string.ascii_letters, 4)))  # wEkQ
print(''.join(random.sample(string.ascii_letters + string.digits + '()`~!@#$%^&*-+=|\'{}[]:;"<>,.?/', 4)))  # 这样就更像密码了
print(''.join(random.choice(string.ascii_uppercase + string.digits)))  # 只能生成一个
print(''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(10)))  # 新添的控制长度

def rndColor(): return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))  # randomint(a, b), return between [a, b]
print(rndColor())  # (151, 195, 191), 随机颜色
def gen_random_list(opts, n): return [random.choice(opts) for i in range(n)]
print(gen_random_list('ABCD*', 4))  # ['A', 'D', '*', '*'], 从给定的模式中选
print(gen_random_list(range(1, 5), 4))  # 在 [1, 5) 中随机选
##################################################################
## random.random(), random.randomint()
print(random.random())          # [0, 1) 之间的均匀分布, 这个不能带参数
print(random.randint(0, 1))     # [a, b] 之间的整数, 这个必须加两个参数
##################################################################
## randrange(a, b, step) 在 [a,b] 范围内, 从 a 开始(包含 a), 每隔 step 的数形成的集合
print(random.randrange(0, 10, 2))  # 生成 [0, 10] 之间的偶数, 返回一个数
print(random.randrange(1, 10, 2))  # 生成 [0, 10] 之间的奇数
##################################################################
## choice(seq) 从一个序列 seq 中随机选取一个元素
print(random.choice([1, 2, 3, 4, 5]))
print(random.choice(((1, 2), (3, 4), (5, 6))))
print(random.choice(('abcdef')))
##################################################################
## sample(seq, k) 从一个序列中随机取出 k 个元素
print(random.sample([1, 2, 3, 4, 5], 3))  # [5, 3, 2]; 乱序的
print(random.sample(range(2000000), 1000000)[:10])  # 生成一百万个随机整数, 浮点数可以用 uniform()
# sample() 在上面一百万个排完序以后居然有时候会显示有重复的取值...
##################################################################
## 下面是生成各种分布
##################################################################
## uniform() 均匀分布
print(random.uniform(-10, 10))  # [a, b] 之间均匀分布的浮点数
##################################################################
## normalvariate(mu, sigma) 正态分布; mu=0, sigma=1 为标准正态分布; 除了均匀分布, 正态分布用的是最多的
n = []
for i in range(1000000): n.append(random.normalvariate(0, 1))
print("均值 =", np.mean(n), "\n标准差 =", np.std(n))
##################################################################
## gauss(mu, sigma) 高斯分布; 就是正态分布, 采用了不同的实现方式, 据说运行速度更快
n = []
for i in range(1000000): n.append(random.gauss(0, 1))
print("均值 =", np.mean(n), "\n标准差 =", np.std(n))
##################################################################
## 还有生成三角形分布、对数分布、指数分布、β 分布、伽马分布等的函数
# triangular(low, high, mode) 三角形分布
# lognormvariate(mu, sigma) 对数分布
# expovariate(lambd) 指数分布
# gammavariate(alpha, beta) 伽马分布
# 实际工作中, 这些分布比均匀分布和正态分布用的都少的多
