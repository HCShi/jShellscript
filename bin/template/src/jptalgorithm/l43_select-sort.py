#!/usr/bin/python3
# coding: utf-8
# 选择排序原理:
# 每一趟从元素列表中选取一个最小的元素作为有序序列中第 i 个元素
# 意思就是:
# 下标: ------ 0  1  2  3  4  5
# 列表: seq = [5, 4, 3, 0, 1, 2]
# 每次循环, 都从列表中选出值最小的元素, 与第 i 个元素进行交换

# 例如:
# 第一个循环: i = 0, 值 = 5, 此时列表最小元素为 0, 下标 = 3; 则将 seq[i] 与 seq[3] 进行交换, 交换后的列表为: [0, 4, 3, 5, 1, 2]
# 第二次循环: i = 1, 值 = 4, 此时列表最小元素为 1, 下标 = 4; 则将 seq[i] 与 seq[4] 进行交换, 交换后的列表为: [0, 1, 3, 5, 4, 2]
# 依次循环, 直到排序完毕
# 选择排序的特点: 每次循环, 仅交换一次元素;
def select_sort(alist):
    for i in range(0, len(alist), 1):
        min = alist[i]  # 当前最小值
        index = i  # 记录当前的最小值
        for j in range(i, len(alist), 1):
            if (alist[j] < min):
                min = alist[j]
                index = j
        alist[index], alist[i] = alist[i], min
    return alist
import random
a = random.sample(range(100), 20)
print(select_sort(a))
