#!/usr/bin/python3
# coding: utf-8
# 比赛网址: [Kaggle](https://www.kaggle.com/c/facebook-recruiting-iv-human-or-bot/data)
# 参考: [](https://segmentfault.com/a/1190000009101175)
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from sklearn.metrics import roc_auc_score
from collections import defaultdict
import numpy as np
import pandas as pd
##################################################################
## 官方数据讲解:
# 根据竞标行为判断是否是机器人
# There are two datasets in this competition. One is a bidder dataset that includes a list of bidder information, including their id,
#     payment account, and address. The other is a bid dataset that includes 7.6 million bids on different auctions.
#     The bids in this dataset are all made by mobile devices.
# The online auction platform has a fixed increment of dollar amount for each bid, so it does not include an amount for each bid.
#     You are welcome to learn the bidding behavior from the time of the bids, the auction, or the device.

# File descriptions:
# train.csv - the training set from the bidder dataset
# test.csv - the test set from the bidder dataset
# bids.csv - the bid dataset

# Data fields:
# For the bidder dataset
# bidder_id – Unique identifier of a bidder.
# payment_account – Payment account associated with a bidder. These are obfuscated to protect privacy.
# address – Mailing address of a bidder. These are obfuscated to protect privacy.
# outcome – Label of a bidder indicating whether or not it is a robot. Value 1.0 indicates a robot, where value 0.0 indicates human.
# The outcome was half hand labeled, half stats-based. There are two types of "bots" with different levels of proof:
#     1. Bidders who are identified as bots/fraudulent with clear proof. Their accounts were banned by the auction site.
#     2. Bidder who may have just started their business/clicks or their stats exceed from system wide average.
#        There are no clear proof that they are bots.
#
# For the bid dataset:
# bid_id - unique id for this bid
# bidder_id – Unique identifier of a bidder (same as the bidder_id used in train.csv and test.csv)
# auction – Unique identifier of an auction
# merchandise –  The category of the auction site campaign, which means the bidder might come to this site by way of searching
#     for "home goods" but ended up bidding for "sporting goods" - and that leads to this field being "home goods". This categorical field
#     could be a search term, or online advertisement.
# device – Phone model of a visitor
# time - Time that the bid is made (transformed to protect privacy).
# country - The country that the IP belongs to
# ip – IP address of a bidder (obfuscated to protect privacy).
# url - url where the bidder was referred from (obfuscated to protect privacy).
##################################################################
## 一: 数据预览
df_bids = pd.read_csv('./tmp_dataset/Kaggle-Facebook-Recruiting-IV-Human-or-Robot/bids.csv', low_memory=False); print(df_bids.shape)  # (7656334, 9); 900M 这个要读 10s+, low_memory 对内存占用并没有影响
df_train = pd.read_csv('./tmp_dataset/Kaggle-Facebook-Recruiting-IV-Human-or-Robot/train.csv'); print(df_train.shape)  # (2013, 4)
df_test = pd.read_csv('./tmp_dataset/Kaggle-Facebook-Recruiting-IV-Human-or-Robot/test.csv'); print(df_test.shape)  # (4700, 3)
print(df_bids.columns.values)  # ['bid_id' 'bidder_id' 'auction' 'merchandise' 'device' 'time' 'country' 'ip' 'url']
print(df_train.columns.values)  # ['bidder_id' 'payment_account' 'address' 'outcome']
print(df_test.columns.values)  # ['bidder_id' 'payment_account' 'address']
print(df_bids.info())
# bid_id         int64
# bidder_id      object
# auction        object
# merchandise    object
# device         object
# time           int64
# country        object
# ip             object
# url            object
# dtypes: int64(2), object(7)
# memory usage: 525.7+ MB
print(df_bids.describe())
#              bid_id          time
# count  7.656334e+06  7.656334e+06
# mean   3.828166e+06  9.697978e+15
# std    2.210193e+06  5.250518e+13
# min    0.000000e+00  9.631917e+15
# 25%    1.914083e+06  9.641139e+15
# 50%    3.828166e+06  9.700654e+15
# 75%    5.742250e+06  9.761744e+15
# max    7.656333e+06  9.772885e+15
print(df_bids.head(1))
#    bid_id                              bidder_id auction merchandise  device   time             country             ip              url
# 0       0  8dac2b259fd1c6d1120e519fb1ac14fbqvax8   ewmzr     jewelry  phone0   9759243157894736      us  69.166.231.58  vasstdc27m7nks3
print(df_train.head(1))
#                                bidder_id payment_account                       address                                    outcome
# 0  91a3c57b13234af24875c56fb7e2b2f4rb56a a3d2de7675556553a5f08e4c88d2c228754av a3d2de7675556553a5f08e4c88d2c228vt0u4      0.0

