#!/usr/bin/python3
# coding: utf-8
import decimal
import numpy as np
##################################################################
## Decimal
d = decimal.Decimal('1.1')
a = np.array([d, d, d], dtype=np.dtype(decimal.Decimal))
print(a)  # [Decimal('1.1') Decimal('1.1') Decimal('1.1')]
print(type(a[1]))  # <class 'decimal.Decimal'>
a = np.array([1.1, 1.1, 1.1], dtype=np.dtype(decimal.Decimal))
print(a)  # [1.1 1.1 1.1]
##################################################################
## 实际应用
a = np.array([9.5, 26.5, 7.8])
print(sorted(a))  # [7.7999999999999998, 9.5, 26.5]; 如何精确取值
a = np.array([9.5, 26.5, 7.8], dtype=np.dtype(decimal.Decimal))
print(a, sorted(a))  # [9.5 26.5 7.8] [7.8, 9.5, 26.5]
