#!/usr/bin/python3
# coding: utf-8
a = [1, 2, 3, 4]
print(a[-2:])     # [3, 4]
print(a[-2::])    # [3, 4]
print(a[-2::-1])  # [3, 2, 1]; 第三个参数是步长
print(a[-2::-2])  # [3, 1]
