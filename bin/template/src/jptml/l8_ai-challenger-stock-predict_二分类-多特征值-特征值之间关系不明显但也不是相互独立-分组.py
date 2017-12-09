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
df = pd.read_csv('./tmp_dataset/ai-challenger-stock-predict/stock_train_data_20171125.csv')  # 第 13 期的赛题数据,
# df = pd.read_csv('./tmp_dataset/ai-challenger-stock-predict/stock_train_data_20171103.csv')  # 最开始实在 1103 的数据集上测试的, 后来换了新的数据集
# df = pd.read_csv('./tmp_dataset/ai-challenger-stock-predict/stock_train_data_20171117.csv')
print(df.shape)  # (316580, 105)
print(len(df.columns.values))  # 105
print(df.columns.values)
print(df.info())  # feature[0-97]
# RangeIndex: 316580 entries, 0 to 316579
# Columns: 105 entries, id to code_id
# dtypes: float64(100), int64(5)
# memory usage: 253.6 MB
print(df.describe())
#                   id       feature0       feature1       feature2  \
# count  316580.000000  316580.000000  316580.000000  316580.000000
# mean   158289.500000       0.042390      -0.023377       0.068664
# std     91388.918447       1.055376       0.985310       1.192804
# min         0.000000     -22.032300      -1.818353      -3.125299
# 25%     79144.750000      -0.454819      -0.679953      -0.332664
# 50%    158289.500000      -0.072936      -0.196487      -0.135759
# 75%    237434.250000       0.488984       0.427742       0.314470
# max    316579.000000       8.836585      33.377829     158.901426
# feather1-104, 各属性基本都是 [-10, 10], 但也有特殊的情况, 进行 StandardScale 归一化
print(set(df.label))  # {0.0, 1.0}; 二分类问题
print(set(df.group1))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28}
print(set(df.group2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104}
# 粗粒度是 28 类, 细粒度是 104 类
print(set(df.era))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118}
print(len(set(df.weight)), df.weight.max(), df.weight.min())  # 313193 20.9381551363 0.00211317497867; {0.12106464611179035, 0.78125, 1.953125,...}; 每个 index 都不太一样
print(len(set(df.code_id)))  # 3164; {0, 1, 2, ..., 2737, 2738}, 还不是连续的...
print(min(set(df.describe().std())))  # 111394.981847
print(max(set(df.describe().std())))  # 114096.744713; 看来不能按方差来弄了
# 查看权重
print(df.weight)
print(df.weight.min(), df.weight.max(), df.weight.mean(), df.weight.std())  # 0.00211317497867 20.9381551363 1.5359548913515246 1.5866062313670015
from collections import Counter
print(Counter(df.weight.apply(lambda x: str(x)[:4])).most_common(10))  # [('0.14', 1920), ('0.24', 1911), ('0.11', 1907), ('0.12', 1895), ('0.13', 1884), ('0.10', 1866), ('0.27', 1841), ('0.25', 1835), ('0.19', 1822), ('0.20', 1821)]