## 异常数据检测
# 查看各表格中是否存在空值
print(df_bids.isnull().any().any())  # True
print(df_train.isnull().any().any())  # False
print(df_test.isnull().any().any())  # False
# 在竞标行为数据集中存在缺失值的情况, 下面便针对 bids 数据进一步寻找缺失值
print(pd.isnull(df_bids).any())
# bid_id         False
# bidder_id      False
# auction        False
# merchandise    False
# device         False
# time           False
# country         True
# ip             False
# url            False
missing_country = df_bids['country'].isnull().sum(); print(missing_country)  # 8859; 这些记录缺失 country
normal_country = df_bids['country'].notnull().sum(); print(normal_country)  # 7647475
# country 一栏属性中存在很少一部分用户行为是没有 country 记录的, 在预处理部分可以针对这部分缺失数据进行填充操作, 有两种思路:
# 1. 针对原始行为数据按照用户分组后, 看看每个对应的用户竞标时经常所位于的国家信息, 对缺失值填充常驻国家
# 2. 针对原始行为数据按照用户分组后, 按时间顺序对每组用户中的缺失

## 简单统计各项基本特征(类别特征)的数目(除去时间)
print(df_bids.shape)  # (7656334, 9)
print(len(df_bids['bidder_id'].unique()))  # 6614
print(len(df_bids['auction'].unique()))  # 15051
print(len(df_bids['merchandise'].unique()))  # 10; 商品类别
print(len(df_bids['device'].unique()))  # 7351
print(len(df_bids['country'].unique()))  # 200
print(len(df_bids['ip'].unique()))  # 2303991
print(len(df_bids['url'].unique()))  # 1786351
print(len(set(df_train.bidder_id)), len(set(df_test.bidder_id)))  # 2013 4700; 竞标行为中的用户总数少于训练集 + 测试集的用户数, 并是一一对应的
# 商品类别和国家的种类相对其他特征较少, 可以作为天然的类别特征提取出来进行处理, 而其余的特征可能更多的进行计数统计

## 接下来验证下竞标行为数据中的用户是否完全来自训练集和测试集
lst_all_users = list(set(df_train['bidder_id'])) + list(set(df_test['bidder_id'])); print(len(lst_all_users))  # 6713
lst_bidder = list(set(df_bids['bidder_id'])); print(len(lst_bidder))  # 6614
print(set(lst_bidder).issubset(set(lst_all_users)))  # True
lst_nobids = [i for i in lst_all_users if i not in lst_bidder]; print(len(lst_nobids))  # 99
lst_nobids_train = [i for i in lst_nobids if i in (df_train['bidder_id'].unique()).tolist()]; print(len(lst_nobids_train))  # 29
lst_nobids_test = [i for i in lst_nobids if i in (df_test['bidder_id'].unique()).tolist()]; print(len(lst_nobids_test))  # 70
print(df_train[(df_train['bidder_id'].isin(lst_nobids_train)) & (df_train['outcome']==1.0)])  # Empty DataFrame; 是机器人且在 train 中, 没在 bids 中
# 由上述计算可知存在 99 个竞标者无竞标记录, 其中 29 位来自训练集, 70 位来自测试集, 而且这 29 位来自训练集的竞标者未被标记为机器人用户,
# 所以可以针对测试集中的这 70 位用户后续标记为人类或者取平均值处理

