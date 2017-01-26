#!/usr/bin/python
# coding: utf-8
lis = ['中国', u'是', u'\u6ce8\u91ca', '好的', u'你', u'\u6ce8\u91ca', '7', '8']  # u 强制类型转化为 Unicode, 否则为第二行指定的编码

# 类型转换
print tuple(lis), list(tuple(lis))
tmp_lis = [(u'a', u'b'), (u'c', u'd')]; print tmp_lis  # [(u'a', u'b'), (u'c', u'd')]
print [(a.encode('utf-8'), b.encode('utf-8')) for (a, b) in tmp_lis]  # [('a', 'b'), ('c', 'd')]

# list 格式化输出
for a, b, c in zip(lis[::3], lis[1::3], lis[2::3]):  # 不足的是最后面的可能不是整倍数
    print '{:<10}{:<10}{:<}'.format(a, b.encode('utf-8'), c.encode('utf-8'))  # 每行 3 个打印, format 只支持 utf-8(str)
import sys, pprint  # 另一种自动格式化的输出方法
pprint.pprint(sys.path, indent=4)
st = pprint.pformat(sys.path)  # 将 pprint 的输出重定向到变量

# 编码, python 内部使用的是 unicode 编码, 常见的有 gbk, gb2312, utf8
# 默认代码文件当作 ascii, 所以有 coding: utf-8, 然后转为 unicode
print lis  # ['\xe4\xb8\xad\xe5\x9b\xbd', u'\u662f', u'\u6ce8\u91ca'], 非 ascii 在 list dict 对象中的存储方式
print lis[0], lis[1], lis[2]  # 中国 是 注释, 单个打印是正常的, 因为已经不是 list 对象了
# 因为 Linux 的终端环境默认是 utf-8, 所以 lis[0] 不会乱码, 而 unicode 会自动转码
print type(lis[0]), type(lis[1]), type(lis[2])  # str, unicode, unicode
print type(lis[1].encode('utf-8'))  # str, 将 unicode 类型转化为 utf-8(str)
# decode 将普通字符串按照参数中的编码格式进行解析, 然后生成对应的 unicode 对象,
# 比如在这里我们代码用的是 utf-8, 那么把一个字符串转换为 unicode对象 就是如下三种形式:
# s = '哈'.decode('utf-8') 或 unicode('哈', 'utf-8') 以及 u'哈'
print repr('中国')  # 查看存储方式
import chardet; print chardet.detect('中国')  # 查看编码, str 对象又很多编码, unicode 是对象, 不是 str 的编码
import sys; print sys.stdin.encoding  # 输出当前的编码格式

# 输入和输出
# open('txt').read() 读入的是以文件的编码存储, 当前代码文件以 codeing 指定的存储
# Python 控制台输出 unicode 对象自动根据输出环境的编码进行转换, 如果是普通字符串, 则会直接按照字符串的编码输出字符串

# 结论:
# 1. list, dict 中的是存储方式, 不是乱码
# 2. 乱码可以用 chardet 查看类型, 然后用 decode().encode() 通过 unicode 转成想要的
# 3. str 和 unicode 都是对象, str 对象可以有很多类型的编码方式(unicode 不是编码方式)
