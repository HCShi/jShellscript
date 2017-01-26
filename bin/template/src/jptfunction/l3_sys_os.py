#!/usr/bin/python
# coding: utf-8
import os
# os.walk(), os.system(), os.path.join(), os.chdir()
os.system('pwd')
for root, dirs, files in os.walk(os.getcwd()):  # root 返回的是 绝对路径, '.' 返回的是 .
    print root  # 根据上面的语句决定
    print dirs  # 所有目录的名字, 没有为空
    print files  # 所有文件的名字
    for name in dirs:
        print(os.path.join(root, name))  # 目录的绝对路径
    for name in files:
        print(os.path.join(root, name))  # 文件的绝对路径
print os.path.join('~', 'Pictures')  # 专门生成路径的一个函数
os.chdir('/home/coder352/')  # 切换目录
