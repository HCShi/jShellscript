#!/usr/bin/python3
# coding: utf-8
# 这个估计不会用到， forever...
# 以下函数用于对 dtype 为 numpy.string_ 或 numpy.unicode_ 的数组执行向量化字符串操作; 基于 Python 内置库中的标准字符串函数
# 这些函数在字符数组类 (numpy.char) 中定义;较旧的 Numarray 包包含 chararray 类; numpy.char 类中的上述函数在执行向量化字符串操作时非常有用
import numpy as np
##################################################################
# numpy.char.add(); 函数执行按元素的字符串连接
print(np.char.add(['hello'], [' xyz']))  # ['hello xyz']; 连接两个字符串
print(np.char.add(['hello', 'hi'], [' abc', ' xyz']))  # ['hello abc' 'hi xyz']; 连接示例
##################################################################
# numpy.char.multiply(); 这个函数执行多重连接
print(np.char.multiply('Hello ', 3))  # fHello Hello Hello
##################################################################
# numpy.char.center(); 返回所需宽度的数组, 以便输入字符串位于中心, 并使用 fillchar 在左侧和右侧进行填充
print(np.char.center('hello', 20, fillchar='*'))  # *******hello********
##################################################################
# numpy.char.capitalize(); 函数返回字符串的副本, 其中第一个字母大写
print(np.char.capitalize('hello world'))  # Hello world
##################################################################
# numpy.char.title() 返回输入字符串的按元素标题转换版本, 其中每个单词的首字母都大写
print(np.char.title('hello how are you?'))  # Hello How Are You?
##################################################################
# numpy.char.lower(); 函数返回一个数组, 其元素转换为小写, 它对每个元素调用 str.lower
print(np.char.lower(['HELLO', 'WORLD']))  # ['hello' 'world']
print(np.char.lower('HELLO'))  # hello
##################################################################
# numpy.char.upper(); 函数返回一个数组, 其元素转换为大写, 它对每个元素调用 str.upper
print(np.char.upper('hello'))  # HELLO
print(np.char.upper(['hello', 'world']))  # ['HELLO' 'WORLD']
##################################################################
# numpy.char.split(); 此函数返回输入字符串中的单词列表; 默认情况下, 空格用作分隔符; 否则, 指定的分隔符字符用于分割字符串
print(np.char.split('hello how are you?'))  # ['hello', 'how', 'are', 'you?']
print(np.char.split('TutorialsPoint,Hyderabad,Telangana', sep=','))  # ['TutorialsPoint', 'Hyderabad', 'Telangana']
##################################################################
# numpy.char.splitlines(); 函数返回数组中元素的单词列表, 以换行符分割; '\n', '\r', '\r\n' 都会用作换行符
print(np.char.splitlines('hello\nhow are you?'))  # ['hello', 'how are you?']
print(np.char.splitlines('hello\rhow are you?'))  # ['hello', 'how are you?']
##################################################################
# numpy.char.strip()  # 函数返回数组的副本, 其中元素移除了开头或结尾处的特定字符
print(np.char.strip('ashok arora', 'a'))  # shok aror
print(np.char.strip(['arora', 'admin', 'java'], 'a'))  # ['ror' 'dmin' 'jav']
##################################################################
# numpy.char.join(); 这个函数返回一个字符串, 其中单个字符由特定的分隔符连接
print(np.char.join(':', 'dmy'))  # d:m:y
print(np.char.join([':', '-'], ['dmy', 'ymd']))  # ['d:m:y' 'y-m-d']
##################################################################
# numpy.char.replace() 这个函数返回字符串副本, 其中所有字符序列的出现位置都被另一个给定的字符序列取代
print(np.char.replace ('He is a good boy', 'is', 'was'))  # He was a good boy
##################################################################
# numpy.char.decode(); 这个函数在给定的字符串中使用特定编码调用 str.decode()
a = np.char.encode('hello', 'cp500'); print(a)  # \x88\x85\x93\x93\x96
print(np.char.decode(a, 'cp500'))  # hello
##################################################################
# numpy.char.encode(); 对数组中的每个元素调用 str.encode 函数; 默认编码是 utf_8, 可以使用标准 Python 库中的编解码器
a = np.char.encode('hello', 'cp500'); print(a)  # \x88\x85\x93\x93\x96
