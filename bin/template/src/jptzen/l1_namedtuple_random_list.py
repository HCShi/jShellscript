#!/usr/bin/python
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
quize = zip(ANS, SCORE)
students = [
    Student(_id, gen_random_list('ABCD*', N_Questions)) for _id in range(1, N_Students+1)
]  # 学生答案为 'ABCD*' 随机，'*' 代表未作答

# print(quize)     # [('A', 3), ('B', 1), ('D', 1), ...
# print(students)  # [Student(id=1, ans=['C', 'B', 'A', ...
print 'ID\tScore\n=================='  # 这里还可以这样写
for student in students:
    sid, score = student.id, 0
    for i in range(len(quize)):
        if quize[i][0] == student.ans[i]:
            score += quize[i][1]
    print sid, '\t', score