# weight / 0.2 + 1; 本来想用这个公式来将每条记录重复这么多遍, 后来发现 fit() 有 sample_weight 参数
weight = df.weight; print(type(weight))  # <class 'pandas.core.series.Series'>
print(len(weight))  # 316580
tmp = weight.astype(int) / 0.2 + 1
print(tmp[:5].astype(int))
##################################################################
## 开始用 Matplotlib
## plot 查看各属性之间和 label 的关系; 放弃了, 属性太多了, 名字还一样 feature1-104, 没重点, 还是先用 logistic 跑一遍, 将相关系数小的筛掉
##################################################################
## 二: 数据预处理, 下面 二(1), 二(2), 二(3), 二(4), 二(5)... 之间没有关系, 可以独立运行
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
print(df.columns.values)
## 将 label, weight, group, feature... 全部筛选出来, 也就是把 id 去掉
# train_df = df.filter(regex='label|weight|group*|feature*|code_id|era'); print(train_df.shape)  # (316580, 104); 好像只是去掉了 id...
train_df = df.drop(['id'], axis=1); print(train_df.shape)  # (316580, 104)
print(train_df.columns.values)  # ['feature0' ... 'feature97' 'weight' 'label' 'group1' 'group2', 'era', 'code_id']; 要换顺序
## 按 era 排序, 并按最小值截取
print(set(df.era))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118}
print(train_df.sort_values('era').head())
print(train_df.groupby('era').count().feature0.tolist())  # [2542, 2555, 2595, 2555, 2596, 2592, 2614, 2613, 2603, 2637, 2639, 2664, 2656, 2593, 2594, 2623, 2592, 2648, 2594, 2573, 2627, 2587, 2635, 2578, 2608, 2646, 2563, 2633, 2602, 2589, 2649, 2669, 2615, 2606, 2665, 2626, 2636, 2635, 2628, 2649, 2688, 2627, 2620, 2572, 2590, 2654, 2625, 2630, 2603, 2658, 2647, 2654, 2662, 2631, 2611, 2671, 2600, 2613, 2639, 2628, 2593, 2598, 2596, 2650, 2686, 2676, 2699, 2691, 2642, 2632, 2707, 2646, 2647, 2634, 2699, 2727, 2695, 2688, 2607, 2690, 2696, 2703, 2639, 2661, 2733, 2652, 2624, 2718, 2756, 2679, 2733, 2676, 2714, 2666, 2671, 2749, 2696, 2767, 2672, 2737, 2662, 2707, 2737, 2732, 2743, 2741, 2733, 2756, 2789, 2781, 2752, 2739, 2824, 2785, 2793, 2712, 2736, 2794, 2772]
print(min(train_df.groupby('era').count().feature0.tolist()))  # 2542; 按最小值截取
train_df = train_df.groupby('era').apply(lambda x: x[:2500]).reset_index(drop=True); print(train_df.shape)  # (297500, 104)
print(set(df.era))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118}
print(train_df.groupby('era').count().feature0.tolist())  # [2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
## 将 weight, era, label 这些测试集中没有的属性放到最后
columns = list(train_df.columns.values); print(columns[:2])  # ['feature0', 'feature1']
columns = columns[:-6] + columns[-4:-2] + [columns[-1]] + ['weight', 'era', 'label']
train_df = train_df[columns]; print(train_df.shape)  # (297500, 104)
print(train_df.columns.values)  # [..., 'feature97' 'group1' 'group2' 'code_id' 'weight' 'label'];
print(set(train_df.label.values))  # {0.0, 1.0}
train_df.label = train_df.label.apply(int); print(set(train_df.label.values))  # {0, 1}; 在这里弄好以后下面又回去了...
## 按照 group 分组训练, 先筛选出了第一组, 和上面几行是并列的, 如果用了上面的那些特征, 就不用再按照 group 单独划分了
# train_df = df.loc[df['group1'] == 1].filter(regex='label|feature*'); print(train_df.shape)  # (10630, 106)

## 上面筛选数据, 下面进行归一化
min_max_scaler = preprocessing.MinMaxScaler()
train_df_scaled = min_max_scaler.fit_transform(train_df); print(train_df_scaled.shape)  # (297500, 104)
print(set(train_df_scaled[:, -1]))  # {0.0, 1.0}
print(train_df_scaled[:, -1][:3])  # [ 0.  1.  0.]

## 切分数据
# split_train, split_cv = train_test_split(train_df_scaled, test_size=0.3, random_state=0)  # 分割数据, 按照 训练数据:cv 数据 = 7:3 的比例
# print(split_train.shape, split_cv.shape)  # (193673, 109) (83003, 109)
# X_train, y_train = split_train[:, :-2], split_train[:, -1].astype(int); print(X_train.shape, y_train.shape, set(y_train))  # (193673, 107) (193673,) {0, 1}
# X_test, y_test = split_cv[:, :-2], split_cv[:, -1].astype(int); print(X_test.shape, y_test.shape, set(y_test))  # (83003, 107) (83003,) {0, 1}
# 上面个是 train_text_split() 随机切分, 现在要按照 era 切分
X_train, y_train = train_df_scaled[:-25000][:, :-3], train_df_scaled[:-25000][:, -1]; print(X_train.shape, y_train.shape)  # (272500, 101) (272500,)
print(y_train[:3])  # [ 0.  1.  0.]
X_test, y_test = train_df_scaled[-25000:][:, :-3], train_df_scaled[-25000:][:, -1]; print(X_test.shape, y_text.shape)  # (25000, 101) (25000,)
print(y_test[:3])  # [ 0.  1.  1.]

