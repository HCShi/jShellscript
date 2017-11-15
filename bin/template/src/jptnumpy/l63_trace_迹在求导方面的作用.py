#!/usr/bin/python3
# coding: utf-8
import numpy as np
np.random.seed(10)
##################################################################
## H * V = trace(H.t . V)
a = np.random.randint(0, 10, (3, 3))
b = np.random.randint(0, 10, (3, 3))
print(np.sum(a * b))  # 187
print(np.trace(np.dot(b.T, a)))  # 187
