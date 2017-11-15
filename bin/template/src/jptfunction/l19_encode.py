#!/usr/bin/python3
# coding: utf-8  # Python3 中可以不用这句话
# 编码(动词): 按照某种规则(这个规则称为: 编码(名词))将"文本"转换为"字节流". 而在 python3 中则表示: unicode 变成 str
# 解码(动词): 将"字节流"按照某种规则转换成"文本".                           而在 python3 中则表示: str 变成 unicode

# 字符串在 Python 内部的表示是 Unicode 编码, 因此, 在做编码转换时, 通常需要以 Unicode 作为中间编码,
#     即先将其他编码的字符串解码(decode)成 Unicode, 再从 Unicode 编码(encode)成另一种编码
# 在新版本的 python3 中, 取消了 unicode 类型, 代替它的是使用 unicode 字符的字符串类型 (str),
#     字符串类型 (str) 成为基础类型如下所示, 而编码后的变为了字节类型 (bytes) 但是两个函数的使用方法不变:
#       decode               encode
# bytes ------> str(unicode) ------> bytes
u = '中文'; print(u, type(u))  # 中文 <class 'str'>;                                     指定字符串类型对象 u
str = u.encode('gb2312'); print(str, type(str))   # b'\xd6\xd0\xce\xc4' <class 'bytes'>; 以 gb2312 编码对 u 进行编码, 获得 bytes 类型对象 str
u1 = str.decode('gb2312'); print(u1, type(u1))  # 中文 <class 'str'>;                    以 gb2312 编码对字符串 str 进行解码, 获得字符串类型对象 u1
u2 = str.decode('utf-8'); print(u2, type(u2))   # Error;                                 以 utf-8 的编码对 str 进行解码得到的结果, 将无法还原原来的字符串内容
# 但是 ascii 编码的可以用 'utf-8' 或这 'gb2312' 解码, 因为默认都兼容 ascii
##################################################################
## Python 的字符串类型是 str, 在内存中以 Unicode 表示, 一个字符对应若干个字节, 如果要在网络上传输, 或者保存到磁盘上
# 就需要把 str 变为以字节为单位的 bytes, Python 对 bytes 类型的数据用带 b 前缀的单引号或双引号表示
print(b'ABC')  # b'ABC'; bytes 的每个字符都只占用一个字节, 只能表示 ASCII
print(b'中文')  # 会报错
##################################################################
## encode(encoding='utf-8'), decode(encoding='utf-8') 相互转换
# 以 Unicode 表示的 str 通过 encode() 方法可以编码为指定的 bytes
print('ABC'.encode(), 'ABC'.encode('ascii'))    # b'ABC' b'ABC'; encode() 默认会自己选择编码类型
print('中文'.encode(), '中文'.encode('utf-8'))  # b'\xe4\xb8\xad\xe6\x96\x87'; 含有中文的 str 可以用 UTF-8 编码为 bytes
# 在 bytes 中, 无法显示为 ASCII 字符的字节, 用 \x## 显示, 第一个字节小于 \x80, 则仍然表示 ASCII 字符; \x80 以上, 跟下后面字节一起(2/3 个字节)表示
# 反过来, 如果我们从网络或磁盘上读取了字节流, 那么读到的数据就是 bytes, 要把 bytes 变为 str, 就需要用 decode() 方法
print(b'ABC'.decode(), b'ABC'.decode('ascii'))  # ABC ABC; decode() 默认也会选择编码类型
print(b'\xe4\xb8\xad'.decode(), b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中 中文
# 在操作字符串时, 我们经常遇到 str 和 bytes 的互相转换, 为了避免乱码问题, 应当始终坚持使用 UTF-8 编码对 str 和 bytes 进行转换
u = 'hello'
str = u.encode('utf-8')    # 转换为 utf-8 编码的字符串 str
str1 = u.encode('gbk')     # 转换为 gbk 编码的字符串 str1
str1 = u.encode('utf-16')  # 转换为 utf-16 编码的字符串 str1
##################################################################
## 避免不了的文件读取问题: 因为存储时用 Unicode 太占空间; 默认是用 utf-8 存储
# 计算机内存统一使用 Unicode 编码, 当需要保存到硬盘或者需要传输的时候, 就转换为 UTF-8 编码, 读取时候从 UTF-8 转为 Unicode
# 在硬盘里存储的是 \xdd 之类的, 但是我们看不到, 我们能看到的都是内存中通过 \udddd 来表达的字符
# 假如我们读取一个文件, 文件保存时, 使用的编码格式, 决定了我们从文件读取的内容的编码格式, 例如, 我们从记事本新建一个文本文件 test.txt,
#   编辑内容, 保存的时候注意, 编码格式是可以选择的, 例如我们可以选择 gb2312, 那么使用 python 读取文件内容, 方式如下:
f = open('./l5_dict_json.json', 'rb')      # 以 bytes 格式读入
s = f.read(); print(s, type(s))            # <class 'bytes'>; 读取文件内容, 如果是不识别的 encoding 格式(识别 encoding 类型跟使用的系统有关), 这里将读取失败
import chardet
print(chardet.detect(s))                   # {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
u = s.decode('gb2312'); print(u, type(u))  # <class 'str'>;   假设文件保存时以 gb2312 编码保存; 以文件保存格式对内容进行解码, 获得 unicode 字符串
u = s.decode(); print(u, type(u))          # <class 'str'>;   假设文件保存时以 gb2312 编码保存; 以文件保存格式对内容进行解码, 获得 unicode 字符串
# 因为是以 ascii 编码, 所以用 gb2312 解码也不会报错(兼容); 但用 gb2312 编码的文件用 utf-8 解码会报错, 见上面...
##################################################################
## json.dumps() 有坑 !!!
# python 中的字符串分普通字符串和 unicode 字符串, 一般从数据库中读取的字符串会自动被转换为 unicode 字符串
import json
obj={"name":"测试"}
dump_obj = json.dumps(obj)
print(type(obj), obj)            # <class 'dict'> {'name': '测试'}
print(type(str(obj)), str(obj))  # <class 'str'> {'name': '测试'};         str 和 没有前导 b 都能说明是以 unicode 形式存储
print(type(dump_obj), dump_obj)  # <class 'str'> {"name": "\u6d4b\u8bd5"}, 内容包含了 unicode 字符串的整数表示...
print(dump_obj.encode())         # b'{"name": "\\u6d4b\\u8bd5"}';          因为都是 ascii, 所以再次编码没什么用了...
print(str(obj).encode())         # b"{'name': '\xe6\xb5\x8b\xe8\xaf\x95'}"; 读取文件时可以识别这种的
# .encode() 模拟存储到磁盘的过程, 结果就是磁盘存放的, 从磁盘上读取时并不能将其进行正确的转化, 所以用 vim 打开文件会显示 {"name": "\\u6d4b\\u8bd5"}
dump_obj = json.dumps(obj, ensure_ascii=False)
print(dump_obj.encode())  # b'{"name": "\xe6\xb5\x8b\xe8\xaf\x95"}'

##################################################################
## 总结
# 1. 查看一个字符串是否是普通字符串, 只要打印一下, 普通字符串会带 b'
# 2. json.dumps() 和 str() 区别是 单双引号的区别, 单引号是 YAML 格式用的...
