#!/usr/bin/python3
# coding: utf-8
dic = {'a': 123}
##################################################################
# Method 1th:
with open('tmp', 'w') as f:  # will auto run close(), so you don not need to type f.close
    f.write('hello\n')  # will be covered
    f.write(str(dic))  # must change the type of argument
    # print(f.read())  # Error: io.UnsupportedOperation: not readable
with open('tmp') as f:  # defaut is 'r'
    raw = f.read(); print(raw )  # hello\n {'a': 123}; 和 request.urlopen(url).read() 效果相同
    print(type(raw), len(raw))  # <class 'str'> 16; 读出来是以 字符 为单位存储
with open('tmp') as f:  # defaut is 'r'
    raw = f.readlines(); print(raw )  # ['hello\n', "{'a': 123}"];
    print(type(raw), len(raw))  # <class 'list'> 2
##################################################################
# Method 2ed:
f = open('tmp', 'w')
f.write('jrp')
# print(f.read())  # Error: io.UnsupportedOperation: not readable
f = open('tmp', 'a')  # write and append
f.write('dr')
f = open('tmp')
# f.write('jrp')  # Error: io.UnsupportedOperation: not readable
print(f.read())  # 把整个文件打印出来
for i in f.read(): print(i)  # 把每个字符打印出来; 下面几个要重新去打开文件, 因为指针已经到末尾了
for i in f.readlines(): print(i)  # 打印每一行
for i in f.readline(): print(i)  # 还是打印每个字符
##################################################################
## Method 3rd: 打开就直接可以了, 相当于 readlines()
open('tmp', 'w').write('jrp\nhello\nworld\n14thcoder\ncoder352\n')
print([line for line in open('tmp')])  # ['jrp\n', 'hello\n', 'world\n', '14thcoder\n', 'coder352\n']
print([line.strip() for line in open('tmp')])  # ['jrp', 'hello', 'world', '14thcoder', 'coder352']
print([line.strip() for line in open('tmp').readlines()])  # ['jrp', 'hello', 'world', '14thcoder', 'coder352']
##################################################################
## 总结:
# 读文件
# 1. open(file).read(); read() 是以字符为单位, 和网络数据扒取 request.urlopen(url).read() 处理效果相同
# 2. open(file).readlines(); 默认就是 readlines() 方法, 所以可以直接写 open(file), 返回以行为单位的 list

# 写文件
