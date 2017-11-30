#!/usr/bin/python3
# coding: utf-8
##################################################################
## str.maketrans(intab, outtab]);
# 用于创建字符映射的转换表, 第一个参数是字符串, 表示需要转换的字符, 第二个参数也是字符串表示转换的目标
# 注: 两个字符串的长度必须相同, 为一一对应的关系
# Python3.4 已经没有 string.maketrans()了, 取而代之的是内建函数: bytearray.maketrans()、 bytes.maketrans()、 str.maketrans()
str_trantab = str.maketrans('abcd', '1234')
print(str_trantab, type(str_trantab))  # {97: 49, 98: 50, 99: 51, 100: 52} <class 'dict'>{97: 49, 98: 50, 99: 51, 100: 52}
test_str = "csdn blog: http://blog.csdn.net/wirelessqa"
print (test_str.translate(str_trantab))  # 3s4n 2log: http://2log.3s4n.net/wirelessq1
# 其实和 re 正则 差不多
##################################################################
## translate() 用法; ** 注意 str.translate() 不接受 None **
# 根据参数 table 给出的表(包含 256 个字符)转换字符串的字符, 要过滤掉的字符放到 del 参数中
# str.translate(table)                   # table -- 翻译表, 翻译表是通过 maketrans 方法转换而来
# bytes.translate(table[, delete])       # deletechars -- 字符串中要过滤的字符列表
# bytearray.translate(table[, delete])
print(b'http://www.csdn.net/wirelessqa'.translate(None, b'ts'))  # b'hp://www.cdn.ne/wireleqa'; 若 table 参数为 None, 则只删除不映射
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(type(bytes_tabtrans))  # <class 'bytes'>; 和 str.translate() 的 dict 不同, 也隐含了下面的 str.translate() 的不同
print(b'http://www.csdn.net/wirelessqa'.translate(bytes_tabtrans, b'ts'))  # b'HP://WWW.CDN.NE/WIRELEQA'; 若 table 参数不为 NONE, 则先删除再映射

# str.translate requires a dict that maps unicode ordinals to other unicode oridinals (or None if you want to remove the character).
s = "this is string example....wow!!!"
print(s.translate(str.maketrans('abc', '123')))  # this is string ex1mple....wow!!!
# print(s.translate(None, 'ts'))  # 会报错, 用下面的方法
table = {ord(char): None for char in 'ts'}
print(s.translate(table))  # hi i ring example....wow!!!
