#!/usr/bin/python3
# coding: utf-8
import random, string
random.seed(10)
##################################################################
## 实际应用
# ascii_letters 包含 大写和小写 的26个英文字母, 不包含数字及其它的字符
print(''.join(random.sample(string.ascii_letters, 4)))  # KcBE
print(''.join(random.sample(string.ascii_letters + string.digits + '()`~!@#$%^&*-+=|\'{}[]:;"<>,.?/', 4)))  # 这样就更像密码了
print(''.join(random.choice(string.ascii_uppercase + string.digits)))  # 只能生成一个
print(''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(10)))  # 新添的控制长度
# 去掉标点; 还可以用 str.translate() 来实现
print(string.punctuation)  # 所有标点符号
mess = 'Sample message! Notice: it has punctuation'
nopunc = ''.join([char for char in mess if char not in string.punctuation]); print(nopunc)  # 去掉标点!!!
##################################################################
## string 各种属性 和 方法
print(type(string.ascii_uppercase))  # <class 'str'>; 返回值可迭代
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.digits)  # 0123456789
print(string.hexdigits)  # 0123456789abcdefABCDEF
print(string.octdigits)  # 01234567
print(string.printable)  # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ ^N
print(string.whitespace)  # ^N; 和奇葩的一些字符

print(string.capwords('hello world!'))  # Hello World!; 首字母大写
