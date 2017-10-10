#!/usr/bin/python3
# coding: utf-8
# 每次从数组中取一个数字, 与现有数字比较并插入适当位置
# 如此重复, 每次均可以保持现有数字按照顺序排列, 直到数字取完, 即排序成功

# 这很像打牌时的抓牌情况,
# 第一个条件: 保持手上的牌的顺序是正确的
# 第二个条件: 每次抓到新的牌均按照顺序插入手上的牌中间
# 保证这两条不变, 那么无论抓了几张牌, 最后手上的牌都是依照顺序排列的

# 插入排序算法
def insert-sort(A):
    for j in range(1, len(A)):
        key = A[j]

        # insert A[j] into the sorted sequence A[1 ... j-1]
        i = j - 1
        while i >= 0 and A[i] > key:  # 向前查找插入位置
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
