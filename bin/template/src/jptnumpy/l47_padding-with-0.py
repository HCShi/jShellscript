#!/usr/bin/python3
# coding: utf-8
import numpy as np
a = np.ones((3, 3)); print(a)
b = np.ones((4, 4)); print(b)
# 将 a 填充成 b 的样子
res = np.zeros(b.shape); print(res)
res[:a.shape[0], :a.shape[1]] = a; print(res)
