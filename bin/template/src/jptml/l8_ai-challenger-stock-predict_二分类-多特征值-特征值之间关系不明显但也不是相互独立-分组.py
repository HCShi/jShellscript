#!/usr/bin/python3
# coding: utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import log_loss  # 评价标准是 logloss, 越低越好
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.decomposition import PCA
from sklearn import svm
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import np_utils
from keras.optimizers import RMSprop
# wc stock_train_data_20171103.csv  # 276677    276677 591530261 stock_train_data_20171103.csv
# head -n 1 stock_train_data_20171103.csv  # id,feature0,feature1,...,feature104,weight,label,group1,group2,era,code_id
# 27w 条数据, 但每个数据有 104 个特征
##################################################################
## 官方数据讲解
# 其中 id 列为数据唯一标识编码, feature 列为原始数据经过变换之后得到的特征, weight 列为样本重要性, label 列为待预测二分类标签
#     group1 和 group2 是两列类别特征, era 列为时间区间编号(数值越小时间越早)

# 测试数据集不包括 weight 列、 label 列和 era 列

# 选手可以在周一 00:00:00~周五 23:59:59 之间上传本期比赛结果, 期间不限制上传次数, 周六之后不再接受新的上传, 将按照选手最后一次上传结果进行评分.
# 上传的结果为一个以逗号分隔的文本文件(csv), 格式示例:
#     id      proba
#     600001  0.843231
#     600002  0.323443
# 其中 id 和测试数据集的 id 一列完全对应, proba 为预测为正类即标签为 1 的概率, 概率值必须为 0~1 之间的某个浮点数
# 虚拟股票趋势预测比赛的评价指标类比一般二分类问题的评价方式, 将最终的 logloss 值作为最终选手排名的依据
# 14thcoder 注: 都说是二分类问题了, 还让输出 proba, 脑子有毛病吧...

# 不同于其他的机器学习竞赛数据集, 本竞赛数据集有其特殊性, 在于: **独立同分布假设不成立**
# 虚拟股票竞赛中, 训练集和测试集的数据分布并不完全一样. 通过大量提交得到的公开排名最佳模型, 很有可能是过拟合的结果, 在最终排名上表现不佳.
#     所以选手要着重注意模型的泛化能力.

