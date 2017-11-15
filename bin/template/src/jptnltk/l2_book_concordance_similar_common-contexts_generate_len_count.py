#!/usr/bin/python3
# coding: utf-8
from nltk import book  # 会引入 text1 - text9, texts; sent1 - sent9, sents
# Loading text1, ..., text9 and sent1, ..., sent9
# Type the name of the text or sentence to view it.
# Type: 'texts()' or 'sents()' to list the materials.
##################################################################
## book 数据结构窥探
print(book.texts())  # 会显示 from nltk import book 相似的内容
print(book.sents())
print(book.text1)  # <Text: Moby Dick by Herman Melville 1851>; 白鲸 作者 1851
print(book.text1[100])  # and; 重写了 list 的相关方法
print(book.gutenberg)  # <PlaintextCorpusReader in '/home/coder352/nltk_data/corpora/gutenberg'>
print(type(book.text1))  # <class 'nltk.text.Text'>
print(len(book.text1))  # 260819; 可以看做一个 list 的封装
print(len(book.text1.tokens))  # 260819 个 Token
# text1 原文在: ~/nltk_data/corpora/gutenberg/melville-moby_dick.txt
# text2 原文在: ~/nltk_data/corpora/gutenberg/austen-sense.txt
# text3 创世纪: Genesis
# text4 语料库(历任美国总统就职演说); ~/nltk_data/corpora/inaugural/
##################################################################
## text.concordance(word) 查询单词
book.text1.concordance('monstrous')  # Displaying 11 of 11 matches; 会将 monstrous 放到中间
##################################################################
## text.similar(word) 用来识别文章中和搜索词相似的词语, 可以用在搜索引擎中的相关度识别功能中
book.text1.similar("monstrous")  # 查询出了 text1 中与 monstrous 相关的所有词语
# true contemptible christian abundant few part mean careful puzzled...; 好神奇
##################################################################
## text.common_contexts(words) 列出用法相似词语前后的词语, 所比较的词语用 "_" 表示; 这里 words 是 list 类型
print(book.text2.name)  # Sense and Sensibility by Jane Austen 1811
# Austen 使用这些词与 Melville 完全不同; 在她那里, monstrous 是正面的意思, 有时它的功能像词 very 一样作强调成分
book.text2.concordance('monstrous')
book.text2.concordance('very')  # 下面就展示了 monstrous 作为 very 意思的时候的上下文
book.text2.common_contexts(["monstrous", "very"])  # a_pretty am_glad a_lucky is_pretty be_glad; 在 text1 中竟然没有
##################################################################
## text.dispersion_plot(words) 查看词语在一篇语料中的位置分布
# 这个函数会调用 Numpy 和 Matplotlib 程序包; 虽然绘制的是物理位置分布, 但是如果语料中的文本按一定顺序排列,
# 绘制结果可以用来研究在预定排列空间里的分布规律; 比如文本按时间排列, 则可以用来研究词语的历时演化
# 作为练习, 我绘制了 book.text4 语料库(历任美国总统就职演说)中 government 和 democray 的分布图
book.text4.dispersion_plot(["government", "democray"])  # 结果很有深意啊……
##################################################################
## text.generate() 用来自动生成文章
print(book.text3.generate())  # 3.0 以后不支持了
##################################################################
## len() 可以用于判断重复词密度
print(len(book.text3))  # 44764 个 token
print(len(set(book.text3)))  # 2789 个没有重复
print(len(book.text3) / len(set(book.text3)))  # 16.050197203298673
# 正文字数/不重复词语字数 = 16, 说明有 15/16 是无效字符
print(sorted(set(book.text3))[:5])  # ['!', "'", '(', ')', ',']; 最多的是符号
##################################################################
## count() 可以用于判断关键词密度
print(book.text3.count('smote') / len(book.text3))  # 0.00011169689929407559
print(book.text4.count('United States'))  # 0; 不支持短语查询
##################################################################
## collocations(num=20, window_size=2); Collocations and Bigrams; 类似于 Bigrams, 见 ./l22_bigrams
book.text4.collocations()  # 默认输出前 20 个
# United States; fellow citizens; four years; years ago; Federal
# Government; General Government; American people; Vice President; Old
# World; Almighty God; Fellow citizens; Chief Magistrate; Chief Justice;
# God bless; every citizen; Indian tribes; public debt; one another;
# foreign nations; political parties
