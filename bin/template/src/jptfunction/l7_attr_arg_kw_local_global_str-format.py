#!/usr/bin/python
# coding: utf-8
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
##################################################################
# local global
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
# format, 另外还有 list 里面的格式化
print('hello {}, {}'.format('jrp', 'beijing')), ('hello %s, %s' % ('jrp', 'beijing'))
print(r'\\\\t')  # r 内部字符串不转义
print(b'A' == 'A', b'A' == b'\x41')  # False, True
print('''hello
    world'''); print('hello\nworld')  # 两种换行方式
print('ab' in ['ab', 'cd'])
print('hello.py'.endswith('py'))
