#!/usr/bin/python3
# coding: utf-8
def fn(self, name='world'): print('Hello, %s.' % name)  # 先定义函数
Hello = type('Hello', (object,), dict(hello=fn))  # 创建 Hello class, 相当于下面创建 class 的过程
h = Hello(); h.hello()
class Hello_1(object):
    def hello(self, name='world'): print('Hello, %s.' % name)
# type() 创建 class 需要三个参数:
# 1. class 的名称
# 2. 继承的父类集合, 注意 Python 支持多重继承, 如果只有一个父类, 别忘了 tuple 的单元素写法
# 3. class 的方法名称与函数绑定, 这里我们把函数 fn 绑定到方法名 hello 上
# 通过 type() 函数创建的类和直接写 class 是完全一样的,
# 因为 Python 解释器遇到 class 定义时, 仅仅是扫描一下 class 定义的语法, 然后调用 type() 函数创建出 class

# metaclass, 直译为元类, 简单的解释就是: 当我们定义了类以后, 就可以根据这个类创建出实例, 所以: 先定义类, 然后创建实例
# 如果我们想创建出类呢? 那就必须根据metaclass创建出类, 所以: 先定义metaclass, 然后创建类, 连接起来: 先定义metaclass, 就可以创建类, 最后创建实例
class ListMetaclass(type):  # metaclass 是类的模板, 所以必须从`type`类型派生, 按照默认习惯, metaclass 的类名总是以 Metaclass 结尾
    def __new__(cls, name, bases, attrs):  # __new__() 会自动调用, attrs 为当前类 (比如 MyList) 中查找定义的类的所有属性, 然后在其基础上添加 add
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)  # 正常情况下, 定义 class 时, 会自动调用 tyep(), 这里只是自己重载了
# 指示Python解释器在创建MyList时, 要通过 ListMetaclass.__new__() 来创建,  __new__()方法接收到的参数依次是:
# 1. 当前准备创建的类的对象; 2. 类的名字; 3. 类继承的父类集合; 4. 类的方法集合
class MyList(list, metaclass=ListMetaclass):  # 指示使用 ListMetaclass 来定制类, 传入关键字参数 metaclass
    pass
L = MyList(); L.add(1); print(L)