# check the partition of bots in train
print(df_train[df_train['outcome'] == 1].shape[0] / df_train.shape[0] * 100)  # 5.11674118231; 训练集中的标记为机器人的用户占所有用户数目约 5%
df_train.groupby('outcome').size().plot(labels=['Human', 'Robot'], kind='pie', autopct='%.2f', figsize=(4, 4), title='Distribution of Human vs. Robots', legend=True); plt.show()
# 由上述训练集中的正负例分布可以看到本数据集正负例比例失衡, 所以后续考虑使用 AUC(不受正负例比例影响)作为评价指标, 此外尽量采用 Gradient Boosting 族模型来进行训练
##################################################################
## 二: 数据预处理
##################################################################
## 二(1): 处理缺失数据
# 针对前面数据探索部分所发现的竞标行为数据中存在的国家属性缺失问题, 考虑使用针对原始行为数据按照用户分组后,
# 按时间顺序对每组用户中的缺失值前向或后向填充相邻的国家信息的方法来进行缺失值的填充处理
print(df_bids.head())
print(pd.Index(df_bids['time']).is_monotonic)  # False; Return boolean if values in the object are monotonic_increasing, 单调递增
df_bids['country'] = df_bids.sort_values(['bidder_id', 'time']).groupby('bidder_id')['country'].ffill()  # 先用前面的填充
df_bids['country'] = df_bids.sort_values(['bidder_id', 'time']).groupby('bidder_id')['country'].bfill()  # 前面没有的按后面填充
# 居然可以这样来填充...  :-), 顺序不会乱吗...

print(df_bids.isnull().any().any())  # True; 居然还有缺失值
missing_country = df_bids['country'].isnull().sum().sum(); print(missing_country)  # 5, 上面居然没有填充完
normal_country = df_bids['country'].notnull().sum().sum(); print(normal_country)  # 7656329
nan_rows = df_bids[df_bids.isnull().T.any()]; print(nan_rows)  # 将那 5 个筛选出来
nan_bidder = nan_rows['bidder_id'].values.tolist(); print(nan_bidder)  # ['f3ab8c9ecc0d021ebc81e89f20c8267bn812w', '88ef9cfdbec4c9e33f6c2e0b512e7a01dp2p2', '29b8af2fea3881ef61911612372dac41vczqv', 'df20f216cbb0b0df5a7b2e94b16a7853iyw9g', '5e05ec450e2dd64d7996a08bbbca4f126nzzk']
print(df_bids[df_bids['bidder_id'].isin(nan_bidder)])  # 查看那 5 个用户各有几次竞标行为
# 在对整体数据的部分用户缺失国家的按照各个用户分组后在时间上前向和后向填充后, 仍然存在 5 个用户缺失了国家信息,
# 结果发现这 5 个用户是仅有一次竞标行为, 下面看看这 5 个用户还有什么特征

lst_nan_train = [i for i in nan_bidder if i in list(set(df_train['bidder_id']))]; print(len(lst_nan_train))  # 1
lst_nan_test = [i for i in nan_bidder if i in list(set(df_test['bidder_id']))]; print(len(lst_nan_test))  # 4
print(df_train[df_train['bidder_id'] == lst_nan_train[0]]['outcome'])  # 546    0.0
# 由于这 5 个用户仅有一次竞标行为, 而且其中 1 个用户来自训练集, 4 个来自测试集, 由训练集用户的标记为人类, 加上行为数太少,
# 所以考虑对这 5 个用户的竞标行为数据予以舍弃, 特别对测试集的 4 个用户后续操作类似之前对无竞标行为的用户, 预测值填充最终模型的平均预测值
bid_to_drop = nan_rows.index.values.tolist(); print(bid_to_drop)  # [1351177, 2754184, 2836631, 3125892, 5153748]
df_bids.drop(df_bids.index[bid_to_drop], inplace=True)
print(df_bids.isnull().any().any())  # False; 终于把所有的空值处理完了...
##################################################################
## 二(2): 统计基本的计数特征
# 根据前面的数据探索, 由于数据集大部分由类别数据或者离散型数据构成, 所以首先针对竞标行为数据按照竞标者分组统计其各项属性的数目,
# 比如使用设备种类, 参与竞标涉及国家, ip 种类等等
bidders = df_bids.groupby('bidder_id')  # group by bidder to do some statistics
print(bidders['device'].count())  # 每个 bidder_id 会统计使用了多少设备
def feature_count(group):
    dct_cnt = {}
    dct_cnt['devices_c'] = group['device'].unique().shape[0]
    dct_cnt['countries_c'] = group['country'].unique().shape[0]
    dct_cnt['ip_c'] = group['ip'].unique().shape[0]
    dct_cnt['url_c'] = group['url'].unique().shape[0]
    dct_cnt['auction_c'] = group['auction'].unique().shape[0]
    dct_cnt['auc_mean'] = np.mean(group['auction'].value_counts())    # bids_c/auction_c
    dct_cnt['merch_c'] = group['merchandise'].unique().shape[0]
    dct_cnt['bids_c'] = group.shape[0]
    dct_cnt = pd.Series(dct_cnt)
    return dct_cnt
