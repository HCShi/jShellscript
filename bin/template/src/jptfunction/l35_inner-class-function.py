#!/usr/bin/python3
# coding: utf-8
##################################################################
## inner-class
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
##################################################################
## inner-function
# 当一个 function 中的逻辑写的比较多的时候, 可以嵌套 function
def person():
    name = 'jrp'
    age = 25
    tag = 'god'
    def show():
        print(name, age, tag)
    show()
person()
# person().show() 不可以这样调用
