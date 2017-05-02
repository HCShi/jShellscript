#!/usr/bin/python3
# coding: utf-8
dic = {'a': 123}
##################################################################
# Method 1th:
##################################################################
with open('tmp', 'w') as f:  # will auto run close(), so you don not need to type f.close
    f.write('hello')  # will be covered
    f.write(str(dic))  # must change the type of argument
    # print(f.read())  # Error: io.UnsupportedOperation: not readable
with open('tmp') as f:  # defaut is 'r'
    print(f.read())

##################################################################
# Method 2ed:
##################################################################
f = open('tmp', 'w')
f.write('jrp')
# print(f.read())  # Error: io.UnsupportedOperation: not readable
f = open('tmp', 'a')  # write and append
f.write('dr')
f = open('tmp')
# f.write('jrp')  # Error: io.UnsupportedOperation: not readable
print(f.read())  # 把整个文件打印出来
for i in f.read(): print(i)  # 把每个字符打印出来
for i in f.readlines(): print(i)  # 打印每一行
for i in f.readline(): print(i)  # 还是打印每个字符
