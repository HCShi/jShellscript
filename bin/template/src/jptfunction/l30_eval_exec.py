#!/usr/bin/python3
# coding: utf-8
# exec 执行储存在字符串或文件中的 Python 语句; 例如, 我们可以在运行时生成一个包含 Python 代码的字符串, 然后使用 exec 语句执行这些语句
exec('print("Hello World")')  # Hello World
# eval 语句用来计算存储在字符串中的有效 Python 表达式
print(eval('2 * 3'))  # 6
