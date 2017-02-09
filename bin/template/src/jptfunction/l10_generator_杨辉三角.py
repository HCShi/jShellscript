#!/usr/bin/python3
# coding: utf-8
# 两种方法生成 generator, 1. 列表生成式, 2. yield
g = (x * x for x in range(10)); print(g)  # 列表生成式的 [] 改成 (), 就创建了一个 generator
print(next(g), next(g))  # next() 基本不会用到
for n in g: print(n)  # for 传入的是 可迭代对象 Iterable, 接着上面的 next() 之后输出

# 函数遇到 return 语句或者最后一行就返回. 而变成generator的函数, 在每次调用next()的时候执行, 遇到yield返回, 再执行时从上次返回的yield处继续执行
def triangles(t):
    L = [1]
    while len(L) <= t:
        yield L  # 函数定义包含 yield, 这个函数不再是普通函数, 而是 generator, yield 相当于 return
        L.append(0)  # 这句想法很好, 就可以用下面的 L[0] = L[-1] + L[0]
        L = [L[i - 1] + L[i] for i in range(len(L))]
print('\n'.join([str(x) for x in triangles(10)]))  # for x in triangles(10): print(x)
