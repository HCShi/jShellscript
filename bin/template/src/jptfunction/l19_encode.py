#!/usr/bin/python3
# coding: utf-8
# 计算机内存统一使用 Unicode 编码, 当需要保存到硬盘或者需要传输的时候, 就转换为 UTF-8 编码, 读取时候从 UTF-8 转为 Unicode
# Python3 字符串是以 Unicode 编码的, 也就是说, Python 的字符串支持多语言
print('包含中文的 str')  # 原样输出

# 对于单个字符的编码, Python 提供了 ord() 函数获取字符的整数表示, chr() 函数把编码转换为对应的字符
print(ord('A'), ord('中'))     # 65, 20013, ord() 只接受一个参数
print(chr(66), chr(25991))     # B, 文
print(hex(20013), hex(25991))  # 0x4e2d 0x6587
print('\u4e2d\u6587')  # 中文, 知道字符的整数编码, 还可以用十六进制

# Python 的字符串类型是 str, 在内存中以 Unicode 表示, 一个字符对应若干个字节, 如果要在网络上传输, 或者保存到磁盘上
# 就需要把 str 变为以字节为单位的 bytes, Python 对 bytes 类型的数据用带 b 前缀的单引号或双引号表示
print(b'ABC')  # b'ABC', bytes 的每个字符都只占用一个字节, 只能表示 ASCII
# print(b'中文') # 会报错

# 相互转换
# 以 Unicode 表示的 str 通过 encode() 方法可以编码为指定的 bytes
print('ABC'.encode(), 'ABC'.encode('ascii'))    # b'ABC' b'ABC', encode() 默认会自己选择编码类型
print('中文'.encode(), '中文'.encode('utf-8'))  # b'\xe4\xb8\xad\xe6\x96\x87', 含有中文的 str 可以用 UTF-8 编码为 bytes
# 在 bytes 中, 无法显示为 ASCII 字符的字节, 用 \x## 显示
# 反过来, 如果我们从网络或磁盘上读取了字节流, 那么读到的数据就是 bytes, 要把 bytes 变为 str, 就需要用 decode() 方法
print(b'ABC'.decode(), b'ABC'.decode('ascii'))  # ABC ABC, decode() 默认也会选择编码类型
print(b'\xe4\xb8\xad'.decode(), b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中 中文
# 在操作字符串时, 我们经常遇到 str 和 bytes 的互相转换, 为了避免乱码问题, 应当始终坚持使用 UTF-8 编码对 str 和 bytes 进行转换

# len
print(len('ABC'), len('中文'))  # 3, 2, 计算的是 str 的字符数
print(len(b'ABC'), len('中文'.encode('utf-8')))  # 3, 6, 换成 bytes, len() 函数就计算字节数
