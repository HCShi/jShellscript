#!/usr/bin/python3
# coding: utf-8
# 区间分析 精妙的地方就在减法和乘法的运算规则..., 保证了在 [x1, x2] 上计算的 [y1, y2] 所形成的矩形能够将 曲线全部包围住
import math
nan = float('nan')  # not a number, represent for empty interval
oo = float('inf')  # infinity, 这两个的定义好厉害啊
class Interval:
    def __init__(x, a, b):  # 每个类方法的第一个参数都是实例本身, self 只是约定俗成, 可全部替换成别的, 这里比 self 直观了很多, 学习了...
        if a > b: x.lb, x.ub = nan, nan  # low / up boundary, 上下边界
        else: x.lb, x.ub = a, b  # 还有就是一维的 Interval 定义为 x, 二位的 Box 定义为 X
    def __add__(x, y):  # overloading x + y
        return Interval(x.lb + y.lb, x.ub + y.ub)  # [a] + [b] = [min(a) + min(b), max(a) + max(b)]
    def __sub__(x, y):  # overloading x - y
        return Interval(x.lb - y.ub, x.ub - y.lb)  # [a] - [b] = [min(a) - max(b), max(a) - min(b)]
    def __mul__(x, y):  # overloading x * y
        L = [x.lb * y.lb, x.lb * y.ub, x.ub * y.lb, x.ub * y.ub]
        return Interval(min(L), max(L))  # [a] * [b] = [四个数分别相乘的 最小值, 最大值]
    def __rmul__(x, y):  # overloading 2 * x, not support x * 2
        return x.__mul__(Interval(y, y))  # n * [a] = [n] * [a] ([n] is [n, n])
    def __contains__(x, a):  # for 0 in y
        return (x.lb <= a <= x.ub)
    def __truediv__(x, y):  # overloading x / y
        if 0 in y: return Interval(-oo, oo)  # use the __contains__()
        else: return x * Interval(1. / y.ub, 1. / y.lb)  # In python3,  we don't need to write the dot
    def __and__(x, y):  # overloading x & y
        if x.is_empty() or y.is_empty():
            return Interval(1, 0)
        else:
            return Interval(max(x.lb, y.lb), min(x.ub, y.ub))
    def __repr__(x): return("[%f, %f]" % (x.lb, x.ub))  # 方便打印, 比 str 功能还要多, 支持交互式非 print 打印
    # 下面这四个是在后面的 myBox 中用到的
    def is_empty(x): return math.isnan(x.lb)  # 判断是否为空
    def width(x): return x.ub - x.lb
    def left(x): return Interval(x.lb, 0.5 * (x.lb + x.ub))
    def right(x): return Interval(0.5 * (x.lb + x.ub), x.ub)
def sqr(x):  # 下面这几个函数没有用面向对象的方式去实现, 是为了和数学表达式靠拢, 最下面的式子表示效果很好
    L = [x.lb ** 2, x.ub ** 2]
    if 0 in x: return Interval(0, max(L))
    else: return Interval(min(L), max(L))
def mini(x, y):  return Interval(min(x.lb, y.lb), min(x.ub, y.ub))  # to adapte the native min
def maxi(x, y):  return Interval(max(x.lb, y.lb), max(x.ub, y.ub))  # to adapte the native max
def exp(x): return Interval(math.exp(x.lb), math.exp(x.ub))
def log(x):
    if x.ub <= 0: return Interval(1, 0)
    elif 0 in x: return Interval(-oo, math.log(x.ub))
    else: return Interval(math.log(x.lb), math.log(x.ub))
def subset(x, y):  # 判断是否是子集
    if x.is_empty(): return True
    else: return (x.lb in y) and (x.ub in y)
def disjoint(x, y):  # 判断是否相交
    return (x & y).is_empty()
if __name__ == '__main__':
    x, y = Interval(-2, 2), Interval(3, 4)
    print('x =', x, 'y =', y)
    print('x + y =', x + y, ', x + y + y =', x + y + y)
    print('x - y =', x - y)
    print('x * y =', x * y, ' 2 * x =', 2 * x)
    print('x / y =', x / y)
    print('sqr(x) =', sqr(x), 'exp(x) =', exp(x), 'log(x) =', log(x))
    print('sqr(x) + 2 * x - exp(x) =', sqr(x) + 2 * x - exp(x))
