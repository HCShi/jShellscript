#!/usr/bin/python3
# coding: utf-8
import numpy as np
import scipy as sp  # 一般不会用到 sp.func/sp.var, 所以这句命令可以不写; 经常从 scipy 的子模块中引入函数
from scipy.special import jn, yn, jn_zeros, yn_zeros
import matplotlib.pyplot as plt
##################################################################
## Bessel
## 1. Bessel function of the first kind of real order and complex argument.
n = 0    # order
x = 0.0
print("J_%d(%f) = %f" % (n, x, jn(n, x)))  # J_0(0.000000) = 1.000000
## 2. Bessel function of the second kind of integer order and real argument.
x = 1.0
print("Y_%d(%f) = %f" % (n, x, yn(n, x)))  # Y_0(1.000000) = 0.088257
## 3. plot
x = np.linspace(0, 10, 100)
fig, ax = plt.subplots()
for n in range(4):
    ax.plot(x, jn(n, x), label=r"$J_%d(x)$" % n)
ax.legend()
plt.show()  # 将 Bessel 画出来
## 4. Compute zeros of integer-order Bessel function Jn(x).
n = 0 # order
m = 4 # number of roots to compute
print(jn_zeros(n, m))  # array([  2.40482556,   5.52007811,   8.65372791,  11.79153444])
