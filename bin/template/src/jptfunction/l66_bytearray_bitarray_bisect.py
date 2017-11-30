#!/usr/bin/python3
# coding: utf-8
##################################################################
## bytearray([source [, encoding [, errors]]]) 返回一个 byte 数组; Bytearray 类型是一个可变的序列, 并且序列中的元素的取值范围为 [0, 255]
## source 为整数, 则返回一个长度为 source 的初始化数组
a = bytearray(3); print(a, a[0], a[1], a[2])  # bytearray(b'\x00\x00\x00') 0 0 0
## source 为字符串, 则按照指定的 encoding 将字符串转换为字节序列
b = bytearray("abc".encode()); print(b, b[0], b[1], b[2])   # bytearray(b'abc') 97 98 99; 这里一定要加 .encode()
## source 为可迭代类型, 则元素必须为 [0, 255] 中的整数
c = bytearray([1, 2, 3]); print(c, c[0], c[1], c[2])  # bytearray(b'\x01\x02\x03') 1 2 3

## append(item, /) Append a single item to the end of the bytearray.
b = bytearray(); text = '0000000011111111'
for i in range(0, len(text), 8): b.append(int(text[i:i+8], 2))  # 2 进制转换为 10 进制
print(b)  # bytearray(b'\x00\xff')

## 写文件, 将 010101 的二进制串以 byte 方式写入文件, jptalgorithm/Huffman 中会使用
b = bytearray(); encoded_text = '0101010101010101'  # encode_text 要是 8 的倍数
for i in range(0, len(encoded_text), 8): b.append(int(encoded_text[i:i+8], 2))  # 2 进制转换为 10 进制
print(b, b.decode())  # bytearray(b'UU') UU; 这里用 bytearray 不能将 ASCII 转换会 二进制字符串了
# 另一种方法
open('tmp.bin', 'w').write(''.join(chr(int(encoded_text[i*8:i*8+8], 2)) for i in range(len(encoded_text)//8)))
print(open('./tmp.bin').read())  # UU
print(''.join([bin(ord(byte))[2:].zfill(8) for byte in open('./tmp.bin').read()]))  # 0101010101010101; jptstring/l*_format*.py 中介绍了很多种方法
##################################################################
## bitarray
from bitarray import bitarray
a = bitarray(10); print(a)  # 初始化一个有 10 个 bit 位的数组, 初始值为 bitarray('0110100000')
a[1:8] = 1; print(a)  # 可以像操作 list 一样操作 bitarray 对象
if not a.all(): print("not all bits are True.")  # 当 bitarray 中所有的元素都为 1 时, all() 返回为 True

# 将 bitarray 转换为 string
tmp = bitarray('1001'); print(tmp)  # bitarray('1001')
print(tmp.to01())  # 1001
print(tmp.tobytes())  # b'\x90'
print(tmp.tolist())  # [True, False, False, True]

## encode(codedict, iterable) Huffman 加解码
# Given a prefix code (a dict mapping symbols to bitarrays), iterates over iterable object with symbols, and extends the bitarray with the corresponding bitarray for each symbols.
huffman_dict = {'!': bitarray('01110'), 'B': bitarray('01111'), 'l': bitarray('10100'), 'y': bitarray('10111')}  # 必须用 bitarray('1000') 作为值
a = bitarray(); a.encode(huffman_dict, 'Bylly!'); print(a)  # bitarray('011111011110100101001011101110')
dec = bitarray('011111011101110').decode(huffman_dict); print(''.join(dec))  # By!
# 上面的 a 没有简单的方式, a = bitarray()encode(huffman_dict, 'Bylly!'); 这样不行

## Huffman 编解码, 和上面实现了相同的功能, 但比较容易理解, 后来发现不实用, 递归太深
def huffmanDecode (dictionary, text):
    if not text: return ""  # 这里的退出条件很重要
    k = next(k for k in dictionary if text.startswith(k))
    return dictionary[k] + huffmanDecode(dictionary, text[len(k):])
print(huffmanDecode({'a': '001', 'b': '111'}, 'ab'))  # 001111
print(huffmanDecode({'001': 'a', '111': 'b'}, '001111'))  # ab
# RecursionError: maximum recursion depth exceeded; 这种方法递归太深了, 对于大文件是不行的
##################################################################
## bisect 排序模块; 使用这个模块以前确定是已经排好序的...
import bisect
## sort() 对原数据进行排序, 会修改原始数据
data = [4, 2, 9, 7]
data.sort(); print(data)  # [2, 4, 7, 9];

## insort() 插入结果不影响原有排序
bisect.insort(data, 3); print(data)  # [2, 3, 4, 7, 9]

## bisect() 其目的在于查找该数值将会插入的位置并返回, 而不会插入
print(bisect.bisect(data, 1))  # 0;
print(data)  # [2, 3, 4, 7, 9]

## bisect_left() 和 bisect_right() 该函数用入处理将会插入重复数值的情况, 返回将会插入的位置
print(bisect.bisect_left(data, 4))  # 2
print(bisect.bisect_right(data, 4))  # 3
print(data)  # [2, 3, 4, 7, 9]

## insort_left() 和 insort_right() 对应的插入函数
bisect.insort_left(data, 4); print(data)  # [2, 3, 4, 4, 7, 9]
data = [2, 3, 4, 7, 9]
bisect.insort_right(data, 4); print(data)  # [2, 3, 4, 4, 7, 9]
# 可见, 单纯看其结果的话, 两个函数的操作结果是一样的, 其实插入的位置不同而已
