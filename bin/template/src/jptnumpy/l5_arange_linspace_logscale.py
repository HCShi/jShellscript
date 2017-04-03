#!/usr/bin/python3
# coding: utf-8
# 通过数值范围创建
import numpy as np
##################################################################
# numpy.arange(start=0, stop, step=1, dtype=None); 这个函数返回 ndarray 对象, 包含给定范围内的等间隔值
# start 范围的起始值, 默认为 0; stop 范围的终止值; step 步长, 默认为 1; dtype 返回 ndarray 的数据类型, 默认使用输入数据的类型
x = np.arange(5); print(x)  # [0  1  2  3  4]
x = np.arange(5, dtype=float); print(x)  # [0.  1.  2.  3.  4.]
x = np.arange(10, 20, 2); print(x)  # [10  12  14  16  18]
##################################################################
# numpy.linspace(start, stop, num=50, endpoint=true, retstep=false, dtype=None); 指定了范围之间的均匀间隔数量, 而不是步长
# start 序列的起始值; stop 序列的终止值, 如果endpoint为true, 该值包含于序列中
# num 要生成的等间隔样例数量, 默认为 50; endpoint 序列中是否包含 stop 值, 默认为ture
# retstep 如果为 true, 返回样例, 以及连续数字之间的步长; dtype 输出 ndarray 的数据类型
x = np.linspace(10, 20, 5); print(x)  # [10.   12.5   15.   17.5  20.]
x = np.linspace(10, 20, 5, endpoint= False); print(x)  # [10.   12.   14.   16.   18.]
x = np.linspace(1, 2, 5, retstep=True); print(x)  # (array([ 1., 1.25, 1.5, 1.75, 2.]), 0.25); 这里的 retstep 为 0.25
##################################################################
# numpy.logscale(start, stop, num=50, endpoint=true, base=10, dtype=None)
# 此函数返回一个 ndarray 对象, 其中包含在对数刻度上均匀分布的数字; 刻度的开始和结束端点是某个底数的幂, 通常为 10
# start 起始值是 base ** start; stop 终止值是 base ** stop; num 范围内的数值数量, 默认为50
# endpoint 如果为true, 终止值包含在输出数组当中; base 对数空间的底数, 默认为10; dtype 输出数组的数据类型, 如果没有提供, 则取决于其它参数
a = np.logspace(1.0, 2.0, num=3); print(a)  # [10. 31.6227766 100.]
a = np.logspace(1, 10, num=3, base=2); print(a)  # [2. 45.254834 1024.]; 将对数空间的底数设置为 2
