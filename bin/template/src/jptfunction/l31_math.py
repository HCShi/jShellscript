#!/usr/bin/python3
# coding: utf-8
# 1. 精度问题, 因为用二进制存储, 所以有这种问题
print(0.1 + 0.2)  # 0.30000000000000004, solved in http://stackoverflow.com/questions/588004/is-floating-point-math-broken
print('%.2f' % (0.1 + 0.2))  # 最好的解决办法是 Decimal
b = '%.2f' % (0.1 + 0.2)
print(b, type(b))  # str
print(type(float(b)))
