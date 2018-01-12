#!/usr/bin/python3
# coding: utf-8
# collections 是 Python 内建的一个集合模块, 提供了许多有用的集合类
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
##################################################################
## namedtuple('名称', [属性 list]); 简化 class
p = (1, 2); print(p)  # tuple 可以表示不变集合, 一个点的二维坐标
# 但是, 看到 (1, 2), 很难看出这个 tuple 是用来表示一个坐标的, 定义一个 class 又小题大做了
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)  # 1 2
# namedtuple 是一个函数, 它用来创建一个自定义的 tuple 对象, 并且规定了 tuple 元素的个数, 并可以用属性而不是索引来引用 tuple 的某个元素
# namedtuple 可以很方便地定义一种数据类型, 它具备 tuple 的不变性, 又可以根据属性来引用, 使用十分方便
print(isinstance(p, Point))  # True; 验证创建的 Point 对象是 tuple 的一种子类
print(isinstance(p, tuple))  # True
Circle = namedtuple('Circle', ['x', 'y', 'r'])  # 用坐标和半径表示一个圆
##################################################################
## deque; 双向 list
q = ['a', 'b', 'c']; print(q.pop())  # c
q = ['a', 'b', 'c']; print(q.pop(0))  # a
q = ['a', 'b', 'c']; print(q.pop(1))  # b
q = ['a', 'b', 'c']; q.append('d'); print(q)  # ['a', 'b', 'c', 'd']
# list 的 pop 和 append 默认是最右边的, pop 可以选择其他位置

# 使用 list 存储数据时, 按索引访问元素很快, 但是插入和删除元素就很慢了, 因为 list 是线性存储, 数据量大的时候, 插入和删除效率很低
# deque 是为了高效实现插入和删除操作的双向列表, 适合用于队列和栈
q = deque(['a', 'b', 'c'])
q.append('x'); q.appendleft('y')  # 高效地往头部添加或删除元素
print(q)  # deque(['y', 'a', 'b', 'c', 'x'])
# deque 除了实现 list 的 append() 和 pop() 外, 还支持 appendleft() 和 popleft()
##################################################################
## defaultdict; 设置默认值的 dict
# 使用 dict 时, 如果引用的 Key 不存在, 就会抛出 KeyError; 如果希望 key 不存在时, 返回一个默认值, 就可以用 defaultdict
dd = defaultdict(lambda: 'N/A'); dd['key1'] = 'abc'
print(dd['key1'])  # abc; key1 存在
print(dd['key2'])  # N/A; key2 不存在, 返回默认值
# 注意默认值是调用函数返回的, 而函数在创建 defaultdict 对象时传入
# 除了在 Key 不存在时返回默认值, defaultdict 的其他行为跟 dict 是完全一样的; dict 也支持返回默认值

# 其实 dict() 也可以实现相关的功能, 显得 defaultdict() 比较鸡肋...
dic = {'name':'Tim', 'age':23}
print(dic.get('workage', 0))  # 如果没有的话, 返回 0

# 统计计数功能呢, 这个 Counter 默认已经实现了
frequency = defaultdict(int)
for symbol in 'hello': frequency[symbol] += 1
print(frequency)  # defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 2, 'o': 1})
print([[word, weight] for word, weight in frequency.items()])  # [['h', 1], ['e', 1], ['l', 2], ['o', 1]]
# defaultdict.items() 的循序会是原来的顺序, Count.items() 居然也是按原来的顺序
frequency = Counter('hello'); print(frequency)  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
print([[word, weight] for word, weight in frequency.items()])  # [['h', 1], ['e', 1], ['l', 2], ['o', 1]]
# 结论, Counter() 真好...
##################################################################
## OrderedDict; 有序 dict
# 使用 dict 时, Key 是无序的; 在对 dict 做迭代时, 我们无法确定 Key 的顺序; 如果要保持 Key 的顺序, 可以用 OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)]); print(d)  # {'a': 1, 'c': 3, 'b': 2}; dict 的 Key 是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)]); OrderedDict 的 Key 是有序的
# 注意, OrderedDict 的 Key 会按照插入的顺序排列, 不是 Key 本身排序:
od = OrderedDict()
od['z'] = 1; od['y'] = 2; od['x'] = 3
print(od.keys())  # ['z', 'y', 'x']; 按照插入的 Key 的顺序返回
# OrderedDict 可以实现一个 FIFO(先进先出) 的 dict, 当容量超出限制时, 先删除最早添加的 Key
##################################################################
## Counter 是一个简单的计数器, 例如, 统计字符出现的个数
# Counter 高级用法
print(Counter(['a', 'b', 'a', 'c']))  # Counter({'a': 2, 'b': 1, 'c': 1})
print(Counter('hello jrp \n hello'))  # Counter({'l': 4, ' ': 3, 'h': 2, 'e': 2, 'o': 2, 'j': 1, 'r': 1, 'p': 1, '\n': 1})
# 空格 和 回车 也会统计...
# items() 和 most_common() 顺序不一样, 前者是按输入顺序
print([[word, weight] for word, weight in Counter('abcdcd').items()])  # [['a', 1], ['b', 1], ['c', 2], ['d', 2]]
print(Counter('abcdcd').most_common(3))  # [('c', 2), ('d', 2), ('a', 1)]

c = Counter()
for ch in 'programming': c[ch] = c[ch] + 1
print(c)  # Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
# Counter 实际上也是 dict 的一个子类, 上面的结果可以看出, 字符 'g'、'm'、'r' 各出现了两次, 其他字符各出现了一次
c = Counter('programming'); print(c)  # 和上面效果一样

# 利用 dict 特性
print(c.keys(), type(c.keys()))  # dict_keys(['p', 'r', 'o', 'g', 'a', 'm', 'i', 'n']), <class 'dict_keys'>
print(c.values())  # dict_values([1, 2, 1, 2, 1, 2, 1, 1])
print(list(c.values()))  # [1, 2, 1, 2, 1, 2, 1, 1]

# list 嵌套 str, 见 朴素贝叶斯文本分类
texts = ["dog cat fish", "dog cat cat", "fish bird", 'bird']
c = Counter([word for line in texts for word in line.split()])
print(c)  # Counter({'cat': 3, 'dog': 2, 'fish': 2, 'bird': 2})
print(c['cat'])  # 3
