#!/usr/bin/python3
# coding: utf-8  # Python3 中可以不用这句话
# 计算机内存统一使用 Unicode 编码, 当需要保存到硬盘或者需要传输的时候, 就转换为 UTF-8 编码, 读取时候从 UTF-8 转为 Unicode
# Python3 字符串是以 Unicode 编码的, 也就是说, Python 的字符串支持多语言
# str <-> char; utf-8 <-> ascii; 普通字符串 <-> Unicode 字符串
# unicode 在 Python 中不是一种编码方式, 所以 unicode 字符串没有解码为普通字符串的方法, 只有编码 .encode() 的方法; 普通字符串有解码为 unicode 的方法 str()
us, s = u'包含中文的 str', '包含中文的 str'; print(us, s)  # 包含中文的 str; 结果是一样的
print(type(us), type(s))  # <class 'str'> <class 'str'>; 在 Python2 中 前一个回事 <class 'unicode'>, Python3 中统一了, str 使用 unicode 编码
# 我们能看到中文, 并且打印出来, 是因为在 .py 文件中以 utf-8 存储, vim 打开的时候尝试用 utf-8 打开 转换成 Unicode 放入内存, 再显示出来
# 在硬盘里存储的是 \xdd 之类的, 但是我们看不到, 我们能看到的都是内存中通过 \udddd 来表达的字符
##################################################################
## 对于单个字符的编码, Python 提供了 ord() 函数获取字符的整数表示, chr() 函数把编码转换为对应的字符
print(ord('A'), ord('中'))     # 65, 20013; ord() 只接受一个参数
print(chr(66), chr(25991))     # B, 文
print(hex(20013), hex(25991))  # 0x4e2d 0x6587
print([ord(i) for i in "中国"])  # [20013, 22269]
print('\u4e2d\u6587')  # 中文; 知道字符的整数编码, 还可以用十六进制
##################################################################
## Python 的字符串类型是 str, 在内存中以 Unicode 表示, 一个字符对应若干个字节, 如果要在网络上传输, 或者保存到磁盘上
# 就需要把 str 变为以字节为单位的 bytes, Python 对 bytes 类型的数据用带 b 前缀的单引号或双引号表示
print(b'ABC')  # b'ABC'; bytes 的每个字符都只占用一个字节, 只能表示 ASCII
# print(b'中文') # 会报错
##################################################################
## 相互转换
# 以 Unicode 表示的 str 通过 encode() 方法可以编码为指定的 bytes
print('ABC'.encode(), 'ABC'.encode('ascii'))    # b'ABC' b'ABC'; encode() 默认会自己选择编码类型
print('中文'.encode(), '中文'.encode('utf-8'))  # b'\xe4\xb8\xad\xe6\x96\x87'; 含有中文的 str 可以用 UTF-8 编码为 bytes
# 在 bytes 中, 无法显示为 ASCII 字符的字节, 用 \x## 显示, 第一个字节小于 \x80, 则仍然表示 ASCII 字符; \x80 以上, 跟下后面字节一起(2/3 个字节)表示
# 反过来, 如果我们从网络或磁盘上读取了字节流, 那么读到的数据就是 bytes, 要把 bytes 变为 str, 就需要用 decode() 方法
print(b'ABC'.decode(), b'ABC'.decode('ascii'))  # ABC ABC; decode() 默认也会选择编码类型
print(b'\xe4\xb8\xad'.decode(), b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中 中文
# 在操作字符串时, 我们经常遇到 str 和 bytes 的互相转换, 为了避免乱码问题, 应当始终坚持使用 UTF-8 编码对 str 和 bytes 进行转换
##################################################################
## len
print(len('ABC'), len('中文'))  # 3, 2; 计算的是 str 的字符数
print(len(b'ABC'), len('中文'.encode('utf-8')))  # 3, 6; 换成 bytes, len() 函数就计算字节数
##################################################################
## 普通字符串 Vs Unicode 字符串; 两种字符串之间的转换, 普通字符串包含好几种, 但都是以 b'' 开头
import chardet
# 将 Unicode 转化为普通 Python 字符串: .encode()
unicodestr = u"He 你好"  # 在 Python3 中 不加 u 默认就是 Unicode
utf8str = unicodestr.encode(); print(chardet.detect(utf8str), type(utf8str), utf8str)              # 'utf-8' <class 'bytes'> b'He \xe4\xbd\xa0\xe5\xa5\xbd'
utf16str = unicodestr.encode("utf-16"); print(chardet.detect(utf16str), type(utf16str), utf16str)  # 'UTF-16' <class 'bytes'> b'\xff\xfeH\x00e\x00 \x00`O}Y'
unicodestr = u"He"  # 因为中文没有 ascii 和 ISO-8859, 所以这里不含中文
asciistr = unicodestr.encode("ascii"); print(chardet.detect(asciistr), type(asciistr), asciistr)  # 'ascii' <class 'bytes'> b'He'
isostr = unicodestr.encode("ISO-8859-1"); print(chardet.detect(isostr), type(isostr), isostr)     # 'ascii' <class 'bytes'> b'He'
# 将普通 Python 字符串转化为 Unicode: str(); decode 在 Python3 中是 str(), 在 Python2 中是 unicode()
# plainstr1 = str(utf8str, "utf-8"); print(chardet.detect(plainstr1), plainstr1)  # <class 'str'> 不能用 chardet, 因为没有进行编码
plainstr1 = str(utf8str, "utf-8"); print(type(plainstr1), plainstr1)      # <class 'str'> He 你好; 括号中的参数都不能省略
plainstr2 = str(utf16str, "utf-16"); print(type(plainstr2), plainstr2)    # <class 'str'> He 你好
plainstr3 = str(asciistr, "ascii"); print(type(plainstr3), plainstr3)     # <class 'str'> He
plainstr4 = str(isostr, "ISO-8859-1"); print(type(plainstr4), plainstr4)  # <class 'str'> He
assert plainstr1 == plainstr2
assert plainstr3 == plainstr4
##################################################################
## json.dumps() 有坑 !!!
# python 中的字符串分普通字符串和 unicode 字符串, 一般从数据库中读取的字符串会自动被转换为 unicode 字符串
import json
obj={"name":"测试"}
dump_obj = json.dumps(obj)
print(type(obj), obj)  # <class 'dict'> {'name': '测试'}
print(type(str(obj)), str(obj))  # <class 'str'> {'name': '测试'}; str 和 没有前导 b 都能说明是以 unicode 形式存储
print(type(dump_obj), dump_obj)  # <class 'str'> {"name": "\u6d4b\u8bd5"}, 内容包含了 unicode 字符串的整数表示...
print(dump_obj.encode())  # b'{"name": "\\u6d4b\\u8bd5"}'; 因为都是 ascii, 所以再次编码没什么用了...
print(str(obj).encode())  # b"{'name': '\xe6\xb5\x8b\xe8\xaf\x95'}"; 读取文件时可以识别这种的
# .encode() 模拟存储到磁盘的过程, 结果就是磁盘存放的, 从磁盘上读取时并不能将其进行正确的转化, 所以用 vim 打开文件会显示 {"name": "\\u6d4b\\u8bd5"}
dump_obj = json.dumps(obj, ensure_ascii=False)
print(dump_obj.encode())  # b'{"name": "\xe6\xb5\x8b\xe8\xaf\x95"}'
##################################################################
## 总结
# 1. 查看一个字符串是否是普通字符串, 只要打印一下, 普通字符串会带 b'
# 2. json.dumps() 和 str() 区别是 单双引号的区别, 单引号是 YAML 格式用的...
