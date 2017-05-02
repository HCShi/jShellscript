#!/usr/bin/python3
# coding: utf-8
# timeit 是循环测试小块代码的, 测试 python 文件执行时间用 time 命令.
# 一: 在终端使用
# python -m timeit -s 'from decimal import Decimal as D' 'D("1.2")+D("3.4")'  # -s 表示 statement(from) 只执行一次
# python -m timeit -s 'from decimal import Decimal as D' '1.2+3.4'
# python -m timeit '"-".join(str(n) for n in range(100))'
# 二: 脚本中运行
import timeit  # number 代表循环次数, 命令行中自动决定循环次数
print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))  # 0.3018611848820001
print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))  # 0.2727368790656328
print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))  # 0.23702679807320237
