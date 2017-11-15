#!/usr/bin/python3
# coding: utf-8
# 两种方法生成 generator, 1. 列表生成式, 2. yield
##################################################################
## 1. 列表生成式
g = (x * x for x in range(10)); print(g)  # 列表生成式的 [] 改成 (), 就创建了一个 generator
print(next(g), next(g))  # next() 基本不会用到
for n in g: print(n)  # for 传入的是 可迭代对象 Iterable, 接着上面的 next() 之后输出
##################################################################
## 2. yield
# 函数遇到 return 语句或者最后一行就返回. 而变成 generator 的函数,
# 在每次调用 next() 的时候执行, 遇到 yield 返回, 再执行时从上次返回的 yield 处继续执行
def triangles(t):
    L = [1]
    while len(L) <= t:
        yield L  # 函数定义包含 yield, 这个函数不再是普通函数, 而是 generator, yield 相当于 return
        L.append(0)  # 这句想法很好, 就可以用下面的 L[0] = L[-1] + L[0]
        L = [L[i - 1] + L[i] for i in range(len(L))]
print('\n'.join([str(x) for x in triangles(10)]))  # for x in triangles(10): print(x)
##################################################################
## 2.1 yield Word2Vec
# 将输入视为 Python 的内置列表很简单, 但是在输入很大时会占用大量的内存.
# 所以 Gensim 只要求输入按顺序提供句子, 并不将这些句子存储在内存, 然后 Gensim 可以加载一个句子, 处理该句子, 然后加载下一个句子
# 例如, 如果输入分布在硬盘上的多个文件中, 文件的每一行是一个句子, 那么可以逐个文件, 逐行的处理输入:
class MySentences(object):
    def __init__(self, dirname): self.dirname = dirname
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
sentences = MySentences('/some/directory')  # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences)
