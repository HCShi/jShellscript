#!/usr/bin/python3
# coding: utf-8
from sympy import *  # 标准引入姿势
import numpy as np
init_session(use_latex=True)
init_printing(use_latex=True)
a, b, x, y, z = symbols("a b x y z")
##################################################################
## simplify 化简表达式
simplify(sin(x)**2 + cos(x)**2)  # 1
simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))  # x - 1
simplify(gamma(x)/gamma(x - 2))  # (x - 2)*(x - 1); gamma(x) x 的阶乘
##################################################################
## expand 展开表达式
expand((x + 1)**2)  # x**2 + 2*x + 1
expand((x + 2)*(x - 3))  # x**2 - x - 6
##################################################################
## factor 因式分解
factor(x**3 - x**2 + x - 1)  # (x - 1)*(x**2 + 1)
factor(x**2*z + 4*x*y*z + 4*y**2*z)  # z*(x + 2*y)**2
# factor 函数的实现采用了一种完整的有理数多变量因式分解算法, 能够保证因式为最简
# 使用 factor_list 函数, 能够将因式分解后得到的因式作为一个列表 (List) 返回
factor_list(x**2*z + 4*x*y*z + 4*y**2*z)  # (1, [(z, 1), (x + 2*y, 2)])
##################################################################
## collect 合并同类项
expr = x*y + x - 3 + 2*x**2 - z*x**2 + x**3
expr  # x**3 - x**2*z + 2*x**2 + x*y + x - 3
collected_expr = collect(expr, x)
collected_expr  # x**3 + x**2*(-z + 2) + x*(y + 1) - 3
##################################################################
## cancel 分式化简
cancel((x**2 + 2*x + 1)/(x**2 + x))  # (x + 1)/x
expr = 1/x + (3*x/2 - 2)/(x - 4)
expr  # (3*x/2 - 2)/(x - 4) + 1/x
cancel(expr)  # (3*x**2 - 2*x - 8)/(2*x**2 - 8*x)
expr = (x*y**2 - 2*x*y*z + x*z**2 + y**2 - 2*y*z + z**2)/(x**2 - 1)
expr  # (x*y**2 - 2*x*y*z + x*z**2 + y**2 - 2*y*z + z**2)/(x**2 - 1)
cancel(expr)  # (y**2 - 2*y*z + z**2)/(x - 1)
##################################################################
## apart 分式裂项; 将一个分式分解为几个分式的和、差, 且分解出来的分式, 都是最简形式
expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
expr  # (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
apart(expr)  # (2*x - 1)/(x**2 + x + 1) - 1/(x + 4) + 3/x
##################################################################
## trigsimp 三角化简; 由三角函数组成的表达式
trigsimp(sin(x)**2 + cos(x)**2)  # 1
trigsimp(sin(x)**4 - 2*cos(x)**2*sin(x)**2 + cos(x)**4)  # cos(4*x)/2 + 1/2
trigsimp(sin(x)*tan(x)/sec(x))  # sin(x)**2
# trigsimp 函数也能够化简双曲三角函数
trigsimp(cosh(x)**2 + sinh(x)**2)  # cosh(2*x)
trigsimp(sinh(x)/tanh(x))  # cosh(x)
# 与 simplify 相似的是, trigsimp 对输入的表达式应用多种三角变换公式, 使用启发式的方法来返回 "最好" 的那一个
##################################################################
## expand_trig 三角展开; 它能够使用三角恒等式, 将三角表达式展开
expand_trig(sin(x + y))  # sin(x)*cos(y) + sin(y)*cos(x)
expand_trig(tan(2*x))  # 2*tan(x)/(-tan(x)**2 + 1)
##################################################################
## powsimp 指数化简; 指数化简包含合并指数和合并基底两种情况
powsimp(x**a*x**b)  # x**(a + b)
powsimp(x**a*y**a)  # (x*y)**a
# 注意, 对于示例中的第二条语句(合并基底), 要满足一定的条件才能够进行
# 首先, x, y 需为正, 且 a 需为实数; 因此, 我们在创建 symbols 的时候, 必须指定
x, y = symbols('x y', positive=True)
a, b = symbols('a b', real=True)
# 这样, 示例中的语句二才能进行合并基底, 否则, 将显示原表达式, 不做任何处理
##################################################################
## expand_power_exp 指数展开; 与上一节的指数化简相对的, 是指数展开, 同样地, 指数展开包含两个部分, 指数展开与基底展开
## 指数展开对应的函数为 expand_power_exp, 基底展开对应的函数为 expand_power_base
expand_power_exp(x**(a + b))  # x**a*x**b
expand_power_base((x*y)**a)  # x**a*y**a
# 对于语句二, symbols 要与上一节中的基底合并满足同样的条件, 才能得正确得到结果
##################################################################
## powdenest 化简指数的指数
# 对于表达式 (x**a)**b, 含有两层指数, 能将其简化为一层的结构
# 首先, 这种化简需要满足下列的条件, 才能正确进行：
x = symbols('x', positive=True)  # 也就是基底 x 要大于 0
powdenest((x**a)**b)  # x**(a*b)
##################################################################
## expand_log 对数展开; 能够套用指数展开公式来完成展开操作
## log 和 ln 是不同的概念, 而在 SymPy 中, 两个是等同的, 都指自然对数。
x, y = symbols('x y', positive=True)
n = symbols('n', real=True)
expand_log(log(x*y))  # log(x) + log(y)
expand_log(log(x/y))  # log(x) – log(y)
expand_log(log(x**2))  # 2*log(x)
expand_log(log(x**n))  # n*log(x)
##################################################################
## logcombine 对数合并; 变量需要满足与上一节中同样的条件
logcombine(log(x) + log(y))  # log(x*y)
logcombine(n*log(x))  # log(x**n)