## PCA 把 test 和 train 一起处理; 结果并不好, 放弃了...
## test
df_test = pd.read_csv('./tmp_dataset/ai-challenger-stock-predict/stock_test_data_20171117.csv')
print(df_test.columns.values)  # ['id' 'feature0' 'feature1' ... 'feature104' 'group1' 'group2' 'code_id']
test_df = df_test.filter(regex='feature*|group*|code_id'); print(test_df.shape)  # (222057, 101)
print(test_df.columns.values)
test_df_scaled = min_max_scaler.fit_transform(test_df.as_matrix());
## 开始 PCA
print(X_train.shape)  # (272500, 101)
print(X_test.shape)  # (25000, 101)
print(test_df_scaled.shape)  # (222057, 101)
dataset = np.vstack((X_train, X_test, test_df_scaled)); print(dataset.shape)  # (519557, 101)
dataset_pca = PCA(70).fit_transform(dataset)
print(dataset_pca.shape)  # (519557, 70)
X_train = dataset_pca[:272500]; print(X_train.shape)  # (272500, 70)
X_test = dataset_pca[272500:297500]; print(X_test.shape)  # (25000, 70)
test_df_scaled = dataset_pca[297500:]; print(test_df_scaled.shape)  # (222057, 70)

## 转换为 to_categorical()
y_train = np_utils.to_categorical(y_train); print(y_train[0])  # [ 1. 0.]; 上面白换成整形了
y_test = np_utils.to_categorical(y_test); print(y_test[0])  # [ 1. 0.]
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
model.add(Dense(2, input_shape=(70,)))
# model.add(Dense(2, input_shape=(784,)))  # 训练 mnist(处理为二分类) 达到了 0.98..., 这里的数据一直是 < 0.56
model.add(Activation('sigmoid'))
# model.compile(loss='mse', optimizer='sgd', metrics=['accuracy'])  # mean square, 优化器
rmsprop = RMSprop(lr=0.0001, rho=0.9, epsilon=1e-08, decay=0.0)  # 学习率, ...
model.compile(optimizer=rmsprop, loss='categorical_crossentropy', metrics=['accuracy'])  # 最终采用这个
##################################################################
## 四: 交叉验证
# print(split_train[:, -2].shape)  # (193673,)
# model.fit(X_train, y_train, batch_size=10000, sample_weight=split_train[:, -2], epochs=1000, verbose=1, validation_data=(X_test, y_test))
# model.fit(X_train, y_train, batch_size=32, epochs=10, verbose=1, validation_data=(X_test, y_test))
model.fit(X_train, y_train, batch_size=32, epochs=10, verbose=1, validation_data=(X_test, y_test))
print(model.evaluate(X_test, y_test))  # [0.68947558536529541, 0.54012000000000004]
# 计算 log_loss
predicted = model.predict(X_test); print(predicted[0])  # [ 0.54894304  0.64039779]
predicted_class = model.predict_classes(X_test); print(set(predicted_class), predicted_class[:3])  # {0, 1} [1 1 1]
true_class = train_df[-25000:].label.astype(int).tolist()
print(np.mean(predicted_class == true_class))  # 0.54012; 大于 0.5, 优化一下还可以吧
print(log_loss(y_test, predicted))  # 0.689217666075; 排行榜上最高的是 0.68, 差距有点大
print(y_test[:2], '\n', predicted[:2])
print(log_loss(true_class, predicted_class))  # 15.8839922416; log_loss 公式中使计算概率的..., 所以不能这样算
print(true_class[:5], '\n', predicted_class[:5])
##################################################################
## 五: 测试集处理
df_test = pd.read_csv('./tmp_dataset/ai-challenger-stock-predict/stock_test_data_20171125.csv')
print(df_test.columns.values)  # ['id' 'feature0' 'feature1' ... 'feature97' 'group1' 'group2' 'code_id']
test_df = df_test.filter(regex='feature*|group*|code_id'); print(test_df.shape)  # (222057, 101)
print(test_df.columns.values)
test_df_scaled = min_max_scaler.fit_transform(test_df.as_matrix()); print(test_df_scaled.shape)  # (222057, 101)
# 上面执行一次就行了
predicted = model.predict(test_df_scaled); print(predicted.shape)  # (222057, 2)
predicted_proba = model.predict_proba(test_df_scaled); print(predicted_proba.shape)  # (222057, 2)
print(predicted_proba[0, :])  # [ 0.51132804  0.73067743]; 前者是 0 的概率, 后者是 1 的概率
result = pd.DataFrame({'id': df_test.id, 'proba': predicted_proba[:, 1]})
print(result.head())
result.to_csv('./tmp_dataset/ai-challenger-stock-predict/result.csv', index=False, float_format = '%.6f')  # 还带着 header 和 index
