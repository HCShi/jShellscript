#!/usr/bin/python3
# coding: utf-8
import heapq, random
random.seed(10)
# 这个模块(build-in)实现了一个堆的数据结构, 完美的解决了 Top-K 问题, 以后解决 Top-K 问题的时候, 直接把这个模块拿来用就可以了
# 注意, 默认的 heap 是一个小顶堆
##################################################################
## heapq.nlargest(n, iterable, key=None)  返回最大的 n 个元素 (Top-K 问题)
## heapq.nsmallest(n, iterable, key=None) 返回最小的 n 个元素 (Top-K 问题)
mylist = list(random.sample(range(100), 10)); print(mylist)  # [73, 4, 54, 61, 1, 26, 59, 62, 35, 83]
largest = heapq.nlargest(3, mylist); print(largest)  # [83, 73, 62]
smallest = heapq.nsmallest(3, mylist); print(smallest)  # [1, 4, 26]

print(sorted(mylist)[:3], sorted(mylist)[-3:][::-1])  # [1, 4, 26] [83, 73, 62]; 这个简单的功能还是比较简单
##################################################################
## 下面的会写会原 list
## heapq.heapify(x) 将列表 x 进行堆调整, 默认的是小顶堆
heapq.heapify(mylist); print(mylist)  # [1, 4, 26, 35, 73, 54, 59, 62, 61, 83]

print(sorted(mylist))  # [1, 4, 26, 35, 54, 59, 61, 62, 73, 83]
print(sorted(mylist, reverse=True))  # [83, 73, 62, 61, 59, 54, 35, 26, 4, 1]
##################################################################
## heapq.heappush(heap, item) 把 item 添加到 heap 中 (heap 是一个列表)
## heapq.heappop(heap)        把堆顶元素弹出, 返回的就是堆顶
heapq.heappush(mylist, 105); print(mylist)  # [1, 4, 26, 35, 73, 54, 59, 62, 61, 83, 105]
heapq.heappop(mylist); print(mylist)  # [4, 35, 26, 61, 73, 54, 59, 62, 105, 83]; 这两个就不好用其他的模拟了
##################################################################
## heapq.heappushpop(heap, item) 先把 item 加入到堆中, 然后再 pop, 比 heappush() 再 heappop() 要快得多
## heapq.heapreplace(heap, item) 先 pop, 然后再把 item 加入到堆中, 比 heappop() 再 heappush() 要快得多
heapq.heappushpop(mylist, 130); print(mylist)  # [26, 35, 54, 61, 73, 130, 59, 62, 105, 83]
heapq.heapreplace(mylist, 2); print(mylist)    # [2, 35, 54, 61, 73, 130, 59, 62, 105, 83]
##################################################################
## heapq.merge(*iterables) 将多个列表合并, 并进行堆调整, 返回的是合并后的列表的迭代器
print(list(heapq.merge([1, 2, 10], [7, 34, 56])))  # [1, 2, 7, 10, 34, 56]

##################################################################
## 应用: Huffman 编码, 好厉害的算法, 并没有用 Huffman 树, 而是用了 Heap 堆...
# 如果看不懂的话, 具体解释见 jptalgorithm/l*.Huffman*.py
from collections import Counter
def encode(frequency):
    # 最后并没有建立一棵 Huffman 树, 所以不方便维护, 但是一般只是得到频率就够了...
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]  # 按原来顺序生成 list
    # print(heap)  # [[1, ['T', '']], [4, ['h', '']], [7, ['e', '']], [13, [' ', '']], [5, ['f', '']], ...]
    heapq.heapify(heap)  # 按照 item[0] 实现一个最小堆
    # print(heap)  # [[1, ['T', '']], [1, ['b', '']], [1, ['d', '']], [1, ['c', '']], [4, ['h', '']], ...]
    while len(heap) > 1:  # 初始是一个森林, 最后都变成一棵树就结束
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]: pair[1] = '0' + pair[1]  # 因为下面用了 [lo[0] + hi[0]] + lo[1:] + hi[1:], 所以后面可能有多个
        for pair in hi[1:]: pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))  # 先按长度排, 再按字典序排
data = "The frog at the bottom of the well drifts off into the great ocean"
frequency = Counter(data); print(frequency)  # Counter({' ': 13, 't': 9, 'e': 7, 'o': 7, 'f': 5, 'h': 4, 'r': 3, 'a': 3, 'g': 2, 'l': 2, 'i': 2, 'n': 2, 'T': 1, 'b': 1, 'm': 1, 'w': 1, 'd': 1, 's': 1, 'c': 1})
huff = encode(frequency); print(huff)
print("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")
for p in huff: print(p[0].ljust(10) + str(frequency[p[0]]).ljust(10) + p[1])
