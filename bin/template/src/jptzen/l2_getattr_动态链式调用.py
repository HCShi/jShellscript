#!/usr/bin/python3
# coding: utf-8
class Chain(object):
    def __init__(self, path=''): self._path = path
    def __getattr__(self, path): return Chain('%s/%s' % (self._path, path))
    def __str__(self): return self._path
    __repr__ = __str__  # 针对 >>> Chain().status 这种终端里面的调用
# 如果要写SDK, 给每个URL对应的API都写一个方法, 那得累死, 而且, API一旦改动, SDK也要改
print(Chain().status.user.timeline.list)
# print(Chain().users('michael').repos)  # 针对这种 GET /users/:user/repos API, 还没写出来
