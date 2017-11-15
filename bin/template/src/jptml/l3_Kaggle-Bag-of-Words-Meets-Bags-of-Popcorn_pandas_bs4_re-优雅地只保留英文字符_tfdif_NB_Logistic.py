#!/usr/bin/python3
# coding: utf-8
# ./l2_Kaggle-Bag-of-Words-Meets-Bags-of-Popcorn 采用的深度学习, 而且数据是 Keras 自带的已经数值化了的;
# 参考: [NLP系列(4)_朴素贝叶斯实战与进阶](http://blog.csdn.net/han_xiaoyang/article/details/50629608)
# 这里将从原数据开始, 一步步的进行...; 选用 NB 和 Logistic 对比 而不是 DL
# Kaggle 原文引导里是用 word2vec 的方式将词转为词向量, 后再用 deep learning 的方式做的.
# 深度学习好归好, 但是毕竟耗时耗力耗资源, 我们用最最 naive 的朴素贝叶斯撸一把, 说不定效果也能不错, 不试试谁知道呢.
# 另外, 朴素贝叶斯建模真心速度快, 很多场景下, 快速建模快速迭代优化正是我们需要的嘛
##################################################################
## 数据观测
# labeledTrainData 情绪标签的训练数据; 包括 id, sentiment 和 review 3 个部分, 分别指代用户 id, 情感标签, 评论内容
# unlabeledTrainData 没有情绪标签的训练数据
# testData 测试数据
# head -n 2 labeledTrainData.tsv  # 显示如下
#     id      sentiment       review
#     "5814_8"        1       "With all this stuff going down at the  # 带有 </br> 等 html 标签
# wc labeledTrainData.tsv # 25001  5893023 33556378 labeledTrainData.tsv
# wc testData.tsv         # 25001  5736720 32724746 testData.tsv; 第一行是 header
import re
from bs4 import BeautifulSoup
import pandas as pd
def review_to_wordlist(review):  # 把 IMDB 的评论转成词序列
    review_text = BeautifulSoup(review, 'html.parser').get_text()  # 去掉 HTML 标签, 拿到内容
    review_text = re.sub("[^a-zA-Z]", " ", review_text)  # 为什么不直接用 '', 而是 ' ', 因为可能有 a-b 这种连字符, 要分开
    return review_text.lower().split()  # 小写化所有的词, 并转成词 list, 返回
##################################################################
## 预处理数据; 比如说把评论部分的 html 标签去掉等等
train = pd.read_csv('./tmp_dataset/Kaggle-Bag-of-Words-Meets-Bags-of-Popcorn/labeledTrainData.tsv', header=0, delimiter="\t", quoting=3)
test = pd.read_csv('./tmp_dataset/Kaggle-Bag-of-Words-Meets-Bags-of-Popcorn/testData.tsv', header=0, delimiter="\t", quoting=3 )
y_train = train['sentiment']  # 取出情感标签,  positive/褒 或者 negative/贬, 真方便
# 将训练和测试数据都转成词 list, 每一项还是很长的 str 评论, 但是去掉了非英文字符
train_data = []
for i in range(0, len(train['review'])): train_data.append(" ".join(review_to_wordlist(train['review'][i])))
test_data = []
for i in range(0, len(test['review'])): test_data.append(" ".join(review_to_wordlist(test['review'][i])))
print(train_data[0])  # with all this stuff...; 居然 2000 个字节
##################################################################
## 特征处理; 数据有了, 我们得想办法从数据里面拿到有区分度的特征
# 比如说 Kaggle 该问题的引导页提供的 word2vec 就是一种文本到数值域的特征抽取方式;
# TF-IDF(term frequency-interdocument frequency)向量. 每一个电影评论最后转化成一个 TF-IDF 向量.
# TF-IDF 是一种统计方法, 用以评估一字词(或者 n-gram)对于一个文件集或一个语料库中的其中一份文件的重要程度.
# 字词的重要性随着它在文件中出现的次数成正比增加, 但同时会随着它在语料库中出现的频率成反比下降.
# 同时我在单词的级别上又拓展到 2 元语言模型(对这个不了解的同学别着急, 后续的博客介绍马上就来)
# 恩, 你可以再加 3 元 4 元 语言模型; 主要是单机内存不够了, 先就 2 元 上, 凑活用吧
from sklearn.feature_extraction.text import TfidfVectorizer as TFIV
# 初始化 TFIV 对象, 去停用词, 加 2 元语言模型
tfv = TFIV(min_df=3, token_pattern=r'\w{1,}', ngram_range=(1, 2), sublinear_tf=1)  # 这里的 token_pattern 还不是很懂..
X_all, len_train = train_data + test_data, len(train_data); print(len(X_all))  # 50000; 合并训练和测试集以便进行 TFIDF 向量化操作
X_all = tfv.fit_transform(X_all)  # 这一步有点慢, 去喝杯茶刷会儿微博知乎歇会儿..., ./l2.py 中直接从这不的下一步开始的...
X, x_test = X_all[:len_train], X_all[len_train:]  # 恢复成训练集和测试集部分
##################################################################
## 多项式朴素贝叶斯 vs 逻辑回归
# 特征现在我们拿到手了, 该建模了, 好吧, 博主折腾劲又上来了, 那个我们还是朴素贝叶斯和逻辑回归都建个分类器吧, 然后也可以比较比较
# 『 talk is cheap, I’ ll show you the code 』
from sklearn.naive_bayes import MultinomialNB as MNB
from sklearn.model_selection import cross_val_score
import numpy as np
print("多项式贝叶斯分类器 20 折交叉验证得分: ", np.mean(cross_val_score(MNB(), X, y_train, cv=20, scoring='roc_auc')))  # 设定打分为 roc_auc
# 多项式贝叶斯分类器 20 折交叉验证得分: 0.950837239
##################################################################
# 折腾一下逻辑回归
from sklearn.linear_model import LogisticRegression as LR
from sklearn.model_selection import GridSearchCV
grid_values = {'C': [30]}  # 设定 grid search 的参数
model_LR = GridSearchCV(LR(penalty='l2', dual=True, random_state=0), grid_values, scoring = 'roc_auc', cv = 20)  # 设定打分为 roc_auc
model_LR.fit(X, y_train)  # 数据灌进来; 20 折交叉验证, 开始漫长的等待...
print(model_LR.cv_results_['mean_test_score'])  # [ 0.96461414]; cv_results_ 还有很多属性
# 看似逻辑回归在这个问题中, TF-IDF 特征下表现要稍强一些, 不过同学们自己跑一下就知道, 这 2 个模型的训练时长真心不在一个数量级,
# 逻辑回归在数据量大的情况下, 要等到睡着
# 另外, 要提到的一点是, 因为我这里只用了 2 元语言模型(2-gram), 加到 3-gram 和 4-gram, 最后两者的结果还会提高,
# 而且朴素贝叶斯说不定会提升更快一点, 内存够的同学们自己动手试试吧^_^
