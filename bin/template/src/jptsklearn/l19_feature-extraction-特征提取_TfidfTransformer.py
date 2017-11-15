#!/usr/bin/python3
# coding: utf-8
# 具体解释见 ./l15_20newsgroups-文本特征提取.py
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
##################################################################
## 训练集 和 停用词表
corpus=["我 来到 北京 清华大学 了",   # 第一个文档切词后的结果, 词之间以空格隔开
    "他 来到 了 网易 杭研 大厦",      # 第二个文档切词结果
    "小明 硕士 毕业 与 中国 科学院",  # 第三个文档切词结果
    "我 爱 得 北京 天安门"]           # 第四个文档切词结果
stpwrdlst = ['了', '我']
##################################################################
## 将文本中的词语转换为词频矩阵, 矩阵元素 a[i][j] 表示 j 词在 i 个文档里的词频
vectorizer = CountVectorizer(stop_words=stpwrdlst)  # 创建词袋数据结构
# 创建 hash 向量词袋
# vectorizer = HashingVectorizer(stop_words =stpwrdlst, n_features = 10000)  # 设置停用词词表, 设置最大维度 10000
##################################################################
## 统计每个词语的 tf-idf 权值
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))  # 第一个 fit_transform 是计算 tf-idf, 第二个 fit_transform 是将文本转为词频矩阵
wordlist = vectorizer.get_feature_names()  # 获取词袋模型中的所有词
# tf-idf 矩阵 元素 a[i][j]表示 j 词在 i 类文本中的 tf-idf 权重
weightlist = tfidf.toarray()
# 打印每类文本的 tf-idf 词语权重, 第一个 for 遍历所有文本, 第二个 for 便利某一类文本下的词语权重
for i in range(len(weightlist)):
    print("-------这里输出第", i, "个文档中词语 tf-idf 权重------")
    for j in range(len(wordlist)):
        print(wordlist[j], weightlist[i][j])
# -------这里输出第 0 个文档中词语 tf-idf 权重------
# 中国 0.0; 北京 0.52640543361; 大厦 0.0; 天安门 0.0; 只去了部分的
# tfidf = tf * idf = 0.25 * 4 / 2 = 0.5, 计算北京的 tfidf 不知道为什么有差值

# 查看 idf
print(transformer.idf_[vectorizer.vocabulary_['北京']])  # 1.51082562377
