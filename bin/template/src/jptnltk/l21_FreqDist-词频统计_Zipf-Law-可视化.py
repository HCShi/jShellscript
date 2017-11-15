#!/usr/bin/python3
# coding: utf-8
import nltk
from nltk.corpus import gutenberg  # 导入 gutenberg 集
##################################################################
## FreqDist 跟踪分布中的采样频率 (sample frequencies)
from nltk import FreqDist  # 导入 FreqDist 类
fd = FreqDist(gutenberg.words('austen-persuasion.txt'))  # 频率分布实例化, 统计文本中的 Token
print(fd)  # <FreqDist with 51156 samples and 2621613 outcomes>; 可以得到 51156 个 不重复值, 2621613 个 token
print(type(fd))  # <class 'nltk.probability.FreqDist'>
print(fd['the'])  # 3120; 查看 word 出现次数; 默认 FreqDist 是一个字典
print(fd.N())  # 98171; 是单词, 不是字母, 有重复的
print(fd.B())  # 6132; number of bins or unique samples; 唯一单词, bins 表示相同的会在一个 bin 中
print(len(fd.keys()), type(fd.keys()))  # 6132 <class 'dict_keys'>
print(fd.keys())  # fd.B() 只是输出个数, 这个是把所有词汇表输出
print(fd.max())  # 频率最高的一个词
print(fd.freq('the'))  # 0.03178127960395636; 出现频率 3120 / 98171
print(fd.hapaxes())  # ['[', 'Persuasion', 'Jane', ...] 只出现一次的罕用词
# 出现频率最高的大多是一些"虚词", 出现频率极低的(hapaxes)又只能靠上下文来理解; 文本中出现频率最高和最低的那些词往往并不能反映这个文本的特征
for idx, word in enumerate(fd):  # 可以用 enumerate 来遍历, 是按出现顺序排的
    if idx == 5: break
    print(idx, word)  # 0 [; 1 Persuasion; 2 by; 3 Jane; 4 Austen
##################################################################
## 统计词的长度频率
fdist = FreqDist(len(w) for w in gutenberg.words('austen-persuasion.txt'))
print(fdist)  # <FreqDist with 16 samples and 98171 outcomes>
print(fdist.items())  # dict_items([(1, 16274), (10, 1615), (2, 16165), (4, 15613), (6, 6538), (7, 5714), (3, 20013), (8, 3348), (13, 230), (9, 2887), (5, 8422), (11, 768), (12, 486), (14, 69), (15, 25), (16, 4)])
print(fdist.most_common(3))  # [(3, 20013), (1, 16274), (2, 16165)]
##################################################################
## 统计 英文字符
fdist = nltk.FreqDist(ch.lower() for ch in gutenberg.raw('austen-persuasion.txt') if ch.isalpha())  # 可以不用 [] 将生成器 list 化
print(fdist.most_common(5))  # [('e', 46949), ('t', 32192), ('a', 29371), ('o', 27617), ('n', 26718)]
print([char for (char, count) in fdist.most_common()])  # 26 个字母使用频率排序
##################################################################
## most_common(n); 得到前 n 个按频率排序后的词
print(fd.most_common(5))  # [(',', 6750), ('the', 3120), ('to', 2775), ('.', 2741), ('and', 2739)]
fd.tabulate()  # 表格形式给出 most_common()
# 或者使用 Counter 来实现
from collections import Counter
print(Counter(fd).most_common(5))  # [(',', 6750), ('the', 3120), ('to', 2775), ('.', 2741), ('and', 2739)]
# 简奥斯丁的小说 Persuasion 总共包含 98171 字和 6141 个唯一单词. 此外, 最常见的词例是逗号, 接着是单词 the.
# 如果你对海量的语料库进行统计, 将每个单词的出现次数和单词出现的频率由高到低记录在表中, 我们可以直观地发现列表中词频和词序的关系.

# 事实上, 齐普夫(Zipf)证明了这个关系可以表达为数学表达式, 例如: 对于任意给定单词, f * r = k(正比于 k);
# f 是词频, r 是词的排列, 或者是在排序后列表中的词序, 而 k 则是一个常数.
# 复杂的公式为: f * r = 1 / log(N); N 为所有单词的总数
# 举个例子, 第五高频的词应该比第十高频的词的出现次数要多两倍. 在 NLP 文献中, 以上的关系通常被称为 "齐普夫定律(Zipf’s Law)" .

# 即使由齐普夫定律描述的数学关系不一定完全准确, 但它依然对于人类语言中单词分布的刻画很有用——词序小的词很常出现,
# 而稍微词序大一点的则较为少出现, 词序非常大的词则几乎没有怎么出现; 相关的 log-log 关系如图 1, 可以很清晰地发现我们语料库中对应的扩展关系
##################################################################
## 使用 NLTK 对齐普夫定律进行作图
import matplotlib.pyplot as plt
fd = FreqDist(gutenberg.words(gutenberg.fileids()))  # 统计 Gutenberg 中每个词例数量
print(fd)  # <FreqDist with 51156 samples and 2621613 outcomes>; 5166 个非重复, 2621613 个 token
fd.plot(50, title='hello', cumulative=True)  # 累加
fd.plot(50)  # 前 50 对应的出现次数

## 传统 matplotlib 方法, 和上面对比, 可以使用 loglog()
freqs = []  # 初始化两个空列表来存放词序和词频
for word, rank in fd.most_common(500): freqs.append(rank)  # 计算排名前 500 的词的出现次数
plt.subplot(2, 1, 1); plt.plot(range(500), freqs)
plt.subplot(2, 1, 2); plt.loglog(range(500), freqs)  # 在 log-log 图中展示词序和词频的关系
plt.xlabel('rank(r)', fontsize=14, fontweight='bold')
plt.ylabel('frequenly(f)', fontsize=14, fontweight='bold')
plt.grid(True)
plt.show()
