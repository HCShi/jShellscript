#!/usr/bin/python3
# coding: utf-8
class Mylist(list):
    def add(self, value): self.append(value)
L = Mylist(); L.add(1); print(L)  # [1]

class Jrp():
    def __init__(self, age): self.age = age
class Dr(Jrp):
    # def __init__(self, age): super(Dr, self).__init__(age)
    # def __init__(self, age): Jrp.__init__(self, age)
    def __init__(self, age): super().__init__(age)  # 三种调用父类 init 的方法, super() 可以省略父类的名字, 第二种适用于多重继承
dr = Dr(15); print(dr.age)