cnt_bidder = bidders.apply(feature_count)
print(cnt_bidder.describe())
print(cnt_bidder[cnt_bidder['merch_c']==2])  # 商品种类数量为 2
##################################################################
## 二(3): 特征相关性, 这部分没看懂...
# 在对竞标行为数据按照用户分组后, 对数据集中的每一个产品特征构建一个散布矩阵(scatter matrix), 来看看各特征之间的相关性
# 对于数据中的每一对特征构造一个散布矩阵
pd.plotting.scatter_matrix(cnt_bidder, alpha=0.3, figsize=(16,10), diagonal='kde'); plt.show()

# 在针对竞标行为数据按照竞标用户进行分组基本统计后由上表可以看出, 此时并未考虑时间戳的情形下, 有以下基本结论:
# 1. 由各项统计的最大值与中位值, 75% 值的比较可以看到除了商品类别一项, 其他的几项多少都存在一些异常数值, 或许可以作为异常行为进行观察
# 2. 各特征的倾斜度很大, 考虑对特征进行取对数的操作, 并再次输出散布矩阵看看相关性
# 3. 商品类别计数这一特征的方差很小, 而且从中位数乃至 75% 的统计来看, 大多数用户仅对同一类别商品进行拍卖,
#    而且因为前面数据探索部分发现商品类别本身适合作为类别数据, 所以考虑分多个类别进行单独统计, 而在计数特征中舍弃该特征
cnt_bidder.drop('merch_c', axis=1, inplace=True)
cnt_bidder = np.log(cnt_bidder)
pd.plotting.scatter_matrix(cnt_bidder, alpha=0.3, figsize=(16,10), diagonal='kde'); plt.show()
# 由上面的散布矩阵可以看到, 个行为特征之间并没有表现出很强的相关性, 虽然其中的 ip 计数和竞标计数,
#     设备计数在进行对数操作处理之后表现出轻微的正相关性, 但是由于是在做了对数操作之后才体现, 而且从图中可以看到并非很强的相关性,
#     所以保留这三个特征

# 针对前述的异常行为, 先从原 train 数据集中的机器人, 人类中分别挑选几个样本进行追踪观察他们在按照 bidders 分组后的统计结果, 对比看看
# trace samples,first 2 bots, last 2 humen
indices = ['9434778d2268f1fa2a8ede48c0cd05c097zey','aabc211b4cf4d29e4ac7e7e361371622pockb', 'd878560888b11447e73324a6e263fbd5iydo1','91a3c57b13234af24875c56fb7e2b2f4rb56a']
# build a DataFrame for the choosed indices
samples = pd.DataFrame(cnt_bidder.loc[indices], columns=cnt_bidder.keys()).reset_index(drop=True); print(samples)
# 使用 seaborn 来对上面四个例子的热力图进行可视化, 看看 percentile 的情况
pcts = 100. * cnt_bidder.rank(axis=0, pct=True).loc[indices].round(decimals=3); print(pcts)
sns.heatmap(pcts, yticklabels=['robot 1', 'robot 2', 'human 1', 'human 2'], annot=True, linewidth=.1, vmax=99, fmt='.1f', cmap='YlGnBu')
plt.title('Percentile ranks of\nsamples\' feature statistics'); plt.xticks(rotation=45, ha='center'); plt.show()
# 由上面的热力图对比可以看到, 机器人的各项统计指标除去商品类别上的统计以外, 均比人类用户要高, 所以考虑据此设计基于基本统计指标规则的基准模型,
# 其中最显著的特征差异应该是在 auc_mean 一项即用户在各个拍卖场的平均竞标次数, 不妨先按照异常值处理的方法来找出上述基础统计中的异常情况
##################################################################
## 二(4): 设计朴素分类器
# 由于最终目的是从竞标者中寻找到机器人用户, 而根据常识, 机器人用户的各项竞标行为的操作应该比人类要频繁许多,
# 所以可以从异常值检验的角度来设计朴素分类器, 根据之前针对不同用户统计的基本特征计数情况, 可以先针对每一个特征找出其中的疑似异常用户列表,
# 最后整合各个特征生成的用户列表, 认为超过多个特征异常的用户为机器人用户
lst_outlier = []  # find the outliers for each feature
for feature in cnt_bidder.keys():
    Q1 = np.percentile(cnt_bidder[feature], 25)  # percentile  25th
    Q3 = np.percentile(cnt_bidder[feature], 75)  # percentile  75th
    step = 1.5 * (Q3 - Q1)
    # show outliers: print "Data points considered outliers for the feature '{}':".format(feature)
    print(cnt_bidder[~((cnt_bidder[feature] >= Q1 - step) & (cnt_bidder[feature] <= Q3 + step))])
    lst_outlier += cnt_bidder[~((cnt_bidder[feature] >= Q1 - step) & (cnt_bidder[feature] <= Q3 + step))].index.values.tolist()
