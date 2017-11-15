#!/usr/bin/python3
# coding: utf-8
# SnowNLP 是一个 python 写的类库, 可以方便的处理中文文本内容, 是受到了 TextBlob 的启发而写的, 由于现在大部分的自然语言处理库基本都是针对英文的,
# 于是写了一个方便处理中文的类库, 并且和 TextBlob 不同的是, 这里没有用 NLTK , 所有的算法都是自己实现的, 并且自带了一些训练好的字典
# 注意本程序都是处理的 unicode 编码, 所以使用时请自行 decode 成 unicode
from snownlp import SnowNLP
s = SnowNLP(u'这个东西真心很赞')  # Python2 中要用 u'' 来转成 unicode, Python3 中默认就是 Unicode
print(s.words)  # ['这个', '东西', '真心', '很', '赞']
print(s.keywords())  # ['赞', '很', '真心', '东西']
print(s.summary())  # ['这个东西真心很赞']; 对文章进行梗概, 这里只有一句话, 所以是本身
print(list(s.tags))  # [('这个', 'r'), ('东西', 'n'), ('真心', 'd'), ('很', 'd'), ('赞', 'Vg')]
print(s.sentiments)  # 0.9769663402895832 positive 的概率
print(s.pinyin)  # ['zhe', 'ge', 'dong', 'xi', 'zhen', 'xin', 'hen', 'zan']
## 找出 keywords 中的 名词
print([word for word in s.keywords() if dict(s.tags)[word] == 'n'])  # dict(s.tags) 不是函数, 不能加 ()
##################################################################
## 繁体字处理
s = SnowNLP(u'「繁體字」「繁體中文」的叫法在臺灣亦很常見。')
print(s.han)  # u'「繁体字」「繁体中文」的叫法在台湾亦很常见。'
##################################################################
## 处理一段文本 keywords(), summary() 两个重量级的函数
text = u'''
自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。
它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。
自然语言处理是一门融语言学、计算机科学、数学于一体的科学。
因此, 这一领域的研究将涉及自然语言, 即人们日常使用的语言,
所以它与语言学的研究有着密切的联系, 但又有重要的区别。
自然语言处理并不是一般地研究自然语言,
而在于研制能有效地实现自然语言通信的计算机系统,
特别是其中的软件系统。因而它是计算机科学的一部分。
'''
s = SnowNLP(text)
print(s.keywords(3))  # [u'语言', u'自然', u'计算机']
print(s.summary(5))  # [u'因而它是计算机科学的一部分',
                #  u'自然语言处理是一门融语言学、计算机科学、数学于一体的科学',
				#  u'自然语言处理是计算机科学领域与人工智能领域中的一个重要方向']
print(s.sentences)  # 输出所有的句子
##################################################################
## 处理 str list; tf-idf
s = SnowNLP([[u'这篇', u'文章'],
             [u'那篇', u'论文'],
             [u'这个']])
print(s.tf)  # [{'这篇': 1, '文章': 1}, {'那篇': 1, '论文': 1}, {'这个': 1}]
print(s.idf)  # {'这篇': 0.5108256237659907, '文章': 0.5108256237659907, '那篇': 0.5108256237659907, '论文': 0.5108256237659907, '这个': 0.5108256237659907}
print(s.sim([u'文章']))  # [0.4686473612532025, 0, 0]
##################################################################
## 实战
text = u"我今天很快乐。我今天很愤怒。"
s = SnowNLP(text)
print(s.sentiments)
for sentence in s.sentences:
    print(sentence)  # 没有标点
    sent = SnowNLP(sentence)
    print(sent.keywords())
    print(sent.sentiments)
# 我今天很快乐
# 0.971889316039116
# 我今天很愤怒
# 0.07763913772213482  # 表达正面情感的概率
