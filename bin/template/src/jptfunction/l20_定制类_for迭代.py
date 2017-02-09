#!/usr/bin/python3
# coding: utf-8
# Python 类定制方便, 得益于动态语言的 鸭子类型, 不用强制继承某个接口
class Student(object):
    def __init__(self, name='Michael'): self.name = name
    def __str__(self): return 'Student object (name: %s)' % self.name  # 替换掉 <__main__.Student object at 0x109afb190>
    __repr__ = __str__  # 这样不用 print() 也能输出格式化的了
    def __getattr__(self, attr):  # 这对那种类里面没有的变量
        if attr=='age': return 25  # 返回变量
        if attr=='age_f': return lambda: 25  # 返回函数
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)  # 那些没有在这里定义的统一返回这句话
    def __call__(self): print('My name is %s.' % self.name)  # 可以直接对实例进行调用
print(Student('Michael'))  # print() 调用的是 __str__(), >>> Student('Michael') 调用的是 __repr__(), 前者是用户看到的, 后者是开发人员看到的
print(Student('Michael').age)  # getattr 更加有趣的见 jptzen ...
print(Student('Michael').age_f())  # 调用返回函数
print(Student('Michael')()); print(callable(Student()))  # 直接在对象本身上调用, 判断 一个对象是否能被调用
print('========')

class Fib(object):
    def __init__(self): self.a, self.b = 0, 1  # 初始化两个计数器a, b
    def __iter__(self): return self  # 实例本身就是迭代对象, 故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000: raise StopIteration();  # 退出循环的条件
        return self.a  # 返回下一个值
    # 类想用for ... in, 像list或tuple, 必须实现__iter__()方法, 返回一个迭代对象,
    # 然后for不断调用该迭代对象__next__()方法拿到循环的下一个值, 直到遇到StopIteration错误时退出循环
    def __getitem__(self, n):  # 还有 __setitem__ 和 __delitem__ 以后研究
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n): a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start, stop = n.start, n.stop
            if start is None: start = 0
            a, b, L = 1, 1, []
            for x in range(stop):
                if x >= start: L.append(a)
                a, b = b, a + b
            return L
for n in Fib(): print(n)  # 用到了 __iter__ 和 __next__
print(Fib()[100])  # 用到了 __getitem__ + 索引
print(Fib()[0:5], Fib()[:5])  # 用到了 __getitem__ + 切片
