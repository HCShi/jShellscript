#!/usr/bin/python3
# coding: utf-8
import pickle
a, b, c = 1, [1, 2], {'a':'jia', 'b':'rui'};
print(type(a), type(b), type(c))  # <class 'int'> <class 'list'> <class 'dict'>
with open('tmp.pkl', 'wb') as f: pickle.dump([a, b, c], f)
##################################################################
## 再次读取可以保持原来的数据结构...
with open('tmp.pkl', 'rb') as f: a, b, c = pickle.load(f)
print(type(a), type(b), type(c))  # <class 'int'> <class 'list'> <class 'dict'>
