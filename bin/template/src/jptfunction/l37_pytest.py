#!/usr/bin/python3
# coding: utf-8
# 与 python 自带的 unittest 测试框架类似, 比 unittest 框架使用起来更简洁, 效率更高
def func(x): return x + 1
def test_func(): assert func(3) == 5  # 基本的断言语句 assert 来对结果进行验证
# py.test l37_pytest.py  # 进行测试; py.test 会在当前的目录下, 寻找以 test 开头的文件
