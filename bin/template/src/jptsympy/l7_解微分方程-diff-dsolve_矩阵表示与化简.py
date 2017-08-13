#!/usr/bin/python3
# coding: utf-8
from sympy import *  # 标准引入姿势
init_session(use_latex=True)
init_printing(use_latex=True)
f = Function('f')
x = Symbol('x')
##################################################################
## diff(f, var) 求导/微分函数
diff(f(x), x)  # 求 y = f(x) 的微分(导数); 图片形式显示
print(diff(f(x), x))  # Derivative(f(x), x)
diff(sin(x), x)  # cos(x)
diff(x**3, x, 1)  # 3*x**2; 一阶导数可以省略
diff(x**3, x, 2)  # 6*x; 高阶导数不能省略
diff(x**3, x, 3)  # 6
diff(x**3, x, 4)  # 0
##################################################################
## dsolve(eq, f(x)) 解决微分方程(differential equation)的函数
## 第一个参数为微分方程 (要先将等式移项为右端为 0 的形式); 第二个参数为要解的函数 (在微分方程中)
print(2*x - diff(f(x), x))
dsolve(2*x - diff(f(x), x), f(x))  # Eq(f(x), C1 + x**2)
##################################################################
## 题目一: 求 y' = 2xy 的通解
dsolve(diff(f(x), x) - 2*x*f(x), f(x))  # Eq(f(x), C1*exp(x**2))
##################################################################
## 符号与矩阵表示
x1, x2, x3 = symbols('x1 x2 x3')
a11, a12, a13, a22, a23, a33 = symbols('a11 a12 a13 a22 a23 a33')
m = Matrix([[x1, x2, x3]]); m  # 注意 m 的表示, 需要有两个中括号
n = Matrix([[a11, a12, a13], [a12, a22, a23], [a13, a23, a33]]); n
v = Matrix([[x1], [x2], [x3]]); v
f = m * n * v; f  # Matrix([[x1*(a11*x1 + a12*x2 + a13*x3) + x2*(a12*x1 + a22*x2 + a23*x3) + x3*(a13*x1 + a23*x2 + a33*x3)]])
f[0].subs({x1:1, x2:1, x3:1})  # a11 + 2*a12 + 2*a13 + a22 + 2*a23 + a33