# 未来数据问题
# 在每一个时点上我们只能利用之前的信息进行预测, 因此我们在数据集中提供了 era 一列表示样本产生的时间, 数值越小, 样本所在的时间越早.
# 选手们需要注意的是:
# - 测试数据集在任何情况下都不能引入到训练集(包括但不限于非监督学习、数据归一化), 否则可能出现严重的过拟合问题, 导致公开排名和最终排名出现较大差异.
# - 对于交叉验证, 建议按照训练数据 era 列随机抽取一个或若干个 era 进行交叉验证, 而不是在全部训练样本上进行随机采样进行交叉验证, 这也是我们加入了 era 列的主要目的.
# - 数据的分布也是随时间而变化, 也就是说, 有可能在某个较长的时间周期下, 某些特征保持不变, 因此建议选手对数据集的特征进行更深入的分析.
# 同组数据具有更高相似性
# group1 和 group2 是两列类别特征. group1 是粗划分类别, group2 是细划分类别, 相同类别内的股票具有更高程度的相似性, 选手可根据自己的需求选择使用.
##################################################################
## 一: 数据预览
df = pd.read_csv('./tmp_dataset/ai-challenger-stock-predict/stock_train_data_20171117.csv')  # 还是很快的, 是因为 index 很少(27w), 但是 column 很多(110) 吗?
# df = pd.read_csv('./tmp_dataset/ai-challenger-stock-predict/stock_train_data_20171103.csv')  # 最开始实在 1103 的数据集上测试的, 后来换了新的数据集, 但有的注释还是 1103
print(df.shape)  # (276676, 112)
print(len(df.columns.values))  # 112
print(df.columns.values)
print(df.info())  # feature[0-104]
# RangeIndex: 276676 entries, 0 to 276675
# Columns: 112 entries, id to code_id
# dtypes: float64(107), int64(5)
# memory usage: 236.4 MB  # 占用内存居然比数据集还小
print(df.describe())
#             feature3       feature4       feature5       feature6  \
# count  276676.000000  276676.000000  276676.000000  276676.000000
# mean       -0.037787       0.002161       0.071094      -0.021346
# std         0.901826       1.006217       0.850766       1.421488
# min        -6.111678      -8.124839      -9.787757    -133.782342
# 25%        -0.503561      -0.764229      -0.293654      -0.202372
# 50%        -0.039513      -0.002357       0.351884      -0.064247
# 75%         0.470702       0.781499       0.734522       0.136148
# max         8.933716       5.187413       0.734522       1.185067
# feather1-104, 各属性基本都是 [-10, 10], 但也有特殊的情况, 进行 StandardScale 归一化
print(set(df.label))  # {0.0, 1.0}; 二分类问题
print(set(df.group1))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}
print(set(df.group2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104}
# 粗粒度是 28 类, 细粒度是 104 类
print(set(df.era))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134}
print(len(set(df.weight)), df.weight.max(), df.weight.min())  # 275522 62.9964416896 0.00087637042423; {0.12106464611179035, 0.78125, 1.953125,...}; 每个 index 都不太一样
print(len(set(df.code_id)))  # 2463; {0, 1, 2, ..., 2737, 2738}, 还不是连续的...
print(min(set(df.describe().std())))  # 97381.9317633
print(max(set(df.describe().std())))  # 99715.1500473; 看来不能按方差来弄了
# 查看权重
print(df.weight)
print(df.weight.min(), df.weight.max(), df.weight.mean(), df.weight.std())  # 0.00087637042423 62.9964416896 4.0096613560878716 3.6548084714775215
from collections import Counter
print(Counter(df.weight.apply(lambda x: str(x)[:4])).most_common(10))  # [('0.24', 585), ('1.19', 582), ('0.99', 578), ('0.23', 573), ('0.49', 570), ('0.42', 560), ('0.86', 556), ('0.33', 555), ('0.80', 546), ('0.32', 545)]

# weight / 0.2 + 1; 本来想用这个公式来将每条记录重复这么多遍, 后来发现 fit() 有 sample_weight 参数
weight = df.weight; print(type(weight))  # <class 'pandas.core.series.Series'>
print(len(weight))  # 276676
tmp = weight.astype(int) / 0.2 + 1
print(tmp[:5].astype(int))
##################################################################
## 开始用 Matplotlib
## plot 查看各属性之间和 label 的关系; 放弃了, 属性太多了, 名字还一样 feature1-104, 没重点, 还是先用 logistic 跑一遍, 将相关系数小的筛掉
##################################################################
## 二: 数据预处理
##################################################################
## 二(1): 一开始的思路是用 Logistic 算出每个 feature 的权重, 将权重小的 pass; 后来太慢了, 放弃, 换 NB, 但无法计算权重
train_df = df.filter(regex='label|feature*'); print(train_df.shape)  # (276676, 106);
print(train_df.columns.values)  # ['feature1', ..., 'feature104', 'label']
X = train_df.ix[:, :-1]; print(X.shape)  # (276676, 105)
y = train_df.ix[:, -1]; print(set(y))  # {0.0, 1.0}
## StandardScale 归一化
scaler = preprocessing.StandardScaler()
X_scaled = scaler.fit_transform(X.as_matrix()); print(X_scaled.shape)  # (276676, 105)
print(X_scaled.min(), X_scaled.max())  # -117.620586788 145.687104865
print(X_scaled.std())  # 1.0; 对最大最小值不满意, 换一种吧
## MinMaxScaler 归一化
min_max_scaler = preprocessing.MinMaxScaler()
X_scaled = min_max_scaler.fit_transform(X.as_matrix()); print(X_scaled.shape)  # (276676, 105)
print(X_scaled.min(), X_scaled.max())  # 0.0 1.0; 这个效果好, 选这个
## 先用 Logistic 跑一遍, 找到属性权重小的删掉
clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
clf.fit(X_scaled, y)  # 好慢啊!!!, 等会一定要保存下来, 这里只是想看一下各个属性的权重和 label 之间的关系, 所以不用交叉验证
# 然后就花了 2h 来跑这个, 发现好像只用了 feather*, 忘加 group* 属性了, 没多大关系
# 最后 KeyboardInterrupt, 真的跟我没关系...
## 上边用 Logistic 太慢了, 这里重新用 NB 跑一遍
clf = MultinomialNB()
clf.fit(X_scaled, y)  # 这个贼快, 但是用不了
print(clf.coef_.T)  # 竟然都是负数
# print(clf.feature_importances_)  # NB 没有 feature_importances_
# NB 的系数并不能当成权重
print(np.dot(X_scaled[1, :], clf.coef_.T))  # [-146.2764231]
print(len(clf.predict(X)))  # 276676
print(clf.predict(X))
## 将 clf 进行保存 并 读取
with open('./tmp_dataset/ai-challenger-stock-predict/data-preprocessing-clf.pickle', 'wb') as f: pickle.dump(clf, f)
with open('./tmp_dataset/ai-challenger-stock-predict/data-preprocessing-clf.pickle', 'rb') as f: clf2 = pickle.load(f)
print(clf2.predict(X[0:1]))  # [0]
##################################################################
## 二(2): 在 train 上 train_test_split, 看 NB 会有什么结果
## MinMaxScaler 放到 [0, 1] 中, 同时 NB 不让是 负数
train_df = df.filter(regex='label|feature*'); print(train_df.shape)  # (276676, 106);
min_max_scaler = preprocessing.MinMaxScaler()

