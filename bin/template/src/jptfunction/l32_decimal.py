#!/usr/bin/python3
# coding: utf-8
# 1. 解决 1.1 + 2.2 = 3.3000000000000003
# 2. 1.20 + 1.30 = 2.50, 最后的 0 会保留, 更加符合在学校学的
# 3. 定义小数点精度
# 4. 很强的管理能力, 根据需要控制输出格式, 得到或者忽略某类错误(如除0, 可以设置忽略它, 而得到一个 Infinity 的 Decimal 值）
# 5. Decimal() 的构造中如果是小数或字符的话, 需要加上单引号; 如果为整数, 则不需要
from decimal import Decimal as D
print(1.1 + 2.2, D('1.1') + D('2.2'))  # 3.300**03, 3.3

from decimal import getcontext
print(getcontext())  # decimal 在一个独立的 context 下工作, 可以通过 getcontext 来获取当前环境
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999999, Emax=999999999, capitals=1,
#         flags=[Rounded, Inexact], traps=[DivisionByZero, InvalidOperation, Overflow])
getcontext().prec = 6  # 设置小数点精度, 默认 28
print(D(1)/D(3))  # Decimal('0.333333')

# decimal 和 float 性能对比, 计算的性能是差了点...
# python -m timeit -s 'from decimal import Decimal as D' 'D("1.2")+D("3.4")'
# python -m timeit -s 'from decimal import Decimal as D' '1.2+3.4'

# 先介绍到这里, 太强大了...
