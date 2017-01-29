#!/usr/bin/python
# coding: utf-8
import os
# os.walk(), os.system(), os.path.join(), os.chdir(), os.getcwd(), os.listdir()
os.system('pwd')  # 执行 terminal 命令
print(os.getcwd())  # 得到当前路径
print(os.path.expanduser('~'))  # 当前家目录
for root, dirs, files in os.walk(os.getcwd()):  # 递归遍历当前目录
    print(root, dirs, files)  # 根据上面的语句决定, 所有目录的名字(没有为空), 所有文件的名字
    print([os.path.join(root, name) for name in dirs])  # 目录的绝对路径
    print([os.path.join(root, name) for name in files])  # 文件的绝对路径
    pass
print([d for d in os.listdir('.')])  # 当前路径下的所有文件和目录, 没有子目录
print(os.path.join('~', 'Pictures'))  # 专门生成路径的一个函数
os.chdir('/home/coder352/')  # 切换目录

import sys
print(sys.path)  # 当前 python 的模板路径
