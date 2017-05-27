#!/usr/bin/python3
# coding: utf-8
__author__ = 'Jia Ruipeng'
'''
一个自己的笔记管理软件
可以将自己写的代码片段放到指定的目录, 用命令快速查看
'''
import os, sys, re
import functools
from datetime import datetime
from configparser import ConfigParser  # 读配置文件
cfg = ConfigParser()
cfg.read(os.path.expanduser('~') + '~/github/jShellscript/bin/pythonpath/config.ini'.lstrip('~'))

##################################################################
# template_ 系列函数是为 jpt... 等 python 程序提供服务的
# 尽量减少 template_ 模块之间的耦合, 同时 jpt... 等程序的逻辑清晰
# 新增判断语句, 支持其他语言的模板
##################################################################
def template_print(filetype='py'):  # 装饰器, 针对不同的文件进行不同的操作, 下面会用到
    def decorate(func):
        separator = cfg.get('MISC', 'template_print_separator')
        @functools.wraps(func)
        def wrapper(*args, **kw):  # 传进来的是 l1, l2 ...
            f_names = [x for x in os.listdir(args[0]) if x.endswith(filetype) and args[1] == x.split('_')[0]]
            for f_name in f_names:
                print(separator + ' ' + f_name)  # 第一行的分隔符
                if filetype == 'py':
                    print('\n'.join([' ' * 4 + line.rstrip('\n') for line in open(args[0] + '/' + f_name).readlines()[2:]]))  # 去掉开头两行相同的
                elif filetype == 'sh':
                    print('\n'.join([' ' * 4 + line.rstrip('\n') for line in open(args[0] + '/' + f_name).readlines()[1:]]))  # 去掉开头一行相同的
                elif filetype == 'html':  # 由于 html 太长了, 所以直接打开吧
                    # print('\n'.join([' ' * 2 + line for line in \
                                     # re.split(r'<body>|</body>', open(args[0] + '/' + f_name).read())[1].strip('\n').split('\n')]))
                    os.chdir(args[0])
                    os.system('vim --noplugin ' + f_name)
                else:  # 针对其他所有情况
                    print('\n'.join([' ' * 4 + line.rstrip('\n') for line in open(args[0] + '/' + f_name).readlines()]))
        return wrapper
    return decorate

def template_generate_func(dir_path, filetype='py'):  # 根据文件夹中的文件生成各个参数
    '''
    添加函数的步骤:
        1. 编写自己的函数, 要用 globals() 来生成全局函数
        2. 在 template_argparse 后面添加 parser.add_argument() 对其进行注册
        3. 然后执行的时候 template_main.getattr 会自动对命令的参数进行解析
    '''
    for pre in [x.split('_')[0] for x in os.listdir(dir_path) if x.endswith(filetype)]:
        @template_print(filetype)
        def _f(): pass  # 这里定义函数的时候没有用参数, 调用的时候传 (*args, **kw)
        globals()[pre] = _f
        del _f
    # globals()['g'] = lambda url, filename: os.system('echo "' + ': ' + str(int(datetime.now().timestamp())) + ':0;cd ' + url + '" >> ~/.zsh_history')
    globals()['g'] = lambda url, filename: print(url)  # 上面是写进历史记录, 然后 alias 调用, 现在改为 cd `jptfunction -g`
    # 已经将 -g 的这个功能覆盖了, 本来 `jptfunction` 可以切换目录, jptfunction 打印目录, 现在是 jptfunction 可以直接切换目录

def template_dir_path(filetype='py'):  # 得到根据执行的文件名得到对应的文件夹的位置, 必须通过调用的文件生成
    if filetype == 'py':
        return os.path.expanduser('~') + '~/github/jShellscript/bin/template/src/'.lstrip('~') + sys.argv[0].split('/')[-1]
    elif filetype == 'sh' or filetype == 'dot':
        return os.path.expanduser('~') + '~/github/jShellscript/template/src/'.lstrip('~') + sys.argv[0].split('/')[-1]
    elif filetype == 'html' or filetype == 'js' or filetype == 'svg':
        return os.path.expanduser('~') + '~/github/jWeb/template/src/'.lstrip('~') + sys.argv[0].split('/')[-1]
    elif filetype == 'tex':
        return os.path.expanduser('~') + '~/github/jTemplate/latex/src/'.lstrip('~') + sys.argv[0].split('/')[-1]
    elif filetype == 'el':
        return os.path.expanduser('~') + '~/github/jTemplate/lisp/elisp/src/'.lstrip('~') + sys.argv[0].split('/')[-1]

def template_main(args, dir_path):  # main 函数
    if args.autho:  # -h --version 这些不会执行这些 if 判断
        print(args.autho)
        exit(0)
    if len(sys.argv) == 1: sys.argv.append('-g')
    getattr(sys.modules[__name__], sys.argv[1].lstrip('-'))(dir_path, sys.argv[1].lstrip('-'))  # getattr()() 第二个传的是参数

def template_argparse(dir_path, filetype='py', comment=''):  # 生成 argparse 部分
    module_name = dir_path.split('/')[-1]
    import argparse
    parser = argparse.ArgumentParser(
        prog=module_name,
        formatter_class=argparse.RawDescriptionHelpFormatter,  # 没有这句话, 换行会过滤掉
        description='''\
            Usage Example:
            --------------------------------
            %s     # -g default
            %s -g  # 返回对应的路径
            %s -l1
            %s -l2
            # 以上格式经测试正确

            Comment:
            --------------------------------
            %s
            ''' % (module_name, module_name, module_name, module_name, comment))
    parser.add_argument('--autho', action='store_const', const='14thCoder', help='show the autho')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    for rule in sorted(list(set(x for x in os.listdir(dir_path) if x.endswith(filetype)))):
        parser.add_argument('-' + rule.split('_')[0], action='store_true', help=' '.join(rule.split('.')[0].split('_')[1:]))
    parser.add_argument('-g', action='store_true', help='go to corresponding directory')
    return parser.parse_args()  # 返回 argparse 渲染过后的对象

if __name__ == '__main__':
    pass
