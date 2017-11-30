#!/usr/bin/python
# coding: utf-8
##################################################################
## attr, arg, kw
"""world"""
print(help(str)), (dir(str))  # 帮助文档, 属性
def empty():
    """ jrp """
    pass
class Jrp():
    def hello(*args, **kw):  # args 传的是 list, kw 传的是 dict
        """hello"""
        print([x for x in args], end="")
        print([key + '=' + value for key, value in kw.items()])
jrp = Jrp()
print(jrp.hello.__doc__, __doc__, empty.__doc__)  # hello world jrp
print('123'.__len__())  # 等同于 len(str)
jrp.hello('hello', 'world')  # ['hello', 'world'][]
jrp.hello(name='jrp')  # []['name=jrp']
print(jrp.__class__, jrp.__class__.__name__)  # <class '__main__.Jrp'> Jrp
import os
print(os.path.abspath(__file__))  # /home/coder352/github/jShellscript/bin/template/src/jptfunction/l7_attr_arg_kw_local_global_str-format.py
print(__file__)  # l7_attr_arg_kw_local_global_str-format.py; __file__ 不能在 Interactive 环境中执行
##################################################################
## local global
one, two = 'one', 'two'
l = [one, two]
def some_stuff(): print("i am sure some stuff")
for item in l:
    def _f(): some_stuff()
    globals()[item] = _f  # globals() 返回的是 dict, 通过 [] 来获得 value
    del _f
one(), two()
def hello(name, age='age'):
    print(locals())  # 基于字典的局部变量 {'age': 'age', 'name': 'jrp'}
    print(globals())  # 当前模块(文件)的所有变量, 包括 import 的
hello('jrp')
##################################################################
## function get global variables
# If you want to simply access a global variable you just use its name.
# However to change its value you need to use the global keyword.
num = 5
def test(): print(num)
def test_1(): num += 3; print(num)
def test_2(): global num; num += 3; print(num)
test(); test_2()
# test_1()  # 会报错
