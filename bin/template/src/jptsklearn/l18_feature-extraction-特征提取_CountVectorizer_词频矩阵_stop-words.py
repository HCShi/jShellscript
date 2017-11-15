#!/usr/bin/python3
# coding: utf-8
from sklearn.feature_extraction.text import CountVectorizer  # compute a simple word frequency, 创建词袋数据结构
##################################################################
## 模型参数
vectorizer = CountVectorizer(analyzer="word", preprocessor=None, tokenizer=None, stop_words=None, max_features=5000)  # 除了 max_features 其他的都是默认值
# analyzer="word" indicates the feature we are using are words;
# preprocessor=None, tokenizer=None and stop_words=None mean the data needes no more
#     preprocessing, tokenization and removing stop sords since we've already done these in the Data Cleaning and Text Processing step;
# max_features=5000 means we only take the top 5000 frequent words as our words in the bag
#     thus limiting the size of the feature vector and speeding up the modeling process.
##################################################################
## CountVectorizer
texts = ["dog cat fish","dog cat cat","fish bird", 'bird']  # 4 篇文档, 共 4 个单词
cv = CountVectorizer()  # 模型参数中会存放 单词 等信息, 所以必须单独赋予变量;
cv_fit = cv.fit_transform(texts)  # 训练完毕, fit_transform() 是将文本转为词频矩阵

# cv 模型属性
print(cv.get_feature_names())  # ['bird', 'cat', 'dog', 'fish']; 将所有特征提取出来; 获取词袋模型中的所有词
print(cv.vocabulary_)  # {'dog': 2, 'cat': 1, 'fish': 3, 'bird': 0}; 一个 dict, 只是映射 feature 的顺序

# cv_fit 训练结果数据的属性
print(type(cv_fit), type(cv_fit.data))  # <class 'scipy.sparse.csr.csr_matrix'>, <class 'numpy.ndarray'>
print(cv_fit.shape)  # (4, 4); 文档数, 单词数
print(cv_fit.data)  # [1 1 1 2 1 1 1 1]; 只是把稀疏矩阵中的数提取出来了, 没什么用
print(cv_fit.toarray())  # [[0 1 1 1] [0 2 1 0] [1 0 0 1] [1 0 0 0]]; 打印出来在 REPL 中看, 一列为一个 feature
# Each row in the array is one of your original documents (strings), each column is a feature (word),
# and the element is the count for that particular word and document.
# You can see that if you sum each column you'll get the correct number
print(cv_fit.toarray().sum(axis=0))  # [2 3 2 2]; 对应于 ['bird', 'cat', 'dog', 'fish'] 分别的个数
print(cv_fit.toarray().sum(axis=0)[cv.vocabulary_.get('cat')])  # 3; 得到 'cat' 出现次数
print(cv_fit.toarray().sum(axis=0)[cv.vocabulary_['cat']])  # 3; 字典还可以这样查值
##################################################################
## stop word
stpwrdlst = ['dog']
cv = CountVectorizer(stop_words=stpwrdlst)
cv_fit = cv.fit_transform(texts)  # 训练完毕, fit_transform() 是将文本转为词频矩阵
print(cv.get_feature_names())  # ['bird', 'cat', 'fish']
print(cv_fit.toarray())  # [[0 1 1] [0 2 0] [1 0 1] [1 0 0]]

# Honestly though, I'd suggest using collections.Counter or something from NLTK,
# unless you have some specific reason to use scikit-learn, as it'll be simpler.
# 只是统计词频的话, 用 Counter 比较简单, 但是用到朴素贝叶斯的时候还是 CountVectorizer 方便一些...
##################################################################
## Counter
from collections import Counter
c = Counter([word for line in texts for word in line.split()])
print(c)  # Counter({'cat': 3, 'dog': 2, 'fish': 2, 'bird': 2})
print(c['cat'])  # 3
##################################################################
## 总结:
# 1. CountVectorizer 会自动 split(), 传进去的是 list[long-str]
# 2. Counter 不会进行 split(), 传进去的时候要处理好
