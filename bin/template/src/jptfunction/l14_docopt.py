#!/usr/bin/python3
# coding: utf-8
##################################################################
# docopt 文档
##################################################################
""" Zen of Python

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
from configparser import ConfigParser  # 读配置文件
cfg = ConfigParser()
cfg.read(user_path + '/github/jShellscript/bin/template/config.ini')
path = cfg.get('PATH', 'current_path')
separator = cfg.get('MISC', 'separator')
def cli():
    args, _run = docopt(__doc__), 0;
    if len(sys.argv) == 1: args['-a'] = True
    if args['run']: _run = 1
    if args['-a']:
        file_path = path + './src/jptzen/l1_namedtuple_random_list.py'.lstrip('.')
        if _run: os.system('python3 ' + file_path)
        else:
            print(separator)
            for line in open(file_path).readlines()[2:]: print(' ' * 4 + line, end="")

if __name__ == '__main__':
    cli()
