#!/usr/bin/python3
# coding: utf-8
import os
import functools
from configparser import ConfigParser  # 读配置文件
cfg = ConfigParser()
cfg.read(os.path.expanduser('~') + '~/github/jShellscript/bin/pythonpath/config.ini'.lstrip('~'))

def template_print(func):  # 装饰器
    separator = cfg.get('MISC', 'template_print_separator')
    @functools.wraps(func)
    def wrapper(*args, **kw):
        f_name = [x for x in os.listdir(args[0]) if x.endswith('py') and args[1] in x.split('_')][0]
        print(separator + ' ' + f_name)  # 第一行的分隔符
        print('\n'.join([' ' * 4 + line.rstrip('\n') for line in open(args[0] + '/' + f_name).readlines()[2:]]))  # 去掉开头两行相同的
    return wrapper

def template_argparse(dir_path, comment=''):  # 生成 argparse 部分
    module_name = dir_path.split('/')[-1]
    import argparse
    parser = argparse.ArgumentParser(
        prog=module_name,
        formatter_class=argparse.RawDescriptionHelpFormatter,  # 没有这句话, 换行会过滤掉
        description='''\
            Usage Example:
            --------------------------------
            %s
            %s l1
            %s l2
            # 以上格式经测试正确

            Comment:
            --------------------------------
            %s
            ''' % (module_name, module_name, module_name, comment))
    parser.add_argument('--autho', action='store_const', const='14thCoder', help='show the autho')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    for rule in sorted([x for x in os.listdir(dir_path) if x.endswith('py')]):
        parser.add_argument('-' + rule.split('_')[0], action='store_true', help=' '.join(rule.split('.')[0].split('_')[1:]))
    return parser.parse_args()

if __name__ == '__main__':
    pass
