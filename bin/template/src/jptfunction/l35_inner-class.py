#!/usr/bin/python3
# coding: utf-8
class Outer:
    def __init__(self): self.name = 'parent'
    def getName(self): print(self.name)
    class Inner:
        def __init__(self): self.name = 'child'
        def getName(self): print(self.name)
if __name__ == '__main__':
    inner = Outer.Inner(); inner.getName()  # child; 可以通过类来调用
    outer = Outer(); print(outer.name)  # parent
    inner = outer.Inner(); print(inner.name)  # child; 还可以通过成员变量来调用
    # 内部类不能访问外部的变量...
