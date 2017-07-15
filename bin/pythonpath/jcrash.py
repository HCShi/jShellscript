#!/usr/bin/python3
# coding: utf-8
# 抛出异常时自动把你带到 IPython Shell, 而且和普通的 IPython 不同, 可以调用 p(print), up(up stack), down(down stack) 之类的命令
# 还能创建临时变量, 执行任意函数
# 在代码某个地方 import jcrash 就可以了

import sys

class ExceptionHook:
    instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            from IPython.core import ultratb
            self.instance = ultratb.FormattedTB(mode='Plain',
                 color_scheme='Linux', call_pdb=1)
        return self.instance(*args, **kwargs)

def info():
    print(sys._getframe().f_code.co_filename)  # 当前文件名
    print(sys._getframe(0).f_code.co_name)  # 当前函数名
    print(sys._getframe(1).f_code.co_name)  # 调用该函数的函数的名字, 如果没有被调用, 则返回 <module>
    print(sys._getframe().f_lineno)  # 当前行号
# 目前这个函数通过 jcrash.info() 来调用, 以后再弄...

sys.excepthook = ExceptionHook()

# 作者：Rui L
# 链接：https://www.zhihu.com/question/21572891/answer/26046582

# 类似方法: (来自知乎的那个评论)
# 1. import pdb; pdb.set_trace()  # 也可以执行 python 命令和 p, up, down, 放到哪就在哪停下
# 2. from IPython import embed; embed()  # 没用 p, up, down; 完全就是一个 IPython 环境, 而且还没有上下文的提示
# 上面两个不能直接定位到错误, 而是放到哪在哪停
# 3. ipython tmp.py --pdb  # 自动停到错误的地方, 上下文提示丰富, 和当前脚本最像了
# 4. Scrapy 中 from scrapy.shell import inspect_response; inspect_response(response, self)
