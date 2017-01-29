#!/usr/bin/python3
# coding: utf-8
import random
from collections import namedtuple
Student = namedtuple('Student', ['id', 'ans'])  # tuple 子类, 类似于结构体
N_Questions = 10  # 问题的数量
N_Students = 10   # 学生的数量

def gen_random_list(opts, n):
    return [random.choice(opts) for i in range(n)]

ANS   = gen_random_list('ABCD', N_Questions)       # 问题答案 'ABCD' 随机
SCORE = gen_random_list(range(1, 6), N_Questions)  # 题目分值 1~5 分
quize = list(zip(ANS, SCORE))  # [('A', 3), ('B', 1), ('D', 1), ...
students = [
    Student(_id, gen_random_list('ABCD*', N_Questions)) for _id in range(1, N_Students+1)  # 学生答案为 'ABCD*' 随机, '*' 代表未作答
]  # [Student(id=1, ans=['C', 'B', 'A', ...

print ('ID\tScore\n==================')  # 这里还可以这样写
for student in students:
    print(student.id, '\t', sum(q[1] for ans, q in zip(student.ans, quize) if ans==q[0]))
# python 中的 for 循环比 c 更进一步, 通常不需要额外的状态变量来记录当前循环次数, 但有时候也不得不使用状态变量, 如第二个循环中比较两个列表的元素
# 函数式编程的一大特点就是尽量抛弃这种明显循环遍历的做法 (计算机思维), 而是把注意集中在解决问题本身,
# 一如在现实中我们批改试卷时, 只需要将两组答案并列进行比较即可, 下面是实现函数式编程
print('ID\tScore\n==================')  # 这里还可以这样写
def cal(quize):
    def inner(student):
        # 将学生答案与正确答案合并到一起, 然后过滤出答案一致的题目
        filtered = filter(lambda x: x[0] == x[1][0], zip(student.ans, quize))  # [('A', ('A', 3)), ('D', ('D', 1)), ...]
        from functools import reduce
        reduced = reduce(lambda x, y: x + y[1][1], filtered, 0)
        print(student.id, '\t', reduced)
    return inner  # 借助闭包(Closure)的方法, 就可以维持纯净的 FP 模式
list(map(cal(quize), students))
# 通过 zip/filter/reduce/map 等函数将数据处理的方法打包应用到数据上, 实现了基本的函数式编程操作
