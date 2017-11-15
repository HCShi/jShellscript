#!/usr/bin/python3
# coding: utf-8
##################################################################
## 闭包: 它是个内层函数,由一个变量来指代,而这个变量对于外层包含它的函数来说是本地变量
def make_adder(addend):
    def adder(augend):  # adder 为内层函数
        return augend + addend
    return adder
a = make_adder(1)  # 产生一个闭包, addend 为 1, 注意 return 的是 adder
b = make_adder(2)  # 产生另一个闭包, addend 为 2, 注意 return 的是 adder
print (a(100), b(100))  # 101, 102; a(100) 就相当于 adder(100), adden 之前为 1, 因此返回 100+1
##################################################################
## 装饰器就是一个返回函数的高阶函数
## 二层装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper  # 把函数名返回, 就可以给 wrapper 传参数了
# 使用
@log
def now(): print('hello')
now()  # call now(): hello
print(now.__name__)  # wrapper, 已经把名字改了, 可以通过下面的方式改回来
##################################################################
## 三层装饰器, 如果 decorator 本身需要传入参数, 那就需要编写一个返回 decorator 的高阶函数, 写出来会更复杂, 比如, 要自定义log的文本
import functools
def log(text):  # 为了传一个参数, 加一层闭包
    def decorator(func):
        @functools.wraps(func)  # 这句话相当于下面的 wrapper.__name__ = func.__name__
        def wrapper(*args, **kw):
            # wrapper.__name__ = func.__name__
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')  # 带参数返回的就是上面二层装饰器
def now(): print('hello')
now()  # execute now(): hello
print(now.__name__)  # now, 如果 @functools.wraps 就会返回 wrapper
