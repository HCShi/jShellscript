#!/usr/bin/python3
# coding: utf-8
from sympy import *  # 标准引入姿势
init_session(use_latex=True)
init_printing(use_latex=True)
##################################################################
## 带变量的表达式, subs() 进行赋值
x, y, z = symbols('x y z')  # 表达式包含有变量, 通常用 x、y 等符号来表示; 在 SymPy 中, 若想要用一个符号表示变量, 要首先对其进行定义
expr = 2 * x + 3 * y + 4 * z; expr
expr.subs({x:2, y:3, z:4})  # 29; [x, y, z] = [2, 3, 4]; 给定一组 x、y、z, 求取表达式值
expr.subs(x, z)  # 3y + 6z
expr * expr; expr ** 2  # 效果相同
## 取二维, 三维空间中一点到原点的距离
r = symbols('r'); d = sqrt(r)
r2 = x**2 + y**2; r3 = x**2 + y**2 +z**2
d.subs(r, r2)  # sqrt(x^2 + y^2)
d.subs(r, r3)  # sqrt(x^2 + y^2 + z^2)
d.subs(r, r2).subs({x:2, y:3})  # 在 d.subs(r, r2) 得到的公式中, 计算点 (2,3) 到原点距离
##################################################################
## sympify() 字符串转化为表达式
# 增强了构建表达式的灵活性, 使得我们不仅仅可以在编程时硬编码表达式, 更可以在运行时从文件中加载表达式
str_expr = "x**2 + 3*x - 1/2"
expr = sympify(str_expr)
##################################################################
## evalf() 对一个表达式进行求值, 并得出浮点数结果
pi.evalf()
pi.evalf(10)  # 10 位精度; evalf 函数默认求取 15 位精度, 但是我们可以对其进行修改
expr.evalf(subs={x:0.001})  # 对于表达式, 可以通过下面方式浮点求值; 将变量的值封装到字典结构中, 附给 evalf 函数的 subs
