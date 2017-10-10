#!/usr/bin/python3
# coding: utf-8
# 快速排序是 C.R.A.Hoare 于 1962 年提出的一种划分交换排序, 它采用了一种分治的策略, 通常称其为分治法 (Divide-and-Conquer Method)
# 思想:
#   首先任意选取一个数据(通常选用数组的第一个数)作为关键数据, 然后将所有比它小的数都放到它前面, 比它大的数都放到它后面, 这个过程称为一趟快速排序
# 一趟快速排序的算法是:
#   1) 设置两个变量 i、j, 排序开始的时候: i=0, j=N-1;
#   2) 以第一个数组元素作为关键数据, 赋值给 key, 即 key=A[0];
#   3) 从 j 开始向前搜索, 即由后开始向前搜索 (j--), 找到第一个小于 key 的 A[j], 将 A[j] 和 A[i] 互换;
#   4) 从 i 开始向后搜索, 即由前开始向后搜索 (i++), 找到第一个大于 key 的 A[i], 将 A[i] 和 A[j] 互换;
#   5) 重复第 3、4 步, 直到 i=j;
# (3, 4 步中, 没找到符合条件的值, 即 3 中 A[j] 不小于 key, 4 中 A[i] 不大于 key 的时候改变 j、i 的值, 使得 j=j-1, i=i+1, 直至找到为止;
#   找到符合条件的值, 进行交换的时候 i, j 指针位置不变; 另外, i==j 这一过程一定正好是 i+ 或 j- 完成的时候, 此时令循环结束)

# 重复循环处理的步骤可以用循环或递归实现; 重点是如何确定参考点以及如何把小于参考点的值挪到左边; 把大于参考点的值挪到右边;
# 快速排序的速度是杠杠的; 但快速排序不是稳定的算法, 有时可能无法完成排序; 在交换过程中可能进入胡同一直在几个数字之间处理
# 若稳定性要求高的可以使用其他排序算法, 例如归并排序

# 实现一: 语法糖: 一行实现快排, 效率很低, 思想很明显...
QuickSort = lambda X: [] if len(X) == 0 else QuickSort([i for i in X if i < X[0]]) + [X[0]] + QuickSort([i for i in X if i > X[0]])
# 实现二:
def quick_sort(lists, left, right):
    if left >= right: return lists  # 跳出递归判断

    key = lists[left]  # 选择参考点, 该调整范围的第 1 个值
    low, high = left, right

    while left < right:  # 循环判断直到遍历全部
        while left < right and lists[right] >= key: right -= 1  # 从右边开始查找小于参考点的值
        lists[left] = lists[right]                              # 这个位置的值先挪到左边
        while left < right and lists[left] <= key: left += 1    # 从左边开始查找大于参考点的值
        lists[right] = lists[left]                              # 这个位置的值挪到右边
    lists[left] = key  # 写回改成的值

    quick_sort(lists, low, left - 1)    # 递归左边部分
    quick_sort(lists, left + 1, high)   # 递归右边部分
    return lists
if __name__=="__main__":
    a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print(QuickSort(a))
    # 随机生成 1 百万个数据
    import random
    lists = random.sample(range(2000000), 1000000)
    sort_lists = quick_sort(lists[:], 0, len(lists)-1)  # 快速排序
    print(lists[:10], '\n', sort_lists[:10])
