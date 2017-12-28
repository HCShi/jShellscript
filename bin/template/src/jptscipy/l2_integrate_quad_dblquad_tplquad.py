#!/usr/bin/python3
# coding: utf-8
import numpy as np
import scipy as sp
from scipy.special import jn, yn, jn_zeros, yn_zeros
from scipy.integrate import quad, dblquad, tplquad  # quad, dblquad, tplquad 分别对应单积分, 双重积分, 三重积分
##################################################################
## quad 函数有许多参数选项来调整该函数的行为, 详情见 help(quad)
def f(x): return x  # define a simple function for the integrand
x_lower = 0  # the lower limit of x
x_upper = 1  # the upper limit of x
val, abserr = quad(f, x_lower, x_upper)
print("integral value =", val, ", absolute error =", abserr)  # integral value = 0.5 , absolute error = 5.55111512313e-15
##################################################################
## 如果我们需要传递额外的参数, 可以使用 args 关键字
def integrand(x, n): return jn(n, x)  # Bessel function of first kind and order n.
x_lower = 0  # the lower limit of x
x_upper = 10 # the upper limit of x
val, abserr = quad(integrand, x_lower, x_upper, args=(3,))
print(val, abserr)  # 0.736675137081 9.38925687719e-13
##################################################################
## 对于简单的函数我们可以直接使用匿名函数
val, abserr = quad(lambda x: np.exp(-x ** 2), -np.Inf, np.Inf)
print("numerical  =", val, abserr)  # numerical  = 1.77245385091 1.42026367809e-08
analytical = np.sqrt(np.pi)
print("analytical =", analytical)  # analytical = 1.77245385091
##################################################################
## 高阶积分用法类似
def integrand(x, y): return np.exp(-x**2 - y**2)
x_lower = 0
x_upper = 10
y_lower = 0
y_upper = 10
val, abserr = dblquad(integrand, x_lower, x_upper, lambda x : y_lower, lambda x: y_upper)
print(val, abserr)  # 0.785398163397 1.63822994214e-13
# 注意到我们为 y 积分的边界传参的方式, 这样写是因为 y 可能是关于 x 的函数
