#!/usr/bin/python3
# coding: utf-8
import math
##################################################################
## 1. 精度问题, 因为用二进制存储, 所以有这种问题
print(0.1 + 0.2)  # 0.30000000000000004, solved in http://stackoverflow.com/questions/588004/is-floating-point-math-broken
print('%.2f' % (0.1 + 0.2))  # 最好的解决办法是 Decimal
b = '%.2f' % (0.1 + 0.2)
print(b, type(b))  # str
print(type(float(b)))
##################################################################
## 2. log(x[, base])
print(math.log(10))  # 2.302585092994046; 以 e 为底
print(math.sin(math.pi))  # 1.2246467991473532e-16; 弧度制
print(math.log(10, 10))  # 第二个参数表示以 10 为底
# import numpy; print(math.log(np.arange(10)))  # 不支持矩阵...
##################################################################
## 3. exp()
print(math.exp(2))
##################################################################
## 4. min(), max(); With a single iterable argument, return its smallest item.
print(min(2, 3))  # 2
print(min((2, 3), (1, 8), (1, 5)))    # (1, 5); 先按第一个元素排, 如果还有一样的再按第二个元素排
print(min((3, 10), (3, 2), (1, 20)))  # (1, 20)
print(min((10, 1), (2, 3), (1, 10)))  # (1, 10)

print(max([1, 2, 3, 4], key=len))  # object of type 'int' has no len()
print(max(['hel', 'hello'], key=len))  # hello
# with operator
import operator
print(max(enumerate([3, 4, 2, 1]), key=operator.itemgetter(1)))
##################################################################
## 5. sum()
print(sum([1, 2, 3]))  # 6
