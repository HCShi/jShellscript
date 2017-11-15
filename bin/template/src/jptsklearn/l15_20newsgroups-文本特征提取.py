#!/usr/bin/python3
# coding: utf-8
# 参考: [[Scikit-learn教程] 03.01 文本处理：特征提取](https://jizhi.im/blog/post/sklearntutorial0301), 已存盘
from sklearn.datasets import fetch_20newsgroups  # 20newsgroups 简介见 ./l14_数据获取-urllib-tarfile-loadfile_20newsgroups.py
categories = ["alt.atheism", "soc.religion.christian", "comp.graphics", "sci.med"]  # 选取需要下载的新闻分类
twenty_train = fetch_20newsgroups(subset="train", categories=categories, shuffle=True, random_state=42)  # 下载并获取训练数据, 也是先全部下载, 再提取部分
print(twenty_train.target_names)  # ['alt.atheism', 'comp.graphics', 'sci.med', 'soc.religion.christian']
##################################################################
## 提取文本特征
# 无论是什么机器学习方法, 都只能针对向量特征 (也就是一系列的数字组合) 进行分析, 因此在读取文本之后, 我们要将文本转化为数字化的特征向量.
##################################################################
## 词袋模型 (Bags of words)
# 为训练集文档中所有出现的词语给予一个固定的数字 ID (也就是为所有的词语建立一个由整数进行索引的字典)
# 对于每一篇文档 #i, 计算每个词语 w 出现的次数并将其记录在 X[i, j] 中作为特征 #j 的值, j 代表词语 w 在字典中 ID
# 词袋模型假设每个数据集中存在 n_features 个不同的单词, 而这个数字通常会超过 100000. 这会带来什么问题呢?
# 考虑一下, 如果采样数(也就是文档的个数)为 10000, 特征以 32 位浮点数存储, 则总的文本特征需要 10000 × 100000 × 4bytes=4GB,
# 而这 4GB 必须全部存储在计算机内存中, 这对于现在的计算机而言几乎是不可能的.

# 幸运的是, 上述方法得到的特征数据中大部分特征数值都会是零值, 这是因为每篇文档实际上仅使用了几百个不同的词汇.
# 由于这个原因, 我们将词袋模型称之为高维度稀疏数据集. 我们可以通过仅存储非零特征来大幅节省内存使用量.
# scipy.sparse 模型正是处理这个过程的一系列数据结构, 而它们也得到了 scikit-learn 的支持.
##################################################################
## 1. 使用 scikit-learn 标记文本
# 一个高效的数据处理模块会包含文本与处理、标记和停词 (stopwords, 指对句意无影响的虚词, 如 "的" 、 "地" 等等) 过滤等功能,
# 这些功能能够帮助我们将文本数据转换为特征向量, 从而建立起数据的特征字典.
# CountVectorizer 就是一个支持文本中词语计数的函数库, 我们可以使用其中的函数来分析文本数据来得到特征向量字典,
# 字典中每一个项目的值代表该词语在全部数据中出现的次数
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print(len(twenty_train.data))  # 2257; 篇文档
print(X_train_counts.shape)  # (2257, 35788); 35788 个单词
print(count_vect.vocabulary_.get(u'algorithm'))  # 4690; algorithm id
print(X_train_counts.toarray().sum(axis=0)[count_vect.vocabulary_.get('algorithm')])  # 90; algorithm 出现次数
##################################################################
## 从出现次数到频率分析
# 统计词语的出现次数是个很好的尝试, 但这也同样存在一个问题, 那就是对于一个词语而言, 它在较长篇幅的文章出现的概率往往会比短文章高得多,
# 即便是这两篇文章讨论的是同一个话题, 这个现象同样存在

# 为了解决这些潜在的差异, 我们可以尝试用 **每个词语在某个文档中出现的次数除以这个文档中总共的词语数目**,
# 这样得到的新的特征我们可以称之为 tf, 也就是词频 **(Term Frequencies)**

# 在 tf 基础上的另外一种优化方案是为某些不太重要的词语降低权重, 这些词语往往会在很多文档中出现,
# 相对于那些仅在一小部分文档中出现的词语而言, 它们对于分类的影响会更细微
# 我们把这种 **词频 + 权重** 模型称之为 tf-idf, 也就是 "Term Frequency times Inverse Document Frequency"; 下面我们简要介绍它们的数学意义

# 逆向文件频率 (inverse document frequency, idf) 是一个词语普遍重要性的度量.
# 某一特定词语的 idf, 可以由 **总文件数目除以包含该词语之文件的数目, 再将得到的商取对数**
# tfidf = tf * idf -> 该单词在当前文档中的频率 * 一个常数 -> 所以 tfidf 是一个 (n, m) 的矩阵
# 就对应上面提到的 X[i, j], 第 i 篇文章中 id 为 j 的单词的重要程度, 也就是文本特征
print(len(twenty_train.data))  # 2257; 篇文档
print(X_train_counts.shape)  # (2257, 35788); 35788 个单词
##################################################################
## 2. TF-IDF 提取文本特征
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)  # 这里依赖于 1. 使用 scikit-learn 标记文本 中生成的 [文档, 词汇] 矩阵
print(X_train_tfidf.shape)  # (2257, 35788)
