#!/usr/bin/python3
# coding: utf-8
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
##################################################################
## 训练集 和 停用词表
corpus = ["我 来到 北京 中国 科学院",  # 第一个文档切词后的结果, 词之间以空格隔开
    "他 来到 了 北京",                 # 第二个文档切词结果
    "小明 毕业 于 中国 科学院"]        # 第三个文档切词结果
stpwrdlst = ['了', '我']
##################################################################
## HashingVectorizer()
hash_vec = HashingVectorizer(stop_words=stpwrdlst, n_features=10000)  # Hash 向量词袋; 设置停用词词表, 设置最大维度 10000
X = hash_vec.fit_transform(corpus); print(X, '\n'); print(X.toarray())
print(X[0])  # 稀疏矩阵也可以输出
##################################################################
## CountVectorizer() 将文本中的词语转换为词频矩阵, 矩阵元素 a[i][j] 表示 j 词在 i 个文档里的词频
count_vec = CountVectorizer(stop_words=stpwrdlst)                        # 词频向量词袋; 默认也有 stop_words
X = count_vec.fit_transform(corpus); print(X, '\n'); print(X.toarray())  # 计算个词语出现的次数
wordlist = count_vec.get_feature_names(); print(wordlist)  # ['中国', '北京', '小明', '来到', '毕业', '科学院']; 自动将 1 个长度的过滤了...
word_dic = count_vec.vocabulary_; print(word_dic)  # {'来到': 3, '北京': 1, '中国': 0, '科学院': 5, '小明': 2, '毕业': 4}; 反向索引字典
# 每个文档的长度都是 wordlist(字典) 的长度, 字典中的次出现了, 就在对应的位置记为 1
##################################################################
## TfidfTransformer() 统计 vectorizer 中每个词语的 tf-idf 权值, 矩阵元素 a[i][j] 表示 j 词在 i 类文本中的 tf-idf 权重
tfidf_tra = TfidfTransformer()
tfidf = tfidf_tra.fit_transform(X)
weightarray = tfidf.toarray(); print(weightarray.shape, '\n', weightarray)  # (3, 6)
idflist = tfidf_tra.idf_; print(idflist)  # [ 1.28768207  1.28768207  1.69314718  1.28768207  1.69314718  1.28768207]
print(tfidf_tra.idf_[count_vec.vocabulary_['北京']])  # 1.28768207245; ** 单个词语 idf 查询 **; 下面是查询所有的
print('\n'.join([' '.join([str((item, weightarray[i][count_vec.vocabulary_[item]])) for item in wordlist]) for i in range(len(weightarray))]))

# tf_ij = n_ij / sigma_k(n_kj)  # n_ij 是 特征词 t_i 在文本 d_j 中出现的次数; 就是 X[i][j] / sum(X[i])

# idf_ij = log(D / (1 + D_t_i))  # D 表示语料中文档总数, D_t_i 表示包含 t_i 的文档的数量

# tfidf = tf * idf = 0.25 * 4 / 2 = 0.5, 计算北京的 tfidf 不知道为什么有差值
