#!/usr/bin/python3
# coding: utf-8
a = [1, 2, 3, 4]
##################################################################
## slice
print(a[0:2])  # [1, 2]; 左闭右开
print(a[0:4])  # [1, 2, 3, 4]
# print(a[4])  # list index out of range

print(a[-2:])     # [3, 4]
print(a[-2::])    # [3, 4]
print(a[-2::-1])  # [3, 2, 1]; 第三个参数是步长; -1 表示逆序
print(a[-2::-2])  # [3, 1]
print(list(range(10))[::2])  # [0, 2, 4, 6, 8]; 隔一个取一次
print(list(range(10))[::5])  # [0, 5]; 隔五个取一次
##################################################################
## 高级应用
a = [1, 2, 3, 4, 5]; print(a[:3][::-1])  # [3, 2, 1]
a = 'abcdcbaqwer'; print(a[:7] == a[:7][::-1])  # True; 判断是否是回文...
