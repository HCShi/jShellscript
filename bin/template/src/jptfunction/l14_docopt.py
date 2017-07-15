#!/usr/bin/python3
# coding: utf-8
# python current.py -h
# 典型代表是 jcurl
##################################################################
## docopt 文档
##################################################################
"""curl localhost for Web test

Usage:
    jcurl [PORT] [URL]
    jcurl -v | --version
    jcurl -h | --help

Options:
    -h, --help     显示帮助菜单
    -v, --version  显示版本号
    port           端口号
    url            地址

Arguments:
    PORT  Local port opened
    URL   Local route

Example:
    jcurl
    jcurl 3000
    jcurl users/userlist
    jcurl 3000 users/userlist
"""
# __doc__ 必须放最前面
from docopt import docopt
args = docopt(__doc__)
##################################################################
## 功能实现, if 条件
##################################################################
import sys
if len(sys.argv) == 1: cmd = 'curl localhost'  # jcurl
if args['PORT']: cmd = 'curl localhost:' + str(args['PORT'])  # jcurl 3000
if args['URL']: cmd = 'curl localhost:' + str(args['URL'])  # jcurl users/userlist
if args['PORT'] and args['URL']: cmd = 'curl localhost:' + str(args['PORT']) + '/' + args['URL']  # jcurl 3000 users/userlist
from os import system
system(cmd)
##################################################################
## Main
##################################################################
if __name__ == '__main__':
    pass
    # print(args)
