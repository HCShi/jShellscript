#!/usr/bin/python3
# coding: utf-8
# 参考: [](http://adataanalyst.com/scikit-learn/countvectorizer-sklearn-example/)
# cd tmp_dataset && wget https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip  # 下载数据
import pandas
##################################################################
## 先观察数据
messages = [line.rstrip() for line in open('./tmp_dataset/smsspamcollection/SMSSpamCollection')]; print(len(messages))  # 5574
for num, message in enumerate(messages[:10]): print(num, message, '\n')  # 发现前面 label 和 后面正文是 \t 分割
##################################################################
## 导入数据
messages = pandas.read_csv('./tmp_dataset/smsspamcollection/SMSSpamCollection', sep='\t', names=['labels', 'message'])
print(messages.head())
print(messages.describe())  # count  5572.000000; 5572 个短信文档
print(messages.info())  # <class 'pandas.core.frame.DataFrame'>
print(messages.groupby('labels').describe())
messages['length'] = messages['message'].apply(len); print(messages.head())  # 添加长度属性
##################################################################
## 画图观察
import matplotlib.pyplot as plt
messages['length'].plot(bins=50, kind='hist'); plt.show()  # 50 个柱子
print(messages['length'].describe())
print(messages[messages['length'] == 910]['message'].iloc[0])  # 输出具体的 Message 内容
messages.hist(column='length', by='labels', bins=50, figsize=(10, 4)); plt.show()
##################################################################
## 对测试样例进行 去停用词
import string
mess = 'Sample message ! Notice: it has punctuation'
nopunc = ''.join([char for char in mess if char not in string.punctuation]); print(nopunc)  # 去掉标点!!!
from nltk.corpus import stopwords; print(stopwords.words('english')[0:10])  # ['i', 'me', 'my', 'myself', ...], 取出最常用的 10 个单词
clean_mess = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
print(clean_mess)  # ['Sample', 'message', 'Notice', 'punctuation']
##################################################################
## 将上面的步骤函数化
def text_process(mess):  # Takes in a string of text, then performs the following:
    # 1. Remove all punctuation; 2. Remove all stopwords; 3. Returns a list of the cleaned text
    nopunc = ''.join([char for char in mess if char not in string.punctuation])  # Check characters to see if they are in punctuation
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]  # Now just remove any stopwords
print(messages.head())
print(messages['message'].head(5).apply(text_process))
##################################################################
## 1. 开始用 词袋模型 进行向量化; 可以去 jptsklearn l13 - l20 看一下文本处理的相关实例
from sklearn.feature_extraction.text import CountVectorizer
bow_transformer = CountVectorizer(analyzer=text_process)  # bag of words; 居然可以把 text_process 传进去
bow_transformer.fit(messages['message'])
# 随机检测一个结果
message4 = messages['message'][3]; print(len(message4), message4)  # 49 U dun say so early hor... U c already then say...; 是一共 49 个字符...
bow4 = bow_transformer.transform([message4]); print(bow4)  # (0, 4068) 2; (0, 4629) 1; (0, 5261) 1; (0, 6204) 1; (0, 6222) 1; (0, 7186) 1; (0, 9554) 2
print(bow_transformer.get_feature_names()[4073])  # UIN
print(bow_transformer.get_feature_names()[4068])  # U; 词袋模型 获取特征名称, 必须通过 CountVectorizer 对象的 get_feature_names()
print(bow_transformer.get_feature_names()[9554])  # say
# 将所有的 message 进行向量化
messages_bow = bow_transformer.transform(messages['message'])
print ('Shape of Sparse Matrix: ', messages_bow.shape)  # Shape of Sparse Matrix:  (5572, 11425); 5572 个短信文档, 11425 个无重复单词
print ('Amount of Non-Zero occurences: ', messages_bow.nnz)  # Amount of Non-Zero occurences:  50548; 稀疏矩阵非 0 部分个数
print ('sparsity: %.2f%%' % (100.0 * messages_bow.nnz / (messages_bow.shape[0] * messages_bow.shape[1])))  # sparsity: 0.08%
##################################################################
## 2. 提取特征值
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer().fit(messages_bow)  # 和上面 bow_transformer 的过程类似了, fit() 以后返回的还是一个 TfidfTransformer 对象
# 测试上面测试的 message4
tfidf4 = tfidf_transformer.transform(bow4)
print(tfidf4)  # (0, 9554) 0.53; (0, 7186) 0.43; (0, 6222) 0.31; (0, 6204) 0.29; (0, 5261) 0.29; (0, 4629) 0.26; (0, 4068) 0.40
print (tfidf_transformer.idf_[bow_transformer.vocabulary_['u']])  # 3.28005242674
print (tfidf_transformer.idf_[bow_transformer.vocabulary_['university']])  # 8.5270764989
# 将所有的 message 提取特征值
messages_tfidf = tfidf_transformer.transform(messages_bow)
print(messages_tfidf.shape)  # (5572, 11425)
##################################################################
## 3. 开始用特征值分类
from sklearn.naive_bayes import MultinomialNB
spam_detect_model = MultinomialNB().fit(messages_tfidf, messages['labels'])
# 测试上面测试的 message4
print('Predicted: ', spam_detect_model.predict(tfidf4)[0] )  # Predicted:  ham
print('Expected: ', messages['labels'][3])  # Expected:  ham
# 测试所有的 message
all_predictions = spam_detect_model.predict(messages_tfidf)
print(all_predictions)  # ['ham' 'ham' 'spam' ..., 'ham' 'ham' 'ham']
##################################################################
## 4. 验证结果
from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(messages['labels'], all_predictions))
#              precision    recall  f1-score   support
#         ham       0.98      1.00      0.99      4825
#        spam       1.00      0.85      0.92       747
# avg / total       0.98      0.98      0.98      5572
print(confusion_matrix(messages['labels'], all_predictions))  # [[4825    0] [ 115  632]]; 因为就两项, 所以有点少
##################################################################
## 5. 网格搜索进行优化..., 这里没有实现
##################################################################
##################################################################
## 6. 上面是在 train 上直接测试, 这里实现 交叉测试 + Pipeline, 一个完整的分类流程
from sklearn.model_selection import train_test_split
msg_train, msg_test, label_train, label_test = train_test_split(messages['message'], messages['labels'], test_size=0.2)
print(len(msg_train), len(msg_test), len(msg_train) + len(msg_test))  # 4457 1115 5572
from sklearn.pipeline import Pipeline
pipeline = Pipeline([('bow', CountVectorizer(analyzer=text_process)),  # 可以直接用 stopwords=stopwords, 效果相同
                     ('tfidf', TfidfTransformer()),
                     ('classifier', MultinomialNB())])
pipeline.fit(msg_train, label_train)
predictions = pipeline.predict(msg_test)
print(classification_report(predictions, label_test))
#              precision    recall  f1-score   support
#         ham       1.00      0.96      0.98       999
#        spam       0.73      1.00      0.84       116
# avg / total       0.97      0.96      0.96      1115
##################################################################
## 总结:
# 1. 命名非常规范, 比官网的都好, 很优秀
# 2. 可以把最后一部分的代码直接拿去处理其他的题目
# 3. 没有类别个数限制, 完全可以适用于多类的文本分类, 不是 0-1 分类
# 4. 停用词在 词袋模型 里面传进去, 这里自己实现了 analyzer, 也可以用 stopwords=stopwords 来实现
