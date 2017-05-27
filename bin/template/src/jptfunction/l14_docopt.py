#!/usr/bin/python3
# coding: utf-8
# python current.py -h
# 找个合适的例子替换掉这个, 现在这个好烂啊
##################################################################
# docopt 文档
##################################################################
"""Zen of Python  # 这里定这些简介

Usage:
    jticket [-abcdefgijklmnopqrstuvwxyz] [run]

Example:
    jptzen -a      # 打印代码
    jptzen -a run  # 运行代码

Options:
    -h,--help
    -a  # 生成 N 位同学在某份试卷的 M 道选择题上的得分, l1_namedtuple_random_list
"""
from docopt import docopt  # __doc__ 必须放最前面
##################################################################
# 功能实现, 修改两处, 先改下面 if, 再添加上面的 -ab...
##################################################################
import os, sys
user_path = os.path.expanduser('~')    # '/home/coder352'
def main():  # 函数名可随便换
    args, _run = docopt(__doc__), 0;
    if len(sys.argv) == 1: args['-a'] = True  # argv=1 表示 ./l14_docopt.py 没带参数
    if args['run']: _run = 1
    if args['-a']:
        if _run: print('hello')
        else: print("world")

if __name__ == '__main__':
    main()
