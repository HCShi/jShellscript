#!/usr/bin/python3
# coding: utf-8
##################################################################
# property 属性函数: 1. 将类方法转换为只读属性; 2. 重新实现一个属性的 setter 和 getter 方法
# 一: 使用属性函数的最简单的方法之一是将它作为一个方法的装饰器来使用
class Person(object):
    def __init__(self, first_name, last_name): self.first_name, self.last_name = first_name, last_name
    @property  # 将一个类方法转变成一个类属性
    def full_name(self):  return "%s %s" % (self.first_name, self.last_name)
person = Person("Mike", "Driscoll"); print(person.full_name)  # Mike Driscoll
# person.full_name = "Jackalope"  # AttributeError: can't set attribute; 只读属性
person.first_name = "Dan"; print(person.full_name)  # 'Dan Driscoll'; 但是可以间接修改
# 二: 取代 setter 和 getter
class Fees(object):
    def __init__(self): self._fee = None
    @property
    def fee(self): return self._fee  # getter 方法
    @fee.setter
    def fee(self, value): self._fee = value  # setter 方法
f = Fees(); f.fee = 1; print(f.fee)  # 好处就是统一了 getter 和 setter, 但又比直接操作 _fee 安全