train_df_scaled = min_max_scaler.fit_transform(train_df); print(train_df_scaled.shape)  # (276676, 106)
print(set(train_df_scaled[:, -1]))  # {0.0, 1.0}
# 上面两句, 相当于下面的几句, 最后一列 label 不会变化
X = train_df.ix[:, :-1]; print(X.shape)  # (276676, 105)
y = train_df.ix[:, -1]; print(set(y), y.shape)  # {0.0, 1.0} (276676,)
X_scaled = min_max_scaler.fit_transform(X); print(X_scaled.shape)  # (276676, 105)
train_df_scaled = np.hstack((X_scaled, y.values.reshape(-1, 1))); print(train_df_scaled.shape)  # (276676, 106)
print(set(train_df_scaled[:, -1]))  # {0.0, 1.0}

split_train, split_cv = train_test_split(train_df_scaled, test_size=0.3, random_state=0)  # 分割数据, 按照 训练数据:cv 数据 = 7:3 的比例
print(split_cv.shape, split_train.shape)  # (83003, 106) (193673, 106)
## MultinomialNB().fit()
clf = MultinomialNB()
clf.fit(split_train[:, :-1], split_train[:, -1])

## predict
predicted = clf.predict(split_cv[:, :-1])
print(np.mean(predicted == split_cv[:, -1]))  # 0.536583015072; 大于 0.5, 优化一下还可以吧
print(log_loss(split_cv[:, -1], predicted))  # 16.0062177861; 排行榜上最高的是 0.68, 差距有点大
##################################################################
## 二(3): 尝试用 group 分组的信息进行筛选
##################################################################
## 二(4): 使用特征选择方法, 还没弄完..., 换 PCA 吧
# 方差
train_df = df.filter(regex='label|feature*'); print(train_df.shape)  # (276676, 106);
min_max_scaler = preprocessing.MinMaxScaler()
train_df_scaled = min_max_scaler.fit_transform(train_df); print(train_df_scaled.shape)  # (276676, 106)
print(len(train_df_scaled.std(axis=0)))  # 106
print(set(train_df_scaled.std(axis=0)))  # {0.13128078563447088, 0.074404706698505629, ...}
# SelectKBest
X_new = SelectKBest(chi2, k=50).fit_transform(split_train[:, :-1], split_train[:, -1]); print(X_new.shape)  # (150, 2)
##################################################################
## 二(5): 准备下面的 Keras 全连接层神经网络
## 将 label, weight, group, feature 全部筛选出来
train_df = df.filter(regex='label|weight|group*|feature*|code_id'); print(train_df.shape)  # (276676, 109);
print(train_df.columns.values)  # [..., 'feature103' 'feature104' 'weight' 'label' 'group1' 'group2']; 要换顺序
columns = list(train_df.columns.values); print(columns[:2])  # ['feature0', 'feature1']
columns = columns[:-5] + columns[-3:] + ['weight', 'label']
train_df = train_df[columns]
print(train_df.columns.values)  # [..., 'feature103' 'feature104' 'group1' 'group2' 'weight' 'label'];
print(set(train_df.label.values))  # {0.0, 1.0}
train_df.label = train_df.label.apply(int); print(set(train_df.label.values))  # {0, 1}; 在这里弄好以后下面有回去了...
## 按照 group 分组训练, 先筛选出了第一组, 和上面几行是并列的, 如果用了上面的那些特征, 就不用再按照 group 单独划分了
# train_df = df.loc[df['group1'] == 1].filter(regex='label|feature*'); print(train_df.shape)  # (10630, 106)