print(len(lst_outlier))  # 267
# 再找到各种特征的所有可能作为'异常值'的用户 id 之后, 可以对其做一个基本统计, 进一步找出其中超过某几个特征值均异常的用户, 经过测试,
# 考虑到原始 train 集合里 bots 用户不到 5%, 所以最终确定以不低于 1 个特征值均异常的用户作为异常用户的一个假设, 由此与 train 集合里的用户进行交叉,
# 可以得到一个用户子集, 可以作为朴素分类器的一个操作方法
freq_outlier = dict(Counter(lst_outlier))
perhaps_outlier = [i for i in freq_outlier if freq_outlier[i] >= 1]; print(len(perhaps_outlier))  # 214
train_pred = df_train[df_train['bidder_id'].isin(perhaps_outlier)]['bidder_id'].tolist(); print(len(train_pred))  # 76
##################################################################
## 二(5): 设计评价指标
# 根据前面数据探索知本实验中的数据集的正负例比例约为 19:1, 有些失衡, 所以考虑使用 auc 这种不受正负例比例影响的评价指标作为衡量标准,
# 现针对所涉及的朴素分类器在原始训练集上的表现得到一个基准得分
y_true = df_train['outcome']
naive_pred = pd.DataFrame(columns=['bidder_id', 'prediction'])
naive_pred['bidder_id'] = df_train['bidder_id']
naive_pred['prediction'] = np.where(naive_pred['bidder_id'].isin(train_pred), 1.0, 0.0)
basic_pred = naive_pred['prediction']
print(roc_auc_score(y_true, basic_pred))  # 0.54661464952

# 在经过上述对基本计数特征的统计之后, 目前尚未针对非类别特征: 时间戳进行处理, 而在之前的数据探索过程中, 针对商品类别和国家这两个类别属性,
#     可以将原始的单一特征转换为多个特征分别统计, 此外, 在上述分析过程中, 我们发现针对用户分组可以进一步对于拍卖场进行分组统计
# 1. 对时间戳进行处理
# 2. 针对商品类别, 国家转换为多个类别分别进行统计
# 3. 按照用户-拍卖场进行分组进一步统计
##################################################################
## 二(6): 对时间戳进行处理
# 主要是分析各个竞标行为的时间间隔, 即统计竞标行为表中在同一拍卖场的各个用户之间的竞标行为间隔,  然后针对每个用户对其他用户的时间间隔计算
# 1. 时间间隔均值
# 2. 时间间隔最大值
# 3. 时间间隔最小值
def generate_timediff():  # 运行这个太慢了, 结果要保存起来
    bids_grouped = df_bids.groupby('auction')
    bds = defaultdict(list)
    last_row = None
    for bids_auc in bids_grouped:
        for i, row in bids_auc[1].iterrows():
            if last_row is None:
                last_row = row
                continue
            time_difference = row['time'] - last_row['time']
            bds[row['bidder_id']].append(time_difference)
            last_row = row
    df = []
    for key in bds.keys(): df.append({'bidder_id': key, 'mean': np.mean(bds[key]), 'min': np.min(bds[key]), 'max': np.max(bds[key])})
    pd.DataFrame(df).to_csv('./tmp_dataset/Kaggle-Facebook-Recruiting-IV-Human-or-Robot/tdiff.csv', index=False)
generate_timediff()  # 这个目前是最费时间的..., 放弃了
##################################################################
## 使用机器学习识别出拍卖场中作弊的机器人用户(二)
# 到上面那步 generate_timediff() 放弃了, 后面的再看看吧
