#!/usr/bin/python3
# coding: utf-8
# 廖雪峰: 定制类
class Chain(object):
    def __init__(self, path=''): self._path = path
    def __getattr__(self, path):
        print(self._path, path)
        return Chain('%s/%s' % (self._path, path))  # 这对那种类里面没有的变量, 已经定义的变量不会调用
    def __str__(self): return self._path
    __repr__ = __str__  # 针对 >>> Chain().status 这种终端里面的调用, __str__ 是给用户看的, __repr__ 是给程序员看的
# 如果要写SDK, 给每个URL对应的API都写一个方法, 那得累死, 而且, API一旦改动, SDK也要改
print(Chain().status.user.timeline.list)  # 上一次的返回值会到下一次的 __init__
# print(Chain().users('michael').repos)  # 针对这种 GET /users/:user/repos API, 还没写出来
