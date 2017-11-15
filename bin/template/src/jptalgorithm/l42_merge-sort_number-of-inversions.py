#!/usr/bin/python3
# coding: utf-8
# 归并排序需要比快速排序多用一个数组空间
# 合并排序(归并排序) 采用分组处理, 也是二分法的思想; 将一组数据拆成两组, 再将小组继续拆分为两个直到每个小组剩下 1 或 0 个元素
# 这时才开始对小组中的元素排序, 排序完成之后再合并为新的小组; 一直往上排序和合并直到排序完成
# 这里需要思考两个东西:
# 1) 如何拆分
# 2) 如何合并且排序; 下边分别实现这两个过程
##################################################################
## 第一种, 归并排序
def merge(left, right):  # 合并和排序
    result, i, j = [], 0, 0
    length_left, length_right = len(left), len(right)
    while i < length_left and j < length_right:  # 逐个比较两个列表的元素, 小的添加进新列表, 大的留下继续比较
        if left[i] <= right[j]: result.append(left[i]); i += 1
        else:                   result.append(right[j]); j += 1
    result.extend(left[i:])  # 最后加上未比较的元素
    result.extend(right[j:])
    return result
##################################################################
## 第二种 更加 Python, 顺便加上了 求逆序数
num = 0
def merge(left, right):
    result = []                           # 1. 定义 num 逆序数个数, 为 0
    while left and right:
        if left[0] > right[0]:
            result.append(right[0])
            right = right[1:]
            global num; num += len(left)  # 2. 这里计算一下逆序数, 这有这两个多出来的地方, 针对归并排序...
        else:
            result.append(left[0])
            left = left[1:]
    result.extend(left)  # 最后加上未比较的元素
    result.extend(right)
    return result
##################################################################
## 主程序
def merge_sort(lists):  # 归并排序入口, 其实这里只是递归实现拆分列表
    length = len(lists)
    return merge(merge_sort(lists[:length // 2]), merge_sort(lists[length // 2:])) if length > 1 else lists  # 可以拆分成下面两行
    # if length <= 1: return lists  # 递归退出条件判断
    # return merge(merge_sort(lists[:length // 2]), merge_sort(lists[length // 2:]))  # 递归拆分, 左子树和右子树分别递归进去
if __name__ == '__main__':
    import random
    lists = random.sample(range(20), 10)
    result = merge_sort(lists)
    print(result[:10])
