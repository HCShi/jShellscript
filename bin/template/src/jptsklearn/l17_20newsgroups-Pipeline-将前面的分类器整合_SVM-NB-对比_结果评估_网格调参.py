#!/usr/bin/python3
# coding: utf-8
# 对 ./l15_20newsgroups-文本特征提取.py ./l16_20newsgroups-分类与优化.py 两篇的简化, 并加入了 SVM, 结果测试, 网格调参
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.datasets import fetch_20newsgroups  # 20newsgroups 简介见 ./l14_数据获取-urllib-tarfile-loadfile_20newsgroups.py
##################################################################
## 准备数据
categories = ["alt.atheism", "soc.religion.christian", "comp.graphics", "sci.med"]  # 选取需要下载的新闻分类
twenty_train = fetch_20newsgroups(subset="train", categories=categories, shuffle=True, random_state=42)  # 下载并获取训练数据, 也是先全部下载, 再提取部分
print(twenty_train.target_names)  # ['alt.atheism', 'comp.graphics', 'sci.med', 'soc.religion.christian']
print(len(twenty_train.data))  # 2257; 篇文档
##################################################################
## 建立 Pipeline
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', MultinomialNB()),])
text_clf = text_clf.fit(twenty_train.data, twenty_train.target)  # 训练分类器
import numpy as np
##################################################################
## 使用测试数据评估分类器性能
twenty_test = fetch_20newsgroups(subset="test", categories=categories, shuffle=True, random_state=42)
predicted = text_clf.predict(twenty_test.data)  # 使用测试数据进行分类预测
print(np.mean(predicted == twenty_test.target))  # 0.834886817577; 计算预测结果的准确率
##################################################################
## 总结:
# 1. 代码如此简介, 世界一下子啊清净了...

##################################################################
## 下面换成 SVM 接着搞事情
##################################################################
# 如果正常运行上述代码, 我们应该可以得到 83.4% 的准确率;
# 我们有很多办法来改进这个成绩, 使用业界公认的最适于文本分类的算法——支持向量机 (SVM, Support Vector Machine) 就是一个很好的方向
# (虽然它会比朴素贝叶斯稍微慢一点); 我们可以通过改变 Pipeline 中分类器所指定的对象轻松地实现这一点
from sklearn.linear_model import SGDClassifier
text_clf_2 = Pipeline([('vect', CountVectorizer()),
                       ('tfidf', TfidfTransformer()),
                       ('clf', SGDClassifier(loss='hinge',
                                             penalty='l2',
                                             alpha=1e-3,
                                             max_iter=5,
                                             random_state=42)),])
text_clf_2.fit(twenty_train.data, twenty_train.target)
predicted = text_clf_2.predict(twenty_test.data)
print(np.mean(predicted == twenty_test.target))  # 0.912782956059; SVM 比 NB 效果好!!!
##################################################################
## 对于预测结果的详细评估
##################################################################
# Scikit-learn 提供了更多的评测工具来更好地帮助我们进行分类器的性能分析, 如下所示
# 我们可以得到预测结果中关于每一种分类的准确率、召回率、 F 值等等以及它们的混淆矩阵
from sklearn import metrics
print(twenty_train.target_names)  # ['alt.atheism', 'comp.graphics', 'sci.med', 'soc.religion.christian']
print(metrics.classification_report(twenty_test.target, predicted, target_names=twenty_test.target_names))
# 打印分类性能指标:
#                         precision    recall  f1-score   support
#
#            alt.atheism       0.95      0.81      0.87       319
#          comp.graphics       0.88      0.97      0.92       389
#                sci.med       0.94      0.90      0.92       396
# soc.religion.christian       0.90      0.95      0.93       398
#
#            avg / total       0.92      0.91      0.91      1502
print(metrics.confusion_matrix(twenty_test.target, predicted))
# 打印混淆矩阵
# [[258  11  15  35]  # alt.atheism: 11 个预测成了 graphics; 15 个预测成了 sci.med; 35 个预测成了 christian
#  [  4 379   3   3]  # 以此类推
#  [  5  33 355   3]
#  [  5  10   4 379]]
# 不出所料, 通过混淆矩阵我们可以发现, 相对于计算机图形学 (comp.graphics), 与无神论 (alt.atheism)
# 以及基督教 (soc.religion.christian) 相关的两种分类更难以被区分出来; 从 35 的可以看出来
##################################################################
## 使用网格搜索来进行参数优化
##################################################################
# 我们已经了解了很多机器学习过程中所遇到的参数, 比如 TfidfTransformer 中的 use_idf
# 分类器往往会拥有很多的参数, 比如说朴素贝叶斯算法中包含平滑参数 alpha, SVM 算法会包含惩罚参数 alpha 以及其他一些可以设置的函数
# 为了避免调整这一系列参数而带来的繁杂工作, 我们可以使用网格搜索方法来寻找各个参数的最优值

# 如下面的例子所示, 我们可以在采用 SVM 算法建立分类器时尝试设置如下参数:
# 使用单词或是使用词组、使用 IDF 或是不使用 IDF 、惩罚参数为 0.01 或是 0.001
from sklearn.model_selection import GridSearchCV
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],  # 设置参与搜索的参数
              'tfidf__use_idf': (True, False),
              'clf__alpha': (1e-2, 1e-3),}
gs_clf = GridSearchCV(text_clf, parameters, n_jobs=-1)  # 构建分类器

# 很明显, 逐个进行这样一个搜索过程会消耗较大的计算资源;
# 如果我们拥有一个多核 CPU 平台, 我们就可以并行计算这 8 个任务(每个参数有两种取值, 三个参数共有 2^3=8 个参数组合)
# 这需要我们修改 n_jobs 这个参数
# 如果我们设置这个参数的值为 -1, 网格搜索过程将会自动检测计算环境所存在的 CPU 核心数量, 并使用全部核心进行并行工作
# 一个具体的网格搜索模型与普通的分类器模型一致, 我们可以使用一个较小的子数据块来加快模型的训练过程
# 对 GridSearchCV 对象调用 fit 方法之后将得到一个与之前案例类似的分类器, 我们可以使用这个分类器来进行预测
gs_clf = gs_clf.fit(twenty_train.data[:400], twenty_train.target[:400])  # 使用部分训练数据训练分类器
# 查看分类器对于新文本的预测结果, 你可以自行改变下方的字符串来观察分类效果
print(twenty_train.target_names[gs_clf.predict(['An apple a day keeps doctor away'])[0]])  # alt.atheism

# 分类器同时包含 best_score_和 best_params_两个属性, 这两个属性包含了最佳预测结果以及取得最佳预测结果时的参数配置
# 当然, 我们也可以浏览 gs_clf.cv_results_ 来获取更详细的搜索结果 (这是 sklearn 0.18.1 版本新加入的特性)
# 这个参数可以很容易地导入到 pandas 中进行更为深入的研究
gs_clf = gs_clf.fit(twenty_train.data[:400], twenty_train.target[:400])
print(gs_clf.best_score_)  # 0.93000000000000005; 最佳准确率
for param_name in sorted(parameters.keys()):
    print("%s: %r" % (param_name, gs_clf.best_params_[param_name]))
# clf__alpha: 0.01
# tfidf__use_idf: True
# vect__ngram_range: (1, 2)
