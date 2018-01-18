#!/usr/bin/python3
# coding: utf-8
##################################################################
## len()
print(len('ABC'), len('中文'))  # 3, 2; len() 计算 str 的字符数
print(len(b'ABC'), len('中文'.encode('utf-8')))  # 3, 6; 换成 bytes, len() 函数就计算字节数
##################################################################
## 对于单个字符的编码, Python 提供了 ord() 函数获取字符的整数表示, chr() 函数把编码转换为对应的字符
print(ord('A'), ord('中'))     # 65, 20013; ord() 只接受一个参数
print(chr(66), chr(25991))     # B, 文
print(hex(20013), hex(25991))  # 0x4e2d 0x6587
print(bin(2), int(0b10))       # 0b10 2
print([ord(i) for i in "中国"])  # [20013, 22269]
print('\u4e2d\u6587')  # 中文; 知道字符的整数编码, 还可以用十六进制
print(int('00001100111000', 2))  # 824; 要指定进制

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
## codecs.open() 进行文件的读取
# python 给我们提供了一个包 codecs 进行文件的读取, 这个包中的 open() 函数可以指定编码的类型
import codecs
f = codecs.open('./l5_dict_json.json', 'r+', encoding='utf-8')  # 必须事先知道文件的编码格式, 这里文件编码是使用的 utf-8
content = f.read()  # 如果 open 时使用的 encoding 和文件本身的 encoding 不一致的话, 那么这里将将会产生错误
# 可以看出 codecs 也很鸡肋...
print(codecs.BOM_UTF8)
##################################################################
## codecs.lookup() 验证是不是有效编码
print(codecs.lookup('utf8'))  # <codecs.CodecInfo object for encoding utf-8 at 0x13fb4f50828>; 有效
print(codecs.lookup('utf-;8'))  # <codecs.CodecInfo object for encoding utf-8 at 0x13fb4f50a08>; 有效
print(codecs.lookup('utf88'))  # unknown encoding: utf88; 无效
##################################################################
## codecs.encode()
print(codecs.encode("我能吞下玻璃而不伤害身体", "gb2312"))
print("我能吞下玻璃而不伤害身体".encode('gb2312'))  # 和上面一毛一样, 索引 codecs 很鸡肋...

##################################################################
## encoding python 支持的编码方式及其别名
from encodings.aliases import aliases
for k in aliases: print('%s: %s' % (k, aliases[k]))
