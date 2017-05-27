#!/usr/bin/python
# coding: utf-8
##################################################################
## sys
import sys
print(sys.path)  # 当前 python 的模板路径
sys.stdout.write(str(99) + '\n')  # print() 可以自动转化为 str, 并且带 \n
print(sys.argv)  # ['l3_sys_os_subprocess.py']; 就是当前的文件名, 带参数的话会显示参数
##################################################################
## os
import os
# os.walk(), os.system(), os.path.join(), os.chdir(), os.getcwd(), os.expanduser(), os.listdir()
os.system('pwd')  # 执行 terminal 命令, 要得到命令的结果, 需要用 subprocess.check_output(pwd)
print(os.getcwd())  # 得到当前路径
print(os.path.expanduser('~'))  # 当前家目录
print(os.path.abspath('.'))  # 当前的绝对路径
for root, dirs, files in os.walk(os.getcwd()):  # 递归遍历当前目录
    print(root, dirs, files)  # 根据上面的语句决定, 所有目录的名字(没有为空), 所有文件的名字
    print([os.path.join(root, name) for name in dirs])  # 目录的绝对路径
    print([os.path.join(root, name) for name in files])  # 文件的绝对路径
    pass
print([d for d in os.listdir('.')])  # 当前路径下的所有文件和目录, 没有子目录
print(os.path.join('~', 'Pictures'))  # 专门生成路径的一个函数
os.chdir('/home/coder352/')  # 切换目录
##################################################################
## subprocess
import subprocess
tmp = subprocess.check_output('pwd'); print(tmp)
subprocess.call(['./test.sh'])  # Thanks @Jim Dennis for suggesting the []; chmod +x test.sh
# for source, 使用 alias, cd 等命令时没有效果, 但可以试试 os.environ()
subprocess.Popen("source test.sh", shell=True, executable="/bin/bash")
# 1. source is a bash builtin command (type help source in bash) but the default shell is /bin/sh that doesn't understand it (/bin/sh uses .)
# 2. it is not very useful to execute source in a subprocess because it can't affect parent's environment
