#!/usr/bin/python3
# coding: utf-8
# 卜东波老师算法课 第一次作业编程
##################################################################
## Closest Pair: A Divide-and-Conquer Approach
# 分治法找最近点对, 可以把时间复杂度从暴力的 O(n^2) 降低到 O(nlogn)
# 原理就是把图中的所有点分为左右两半, 接着递归再二分左右两半; 直到区间内只有两个点, 易得两点间长度
# 之后是合并的过程, 从左右区间中取出更小的那一个; 接着, 比较中间区域 strip 内的点对, 看看有没有更短的点对; (这个过程经过证明最多只要比较 7 次)
# 最后得到最小的那个长度

# 我们首先将所有点按照坐标 x 排序一下, 再做一条直线 l 当作"分割线", 方便我们递归
# 然后, 我们就可以把这些点按照 x 轴的坐标分为左半部分和右半部分; 那么最短距离一定在左半部分、右半部分、跨越左右的点对中的一个
# 那么你可能会有疑问了: 本来最近点对也一定在这三个区域内, 这不还是相当于什么都没干吗？
# 还真不是; 我们可以假设通过递归得到了左边最小距离为 d1, 右边最小距离为 d2, 令 δ = min(d1,d2)
# 如图所示, 如果跨越左右的点对可能是最短距离, 那么它也必然比 δ 小; 而在以 l 为中心、最大距离为 2δ 的区域中, 最多有 O(n) 个如图所示的矩形;
# 另外, 可以证明对于每个矩形区域, 最多尝试 8 个点对一定能找到最短距离 (算法导论第 33.4 节有详细的证明, 这里不再赘述)
# 因此, 我们可以写出递归式: T(n)=2T(n/2)+O(n), 可以用主项定理 (master method) 解得时间复杂度 T(n)=O(nlogn);
# 加上排序一次的时间 O(nlogn), 因此整个算法的运行时间 T(n)' = T(n)+O(nlogn) = O(nlogn)
from math import sqrt, pow
import random
def distance(a, b):
    return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))

def bruteforce_Min(points, current=float("inf")):
    if len(points) < 2: return current
    else:
        head = points[0]  # 设定当前点
        del points[0]
        newMin = min([distance(head, x) for x in points])  # 每个点都和当前点比较, 找到最小值
        newCurrent = min([newMin, current])
        return bruteforce_Min(points, newCurrent)  # 去除当前点, 但是把当前点的最短距离传进去

def divideMin(points):
    len_point = len(points)
    if len_point <= 3:
        return bruteforce_Min(points)  # 直接暴力出来
    half = len_point // 2
    # minimum = min([bruteforce_Min(points[:half]), bruteforce_Min(points[half:])])  # 直接暴力出来
    minimum = min(divideMin(points[:half]), divideMin(points[half:]))                # 递归出来
    # nearLine = [filter(lambda x: half - minimum <= x[0] <= half + minimum, points)]  # 过滤器
    nearLine = [x for x in points if half - minimum <= x[0] <= half + minimum]         # 生成器
    return min([bruteforce_Min(nearLine), minimum])  # 这里不会比较很多次, 可以直接暴力出来

# 构造 1000 个坐标, 并添加 (1, 2) (2, 1) 用来检测
list1 = list(zip(random.sample(range(2000), 1000) + [1, 2], random.sample(range(2000), 1000) + [2, 1]))
print(divideMin(list1))  # 1.414