## 上面筛选数据, 下面进行归一化
min_max_scaler = preprocessing.MinMaxScaler()
train_df_scaled = min_max_scaler.fit_transform(train_df); print(train_df_scaled.shape)  # (276676, 108)
print(set(train_df_scaled[:, -1]))  # {0.0, 1.0}
## std_scaler 还没调好, 还是用上面的 min-max 吧
# std_scaler = preprocessing.StandardScaler()
# train_df_scaled = std_scaler.fit_transform(train_df); print(train_df_scaled.shape)  # (276676, 108)
# print(train_df_scaled.min(), train_df_scaled.max())  # -117.620586788 145.687104865
# print(train_df_scaled.std())  # 1.0;
# print(train_df_scaled.shape)  # (276676, 108)

## 切分数据
split_train, split_cv = train_test_split(train_df_scaled, test_size=0.3, random_state=0)  # 分割数据, 按照 训练数据:cv 数据 = 7:3 的比例
print(split_train.shape, split_cv.shape)  # (193673, 109) (83003, 109)
X_train, y_train = split_train[:, :-2], split_train[:, -1].astype(int); print(X_train.shape, y_train.shape, set(y_train))  # (193673, 107) (193673,) {0, 1}
X_test, y_test = split_cv[:, :-2], split_cv[:, -1].astype(int); print(X_test.shape, y_test.shape, set(y_test))  # (83003, 107) (83003,) {0, 1}
## 切分只有 label, 没有 weight 的数据
# X_train, y_train = split_train[:, :-1], split_train[:, -1].astype(int); print(X_train.shape, y_train.shape, set(y_train))  # (193673, 107) (193673,) {0, 1}
# X_test, y_test = split_cv[:, :-1], split_cv[:, -1].astype(int); print(X_test.shape, y_test.shape, set(y_test))  # (83003, 107) (83003,) {0, 1}

# ## PCA 把 test 和 train 一起处理
# ## test
# df_test = pd.read_csv('./tmp_dataset/ai-challenger-stock-predict/stock_test_data_20171117.csv')
# print(df_test.columns.values)  # ['id' 'feature0' 'feature1' ... 'feature104' 'group1' 'group2' 'code_id']
# test_df = df_test.filter(regex='feature*|group*'); print(test_df.shape)  # (203129, 107)
# print(test_df.columns.values)
# test_df_scaled = min_max_scaler.fit_transform(test_df.as_matrix());
# ## 开始 PCA
# print(X_train.shape)  # (220805, 100)
# print(X_test.shape)  # (94632, 100)
# print(test_df_scaled.shape)  # (238858, 100)
# print(train_df.ix[0])
# dataset = np.vstack((X_train, X_test, test_df_scaled)); print(dataset.shape)  # (554295, 100)
# dataset_pca = PCA(n_components=20).fit_transform(dataset); print(dataset_pca.shape)  # (554295, 50)
# X_train_pca = dataset_pca[:220805]; print(X_train_pca.shape)  # (220805, 50)
# X_test_pca = dataset_pca[220805:315437]; print(X_test_pca.shape)  # (94632, 50)
# test_df_scaled_pca = dataset_pca[315437:]; print(test_df_scaled_pca.shape)  # (238858, 50)
# print(y_train.shape)

