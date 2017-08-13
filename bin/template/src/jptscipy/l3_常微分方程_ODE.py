#!/usr/bin/python3
# coding: utf-8
# SciPy 提供了两种方式来求解常微分方程: 基于函数 odeint 的 API 与基于 ode 类的面相对象的 API; 通常 odeint 更好上手一些，而 ode 类更灵活一些
# 这里我们将使用 odeint 函数
# dy/dt = f(y, t)
# given initial conditions y(0) = y0, where y is a length N vector and f is a mapping from R^N to R^N.
# A higher-order ordinary differential equation can always be reduced to a differential equation of this type by introducing intermediate derivatives into the y vector.
from scipy.integrate import odeint, ode
# 一直没找到好的微分的例子..
def f(x): return x**2  # 求 y = x^2 在 x = 2 处的导数
print(odeint(f, 0, 2))  # 还是不太懂, 以后了解吧
