#!/usr/bin/python3
# coding: utf-8
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import CountVectorizer  # compute a simple word frequency, 创建词袋数据结构
from sklearn.feature_extraction.text import TfidfTransformer
##################################################################
## 训练集 和 停用词表
corpus = ["我 来到 北京 中国 科学院",  # 第一个文档切词后的结果, 词之间以空格隔开
    "他 来到 了 北京",                 # 第二个文档切词结果
    "小明 毕业 于 中国 科学院"]        # 第三个文档切词结果
stpwrdlst = ['了', '我']  # 一个字符长度的词会自动过滤掉
##################################################################
## HashingVectorizer()
hash_vec = HashingVectorizer(stop_words=stpwrdlst, n_features=10000)  # Hash 向量词袋; 设置停用词词表, 设置最大维度 10000
X = hash_vec.fit_transform(corpus); print(X, '\n'); print(X.toarray())
print(X[0])  # 稀疏矩阵也可以输出
##################################################################
## CountVectorizer(analyzer="word", preprocessor=None, tokenizer=None, stop_words=None, max_features=5000) 将文本中的词语转换为词频矩阵, 矩阵元素 a[i][j] 表示 j 词在 i 个文档里的词频
# analyzer="word" indicates the feature we are using are words;
# preprocessor=None, tokenizer=None and stop_words=None mean the data needes no more
#     preprocessing, tokenization and removing stop sords since we've already done these in the Data Cleaning and Text Processing step;
# max_features=5000 means we only take the top 5000 frequent words as our words in the bag
#     thus limiting the size of the feature vector and speeding up the modeling process.
count_vec = CountVectorizer(stop_words=stpwrdlst)                        # 词频向量词袋; 默认也有 stop_words
X = count_vec.fit_transform(corpus); print(X, '\n'); print(X.toarray())  # 计算个词语出现的次数

## 训练后模型的属性
wordlist = count_vec.get_feature_names(); print(wordlist)  # ['中国', '北京', '小明', '来到', '毕业', '科学院']; 自动将 1 个长度的过滤了...
word_dic = count_vec.vocabulary_; print(word_dic)  # {'来到': 3, '北京': 1, '中国': 0, '科学院': 5, '小明': 2, '毕业': 4}; 反向索引字典
# 每个文档的长度都是 wordlist(字典) 的长度, 字典中的次出现了, 就在对应的位置记为 1

## 转换后的数据属性
print(type(X), type(X.data))  # <class 'scipy.sparse.csr.csr_matrix'>, <class 'numpy.ndarray'>; 稀疏矩阵 csr..., 好开心
print(X.shape)  # (3, 6); 文档数, 单词数; 上面的 wordlist 正好有 6 个数
print(X.data)  # [1 1 1 1 1 1 1 1 1 1]; 只是把稀疏矩阵中的数提取出来了, 没什么用
print(X.toarray())  # [[1 1 0 1 0 1] [0 1 0 1 0 0] [1 0 1 0 1 1]]; 打印出来在 REPL 中看, 一列为一个 feature
# Each row in the array is one of your original documents (strings), each column is a feature (word),
# and the element is the count for that particular word and document.
# You can see that if you sum each column you'll get the correct number
print(X.toarray().sum(axis=0))  # [2 2 1 2 1 2]; 对应于 wordlist 分别的个数
print(X.toarray().sum(axis=0)[count_vec.vocabulary_.get('北京')])  # 2; 得到 '北京' 出现次数
print(X.toarray().sum(axis=0)[count_vec.vocabulary_['北京']])  # 2; 字典还可以这样查值
#################################
## Counter
from collections import Counter
c = Counter([word for line in corpus for word in line.split()])
print(c)  # Counter({'来到': 2, '北京': 2, '中国': 2, '科学院': 2, '我': 1, '他': 1, '了': 1, '小明': 1, '毕业': 1, '于': 1})
print(c['北京'])  # 2
#################################
## 总结:
# 1. CountVectorizer 会自动 split(), 传进去的是 list[long-str]
# 2. Counter 不会进行 split(), 传进去的时候要处理好
# 3. Honestly though, I'd suggest using collections.Counter or something from NLTK,
#    unless you have some specific reason to use scikit-learn, as it'll be simpler.
# 4. 只是统计词频的话, 用 Counter 比较简单, 但是用到朴素贝叶斯的时候还是 CountVectorizer 方便一些...
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
