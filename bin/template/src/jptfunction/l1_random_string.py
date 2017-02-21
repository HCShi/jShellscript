#!/usr/bin/python3
# coding: utf-8
import random, string
random.seed(10)  # 不写这句话, 默认是系统时间, 现在自己指定了, 所以每次生成的随机数会一样

# ascii_letters 包含 大写和小写 的26个英文字母, 不包含数字及其它的字符
print(''.join(random.sample(string.ascii_letters, 4)))  # wEkQ
print(''.join(random.sample(string.ascii_letters + string.digits + '()`~!@#$%^&*-+=|\'{}[]:;"<>,.?/', 4)))  # 这样就更像密码了
print(''.join(random.choice(string.ascii_uppercase + string.digits)))  # 只能生成一个
print(''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(10)))  # 新添的控制长度

def rndColor(): return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
print(rndColor())  # (151, 195, 191), 随机颜色
def gen_random_list(opts, n): return [random.choice(opts) for i in range(n)]
print(gen_random_list('ABCD*', 4))  # ['A', 'D', '*', '*'], 从给定的模式中选
print(gen_random_list(range(1, 5), 4))  # 在 [1, 5) 中随机选