## 转换为 to_categorical()
y_train = np_utils.to_categorical(y_train); print(y_train[0])  # [ 0.  1.]; 上面白换成整形了
y_test = np_utils.to_categorical(y_test); print(y_test[0])  # [ 0.  1.]
##################################################################
## 二(六): 使用 二(五) 中处理好的数据测试 SVM, y_train/y_test 不要用 to_categorical() 了
clf_lin = svm.SVC(kernel='linear', decision_function_shape='ovo')
clf_poly = svm.SVC(kernel='poly', decision_function_shape='ovo')
clf_rbf = svm.SVC(kernel='rbf', decision_function_shape='ovo')
clf_lin.fit(X_train[:1000], y_train[:1000])  # 这三个都是近 20s, 还可以忍
clf_rbf.fit(X_train[:1000], y_train[:1000])
clf_poly.fit(X_train[:1000], y_train[:1000])
print(clf_lin.predict(X_test[:10]))
print(clf_rbf.predict(X_test[:10]))
print(clf_poly.predict(X_test[:10]))
print(y_test[:10])  # 效果差的可怜...
##################################################################
## 三: 建立模型 Keras
# split_train.shape: (193673, 106)
model = Sequential()  # 默认第二层输入是第一层的输出
model.add(Dense(2, input_shape=(101,)))
# model.add(Dense(2, input_shape=(784,)))  # 训练 mnist(处理为二分类) 达到了 0.98..., 这里的数据一直是 < 0.56
model.add(Activation('sigmoid'))
# model.compile(loss='mse', optimizer='sgd', metrics=['accuracy'])  # mean square, 优化器
rmsprop = RMSprop(lr=0.0001, rho=0.9, epsilon=1e-08, decay=0.0)  # 学习率, ...
model.compile(optimizer=rmsprop, loss='categorical_crossentropy', metrics=['accuracy'])  # 最终采用这个
##################################################################
## 四: 交叉验证
print(split_train[:, -2].shape)  # (193673,)
# model.fit(X_train, y_train, batch_size=10000, sample_weight=split_train[:, -2], epochs=1000, verbose=1, validation_data=(X_test, y_test))
# model.fit(X_train, y_train, batch_size=32, epochs=10, verbose=1, validation_data=(X_test, y_test))
model.fit(X_train, y_train, batch_size=32, epochs=10, verbose=1, validation_data=(X_test, y_test))
print(model.evaluate(X_test, y_test))  # [0.68263210975401256, 0.56024481042279395]
# 计算 log_loss
predicted = model.predict(split_cv[:, :-2])
print(np.mean(predicted == split_cv[:, -1]))  # 0.536583015072; 大于 0.5, 优化一下还可以吧
print(log_loss(split_cv[:, -1], predicted))  # 0.689217666075; 排行榜上最高的是 0.68, 差距有点大
##################################################################
## 五: 测试集处理
df_test = pd.read_csv('./tmp_dataset/ai-challenger-stock-predict/stock_test_data_20171117.csv')
print(df_test.columns.values)  # ['id' 'feature0' 'feature1' ... 'feature104' 'group1' 'group2' 'code_id']
test_df = df_test.filter(regex='feature*|group*|code_id'); print(test_df.shape)  # (203129, 107)
print(test_df.columns.values)
test_df_scaled = min_max_scaler.fit_transform(test_df.as_matrix()); print(test_df_scaled.shape)  # (203129, 107)
# 上面执行一次就行了
predicted = model.predict(test_df_scaled); print(predicted.shape)  # (203129, 2)
predicted_proba = model.predict_proba(test_df_scaled); print(predicted_proba.shape)  # (203129, 2)
print(predicted_proba[0, :])  # [ 0.49355215  0.50644785]; 前者是 0 的概率, 后者是 1 的概率
result = pd.DataFrame({'id': df_test.id, 'proba': predicted_proba[:, 1]})
print(result.head())
result.to_csv('./tmp_dataset/ai-challenger-stock-predict/result.csv', index=False, float_format = '%.6f')  # 还带着 header 和 index
