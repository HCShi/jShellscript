#!/usr/bin/python
# coding: utf-8
##################################################################
# 第一部分: argparse, 参考自 b64, 有删减, 不能执行
##################################################################
import argparse
parser = argparse.ArgumentParser(
    prog="b64",  # 这里填应用的名字
    formatter_class=argparse.RawDescriptionHelpFormatter,  # 没有这句话, 换行会过滤掉
    description='''\
        Usage Example:  # 这里可写一些自己的描述
        --------------------------------
        b64 -e hellojrp            # aGVsbG9qcnA=
        ''')
parser.add_argument('string', type=str, nargs='?', help='decode the string')                    # test.py string 用户指定的字符串, 可以不输入
parser.add_argument('-d', action='store_true', help='decode the string [default]')              # bool 型参数, 可以是 --d, --decode
parser.add_argument('--name', action='store', help='name')                                      # --name jrp
parser.add_argument('--autho', action='store_const', const='14thCoder', help='show the autho')  # 固定输出的字符串
parser.add_argument('--version', action='version', version='%(prog)s 1.0')                      # 版本信息
args = parser.parse_args()
##################################################################
# 第二部分: 主功能区
##################################################################
import base64
def decode(s):
    return base64.b64decode(s)
##################################################################
# 第三部分: main
##################################################################
import sys
if __name__ == "__main__":
    if args.autho:
        print args.autho
        exit(0)
    if len(sys.argv) == 1:  # echo 'aGVsbG9qcnA' | jclip, 默认是解密
        decode(s)
    if len(sys.argv) == 2 and args.e and args.string:  # 这里可以使用上面定义的参数
        args.string = raw_input()  # echo 'aGVsbG9qcnA' | jclip -d
        encode(args.string)
