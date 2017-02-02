#!/usr/bin/python3
# coding: utf-8
import os, sys, re
import functools
from configparser import ConfigParser  # 读配置文件
cfg = ConfigParser()
cfg.read(os.path.expanduser('~') + '~/github/jShellscript/bin/pythonpath/config.ini'.lstrip('~'))

##################################################################
# template_ 系列函数是为 jpt... 等 python 程序提供服务的
# 尽量减少 template_ 模块之间的耦合, 同时 jpt... 等程序的逻辑清晰
# 新增判断语句, 支持其他语言的模板
##################################################################
def template_print(filetype='py'):  # 装饰器
    def decorate(func):
        separator = cfg.get('MISC', 'template_print_separator')
        @functools.wraps(func)
        def wrapper(*args, **kw):  # 传进来的是 l1, l2 ...
            f_names = [x for x in os.listdir(args[0]) if x.endswith(filetype) and args[1] == x.split('_')[0]]
            for f_name in f_names:
                print(separator + ' ' + f_name)  # 第一行的分隔符
                if filetype == 'py':
                    print('\n'.join([' ' * 4 + line.rstrip('\n') for line in open(args[0] + '/' + f_name).readlines()[2:]]))  # 去掉开头两行相同的
                elif filetype == 'html':
                    print('\n'.join([' ' * 2 + line for line in \
                                     re.split(r'<body>|</body>', open(args[0] + '/' + f_name).read())[1].strip('\n').split('\n')]))
        return wrapper
    return decorate

def template_generate_func(dir_path, filetype='py'):  # 根据文件夹中的文件生成各个参数
    for pre in [x.split('_')[0] for x in os.listdir(dir_path) if x.endswith(filetype)]:
        @template_print(filetype)  # 使用自己定义的装饰器
        def _f(url): pass
        globals()[pre] = _f
        del _f

def template_dir_path(filetype='py'):  # 得到根据执行的文件名得到对应的文件夹的位置, 必须通过调用的文件生成
    if filetype == 'py':
        return os.path.expanduser('~') + '~/github/jShellscript/bin/template/src/'.lstrip('~') + sys.argv[0].split('/')[-1]
    elif filetype == 'html':
        return os.path.expanduser('~') + '~/github/jWeb/template/src/'.lstrip('~') + sys.argv[0].split('/')[-1]

def template_main(args, dir_path):  # main 函数
    if args.autho:  # -h --version 这些不会执行这些 if 判断
        print(args.autho)
        exit(0)
    if len(sys.argv) == 1: sys.argv.append('-l1')
    getattr(sys.modules[__name__], sys.argv[1].lstrip('-'))(dir_path, sys.argv[1].lstrip('-'))

def template_argparse(dir_path, filetype='py', comment=''):  # 生成 argparse 部分
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
    for rule in sorted(list(set(x for x in os.listdir(dir_path) if x.endswith(filetype)))):
        parser.add_argument('-' + rule.split('_')[0], action='store_true', help=' '.join(rule.split('.')[0].split('_')[1:]))
    return parser.parse_args()  # 返回 argparse 渲染过后的对象

if __name__ == '__main__':
    pass
