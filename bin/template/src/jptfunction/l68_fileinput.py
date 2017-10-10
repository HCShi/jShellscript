#!/usr/bin/python3
# coding: utf-8
import fileinput
f = open('tmp', 'w'); f.flush(); f.write('jrp\n hello\n world\n china'); f.close()
f = open('tmp_2', 'w'); f.flush(); f.write('jrp\n hello\n world\n china'); f.close()
##################################################################
## 1. 基本方式
for line in fileinput.input('./tmp'): print(line)  # 迭代读取文件, 对大文件友好
for line in fileinput.input('./tmp_2'): print(fileinput.filename(), '|', 'Line Number:', fileinput.lineno(), '|: ', line)  # 格式化输出
##################################################################
## 2. 多文件操作
for line in fileinput.input(('./tmp', './tmp_2')): print(line)  # 按顺序读完一个接着另一个
fileinput.close()
##################################################################
## 总结:
# 1. fileinput 模块可以对一个或多个文件中的内容进行迭代、遍历等操作
#    input() 函数有点类似文件 readlines() 方法, 区别在于:
#    前者是一个迭代对象, 即每次只生成一行, 需要用 for 循环迭代, 后者是一次性读取所有行
#    在碰到大文件的读取时, fileinput.input() 无疑效率更高效
#    用 fileinput 对文件进行循环遍历, 格式化输出, 查找、替换等操作, 非常方便
# 2. fileinput 模块提供处理一个或多个文本文件的功能, 可以通过使用 for 循环来读取一个或多个文本文件的所有行
#    它的工作方式和 readlines 很类似, 不同点在于它不是将全部的行读到列表中而是创建了一个 xreadlines 对象
# 3. 常用函数
#    fileinput.input()        # 返回能够用于 for 循环遍历的对象
#    fileinput.filename()     # 返回当前文件的名称
#    fileinput.lineno()       # 返回当前已经读取的行的数量 (或者序号)
#    fileinput.filelineno()   # 返回当前读取的行的行号
#    fileinput.isfirstline()  # 检查当前行是否是文件的第一行
#    fileinput.isstdin()      # 判断最后一行是否从 stdin 中读取
#    fileinput.close()        # 关闭队列
