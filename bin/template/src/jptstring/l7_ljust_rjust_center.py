#!/usr/bin/python3
# coding: utf-8
##################################################################
## ljust(width[, fillchar]) 即长度加占位符, 默认为空格, 这三种在格式化输出时用着非常方便
a = "Hello world"
# 默认是空格
print(a.rjust(12))  #  Hello world; 左侧会有一个空格, a 长度为 11, 12 - 11 = 1
print(a.ljust(12))  # Hello world ; 右侧一个空格
print(a.center(13))  #  Hello world ; 左右各一个空格

# 指定填充字符
print(a.rjust(13, '*'))  # **Hello world
print(a.ljust(13, '*'))  # Hello world**
print(a.center(13, '*'))  # *Hello world*

# 如果 width 小于字符串的长度, 则完整输出字符串
print(a.center(10, '*'))  # Hello world
##################################################################
## 格式化输出
print("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")
print('a'.ljust(10) + '15'.ljust(10) + '111'.ljust(10))
print('a'.ljust(10), '15'.ljust(10), '111'.ljust(10))  # 会错开几格
# 所以要用 +, 不能用 ,
