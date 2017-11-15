#!/usr/bin/python3
# coding: utf-8
# 参考: [机器学习系列(3)_逻辑回归应用之 Kaggle 泰坦尼克之灾](http://blog.csdn.net/han_xiaoyang/article/details/49797143)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 根据每个人的特征来预测此人是否会生存下来
##################################################################
## 一: 数据预览
df = pd.read_csv("./tmp_dataset/Kaggle-Titanic/train.csv")
print(df.shape)  # (891, 12)
print(df.columns.values)  # ['PassengerId' 'Survived' 'Pclass' 'Name' 'Sex' 'Age' 'SibSp' 'Parch' 'Ticket' 'Fare' 'Cabin' 'Embarked']
print(df[:1].values)      # [[1 0 3 'Braund, Mr. Owen Harris' 'male' 22.0 1 0 'A/5 21171' 7.25 nan 'S']]
# Survived => test 集中没有, 也是 test 集要预测的东西
# Pclass => 乘客等级(1/2/3 等舱位)
# SibSp => 堂兄弟/妹个数
# Parch => 父母与小孩个数
# Ticket => 船票信息
# Fare => 票价
# Cabin => 客舱
# Embarked => 登船港口
print(df.info())
# RangeIndex: 891 entries, 0 to 890
# Data columns (total 12 columns):
# Age            714 non-null float64
# Fare           891 non-null float64
# Cabin          204 non-null object
# Embarked       889 non-null object
# 训练数据中总共有 891 名乘客, 但是很不幸, 我们有些属性的数据不全, 比如说:
# Age(年龄)属性只有 714 名乘客有记录; Cabin(客舱)更是只有 204 名乘客是已知的
print(df.describe())
#        PassengerId    Survived      Pclass         Age       SibSp       Parch        Fare
# count   891.000000  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
# mean    446.000000    0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
# mean 字段告诉我们, 大概 0.383838 的人最后获救了, 2/3 等舱的人数比 1 等舱要多, 平均乘客年龄大概是 29.7 岁(计算这个时候会略掉无记录的)等等
##################################################################
## plot 查看各属性之间的关系; 每个/多个 属性和最后的 Survived 之间有着什么样的关系
plt.subplot2grid((2, 3), (0, 0)); df.Survived.value_counts().plot(kind='bar'); plt.title("获救情况 (1 为获救)"); plt.ylabel("人数")
plt.subplot2grid((2, 3), (0, 1)); df.Pclass.value_counts().plot(kind="bar"); plt.ylabel("人数"); plt.title("乘客等级分布")
plt.subplot2grid((2, 3), (0, 2)); plt.scatter(df.Survived, df.Age); plt.ylabel("年龄"); plt.grid(b=True, which='major', axis='y'); plt.title("按年龄看获救分布 (1 为获救)")

plt.subplot2grid((2, 3), (1, 0), colspan=2)
df.Age[df.Pclass == 1].plot(kind='kde')
df.Age[df.Pclass == 2].plot(kind='kde')
df.Age[df.Pclass == 3].plot(kind='kde')
plt.xlabel("年龄"); plt.ylabel("密度"); plt.title("各等级的乘客年龄分布")
plt.legend(('头等舱', '2 等舱', '3 等舱'), loc='best')  # sets our legend for our graph.

plt.subplot2grid((2, 3), (1, 2)); df.Embarked.value_counts().plot(kind='bar'); plt.title("各登船口岸上船人数"); plt.ylabel("人数")
plt.show()
# bingo, 图还是比数字好看多了. 所以我们在图上可以看出来, 被救的人 300 多点, 不到半数; 3 等舱乘客灰常多; 遇难和获救的人年龄似乎跨度都很广;
#     3 个不同的舱年龄总体趋势似乎也一致, 2/3 等舱乘客 20 岁多点的人最多, 1 等舱 40 岁左右的最多; 登船港口人数按照 S 、 C 、 Q 递减,
#     而且 S 远多于另外俩港口.
# 这个时候我们可能会有一些想法了:
#     不同舱位/乘客等级可能和财富/地位有关系, 最后获救概率可能会不一样
#     年龄对获救概率也一定是有影响的, 毕竟前面说了, 副船长还说『小孩和女士先走』呢
#     和登船港口是不是有关系呢？也许登船港口不同, 人的出身地位不同？
#     口说无凭, 空想无益. 老老实实再来统计统计, 看看这些属性值的统计分布吧.
##################################################################
## 属性与获救结果的关联统计
## 各乘客等级的获救情况
Survived_0 = df.Pclass[df.Survived == 0].value_counts()
Survived_1 = df.Pclass[df.Survived == 1].value_counts()
tmp_df = pd.DataFrame({'获救': Survived_1, '未获救': Survived_0})
tmp_df.plot(kind='bar', stacked=True)  # 横坐标是 index, 纵坐标是 columns
plt.title("各乘客等级的获救情况"); plt.xlabel("乘客等级"); plt.ylabel("人数")
plt.show()
# 啧啧, 果然, 钱和地位对舱位有影响, 进而对获救的可能性也有影响啊
# 咳咳, 跑题了, 我想说的是, 明显等级为 1 的乘客, 获救的概率高很多. 恩, 这个一定是影响最后获救结果的一个特征
## 各性别的获救情况
male = df.Survived[df.Sex == 'male'].value_counts()
female = df.Survived[df.Sex == 'female'].value_counts()
pd.DataFrame({'male': male, 'female': female}).plot(kind='bar', stacked=True)
plt.xlabel("获救情况"); plt.ylabel("人数")
plt.show()
## 然后我们再来看看各种舱级别情况下各性别的获救情况
fig=plt.figure(); fig.set(alpha=0.65) # 设置图像透明度, 无所谓
plt.title("根据舱等级和性别的获救情况")
ax1 = fig.add_subplot(141)
df.Survived[df.Sex == 'female'][df.Pclass != 3].value_counts().plot(kind='bar', label="female highclass", color='#FA2479')
ax1.set_xticklabels([u"获救", u"未获救"], rotation=0); plt.legend([u"女性/高级舱"], loc='best')
ax2=fig.add_subplot(142, sharey=ax1)
df.Survived[df.Sex == 'female'][df.Pclass == 3].value_counts().plot(kind='bar', label='female, low class', color='pink')
ax2.set_xticklabels([u"未获救", u"获救"], rotation=0); plt.legend([u"女性/低级舱"], loc='best')
ax3=fig.add_subplot(143, sharey=ax1)
df.Survived[df.Sex == 'male'][df.Pclass != 3].value_counts().plot(kind='bar', label='male, high class',color='lightblue')
ax3.set_xticklabels([u"未获救", u"获救"], rotation=0); plt.legend([u"男性/高级舱"], loc='best')
ax4=fig.add_subplot(144, sharey=ax1)
df.Survived[df.Sex == 'male'][df.Pclass == 3].value_counts().plot(kind='bar', label='male low class', color='steelblue')
ax4.set_xticklabels([u"未获救", u"获救"], rotation=0); plt.legend([u"男性/低级舱"], loc='best')
plt.show()  # 可以发现 女性 获救比例很高
##################################################################
## 我们看看各登船港口的获救情况
Survived_0 = df.Embarked[df.Survived == 0].value_counts()
Survived_1 = df.Embarked[df.Survived == 1].value_counts()
tmp_df = pd.DataFrame({'获救': Survived_1, '未获救': Survived_0})
tmp_df.plot(kind='bar', stacked=True); plt.title("各登录港口乘客的获救情况"); plt.xlabel("登录港口"); plt.ylabel("人数")
plt.show() # C 港口获救率比较高, 但也不一定
##################################################################
## 堂兄弟/妹, 孩子/父母有几人, 对是否获救的影响
g = df.groupby(['SibSp', 'Survived'])
tmp_df = pd.DataFrame(g.count()['PassengerId'])  # 这里用
print(tmp_df)  # 堂兄弟个数 和 获救之间的关系
g = df.groupby(['Parch','Survived'])
tmp_df = pd.DataFrame(g.count()['PassengerId'])
print(tmp_df)
# 好吧, 没看出特别特别明显的规律(为自己的智商感到捉急…), 先作为备选特征, 放一放
##################################################################
## ticket 是船票编号, 应该是 unique 的, 和最后的结果没有太大的关系, 先不纳入考虑的特征范畴把
## cabin 只有 204 个乘客有值, 我们先看看它的一个分布
print(df.Cabin.value_counts())  # 分类统计
# 关键是 Cabin 这鬼属性, 应该算作类目型的, 本来缺失值就多, 还如此不集中, 注定是个棘手货, 第一感觉,
# 这玩意儿如果直接按照类目特征处理的话, 太散了, 估计每个因子化后的特征都拿不到什么权重
# 加上有那么多缺失值, 要不我们先把 Cabin 缺失与否作为条件(虽然这部分信息缺失可能并非未登记, maybe 只是丢失了而已, 所以这样做未必妥当),
##################################################################
## 先在有无 Cabin 信息这个粗粒度上看看 Survived 的情况好了
Survived_cabin = df.Survived[pd.notnull(df.Cabin)].value_counts()
Survived_nocabin = df.Survived[pd.isnull(df.Cabin)].value_counts()
tmp_df = pd.DataFrame({'有': Survived_cabin, '无': Survived_nocabin}).transpose()
tmp_df.plot(kind='bar', stacked=True)
plt.title("按 Cabin 有无看获救情况"); plt.xlabel("Cabin 有无"); plt.ylabel("人数"); plt.show()
# 咳咳, 有 Cabin 记录的似乎获救概率稍高一些, 先这么着放一放吧
##################################################################
## 二: 数据预处理
# 大体数据的情况看了一遍, 对感兴趣的属性也有个大概的了解了; 下一步干啥？咱们该处理处理这些数据, 为机器学习建模做点准备了
# 这里说的数据预处理, 其实就包括了很多 Kaggler 津津乐道的 feature engineering 过程, 灰常灰常有必要！
# 『特征工程(feature engineering)太重要了！』
##################################################################
## 先从最突出的数据属性开始吧, 对, Cabin 和 Age, 有丢失数据实在是对下一步工作影响太大.
# 先说 Cabin, 暂时我们就按照刚才说的, 按 Cabin 有无数据, 将这个属性处理成 Yes 和 No 两种类型吧
# 再说 Age:
# 通常遇到缺值的情况, 我们会有几种常见的处理方式
# 如果缺值的样本占总数比例极高, 我们可能就直接舍弃了, 作为特征加入的话, 可能反倒带入 noise, 影响最后的结果了
# 如果缺值的样本适中, 而该属性非连续值特征属性(比如说类目属性), 那就把 NaN 作为一个新类别, 加到类别特征中
# 如果缺值的样本适中, 而该属性为连续值特征属性, 有时候我们会考虑给定一个 step(比如这里的 age, 我们可以考虑每隔 2/3 岁为一个步长),
#     然后把它离散化, 之后把 NaN 作为一个 type 加到属性类目中
# 有些情况下, 缺失的值个数并不是特别多, 那我们也可以试着根据已有的值, 拟合一下数据, 补充上

# 本例中, 后两种处理方式应该都是可行的, 我们先试试拟合补全吧(虽然说没有特别多的背景可供我们拟合, 这不一定是一个多么好的选择)
# 我们这里用 scikit-learn 中的 RandomForest 来拟合一下缺失的年龄数据(注: RandomForest 是一个用在原始数据中做不同采样, 建立多颗 DecisionTree,
#     再进行 average 等等来降低过拟合现象, 提高结果的机器学习算法, 我们之后会介绍到)
from sklearn.ensemble import RandomForestRegressor  # 使用 RandomForestClassifier 填补缺失的年龄属性
def set_missing_ages(df):
    age_df = df[['Age', 'Fare', 'Parch', 'SibSp', 'Pclass']]  # 把已有的数值型特征取出来丢进 Random Forest Regressor 中
    known_age = age_df[age_df.Age.notnull()].as_matrix()
    unknown_age = age_df[age_df.Age.isnull()].as_matrix()  # 乘客分成已知年龄和未知年龄两部分
    X = known_age[:, 1:]  # X 即特征属性值
    y = known_age[:, 0]  # y 即目标年龄
    rfr = RandomForestRegressor(random_state=0, n_estimators=2000, n_jobs=-1)  # fit 到 RandomForestRegressor 之中
    rfr.fit(X, y)
    predictedAges = rfr.predict(unknown_age[:, 1::])  # 用得到的模型进行未知年龄结果预测
    df.loc[(df.Age.isnull()), 'Age'] = predictedAges  # 用得到的预测结果填补原缺失数据
    return df, rfr
def set_Cabin_type(df):
    df.loc[(df.Cabin.notnull()), 'Cabin'] = "Yes"
    df.loc[(df.Cabin.isnull()), 'Cabin'] = "No"
    return df
df, rfr = set_missing_ages(df)
df = set_Cabin_type(df)
print(df.info())  # 显示没有缺失值了; 目的达到, OK 了.
##################################################################
## 因为逻辑回归建模时, 需要输入的特征都是数值型特征, 我们通常会先对类目型的特征因子化.
# 什么叫做因子化呢？举个例子:
# 以 Cabin 为例, 原本一个属性维度, 因为其取值可以是 ['yes','no'], 而将其平展开为 'Cabin_yes', 'Cabin_no' 两个属性
# 原本 Cabin 取值为 yes 的, 在此处的"Cabin_yes"下取值为 1, 在"Cabin_no"下取值为 0
# 原本 Cabin 取值为 no 的, 在此处的"Cabin_yes"下取值为 0, 在"Cabin_no"下取值为 1
# 我们使用 pandas 的 "get_dummies" 来完成这个工作, 并拼接在原来的 "df" 之上, 如下所示.
dummies_Cabin = pd.get_dummies(df['Cabin'], prefix= 'Cabin'); print(dummies_Cabin.head())
dummies_Embarked = pd.get_dummies(df['Embarked'], prefix= 'Embarked'); print(dummies_Embarked.head())
dummies_Sex = pd.get_dummies(df['Sex'], prefix= 'Sex'); print(dummies_Sex.head())
dummies_Pclass = pd.get_dummies(df['Pclass'], prefix= 'Pclass'); print(dummies_Pclass.head())
# print(pd.get_dummies(df))  # 不能这样, 否则会很多
# dumies = pd.get_dummies(df[['Cabin', 'Embarked', 'Sex', 'Pclass']]); print(dumies.head())  # 不能这样写, 因为 Pclass 本身就是数值型, 不会发生变化
df = pd.concat([df, dummies_Cabin, dummies_Embarked, dummies_Sex, dummies_Pclass], axis=1)
df.drop(['Pclass', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)
print(df.head())
# bingo, 我们很成功地把这些类目属性全都转成 0, 1 的数值属性了.
# 这样, 看起来, 是不是我们需要的属性值都有了, 且它们都是数值型属性呢.
# 有一种临近结果的宠宠欲动感吧, 莫急莫急, 我们还得做一些处理, 仔细看看 Age 和 Fare 两个属性, 乘客的数值幅度变化, 也忒大了吧！！
#     如果大家了解逻辑回归与梯度下降的话, 会知道, 各属性值之间 scale 差距太大, 将对收敛速度造成几万点伤害值！甚至不收敛！
##################################################################
## scikit-learn 里面的 preprocessing 模块对这俩货做一个 scaling, 所谓 scaling, 其实就是将一些变化幅度较大的特征化到 [-1, 1] 之内.
import sklearn.preprocessing as preprocessing
scaler = preprocessing.StandardScaler()
df['Age_scaled'] = scaler.fit_transform(df['Age'].values.reshape(-1, 1))
df['Fare_scaled'] = scaler.fit_transform(df['Fare'].values.reshape(-1, 1))
print(df.head())
# 好看多了, 万事俱备, 只欠建模; 马上就要看到成效了, 哈哈; 我们把需要的属性值抽出来, 转成 scikit-learn 里面 LogisticRegression 可以处理的格式.
##################################################################
## 测试集预处理; 对 test_data 做和 train_data 中一致的特征变换; 这部分本来在原文的 建模以后, 但放到这里比较合适
data_test = pd.read_csv("./tmp_dataset/Kaggle-Titanic/test.csv")
data_test.loc[(data_test.Fare.isnull()), 'Fare'] = 0  # 将缺失数据补全
## 首先用同样的 RandomForestRegressor 模型填上丢失的年龄
tmp_df = data_test[['Age','Fare', 'Parch', 'SibSp', 'Pclass']]
null_age = tmp_df[data_test.Age.isnull()].as_matrix()
# 根据特征属性 X 预测年龄并补上
X = null_age[:, 1:]
predictedAges = rfr.predict(X)
data_test.loc[(data_test.Age.isnull()), 'Age'] = predictedAges
## 补全并转换 Cabin, 非空 Yes, 空为 No
data_test = set_Cabin_type(data_test)
## 特征因子化
dummies_Cabin = pd.get_dummies(data_test['Cabin'], prefix= 'Cabin')
dummies_Embarked = pd.get_dummies(data_test['Embarked'], prefix= 'Embarked')
dummies_Sex = pd.get_dummies(data_test['Sex'], prefix= 'Sex')
dummies_Pclass = pd.get_dummies(data_test['Pclass'], prefix= 'Pclass')
df_test = pd.concat([data_test, dummies_Cabin, dummies_Embarked, dummies_Sex, dummies_Pclass], axis=1)
df_test.drop(['Pclass', 'Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)
df_test['Age_scaled'] = scaler.fit_transform(df_test['Age'].values.reshape(-1, 1))
df_test['Fare_scaled'] = scaler.fit_transform(df_test['Fare'].values.reshape(-1, 1))
print(df_test.head())
##################################################################
## 三: 逻辑回归建模
# 我们把需要的 feature 字段取出来, 转成 numpy 格式, 使用 scikit-learn 中的 LogisticRegression 建模
from sklearn import linear_model
train_df = df.filter(regex='Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')  # 用正则取出我们要的属性值
train_np = train_df.as_matrix()
y = train_np[:, 0]; print(y)  # y 即 Survival 结果; 没有 PassengerId, Survived 就是第一列
X = train_np[:, 1:]; print(X)  # X 即特征属性值
# fit 到 RandomForestRegressor 之中
clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
clf.fit(X, y)
print(clf)
##################################################################
## 四: 交叉验证
# 这部分在 模型优化 下面
##################################################################
## 五: 预测取结果
test = df_test.filter(regex='Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')  # 和训练集提取的属性要相同
predictions = clf.predict(test)
result = pd.DataFrame({'PassengerId':data_test['PassengerId'].as_matrix(), 'Survived':predictions.astype(np.int32)})
result.to_csv("./tmp_dataset/Kaggle-Titanic/result.csv", index=False)  # 不要 Index, 但需要 columns
# 0.76555; 提交上去的结果...
##################################################################
## 六: 模型优化, 关联分析; 这里是精华
## 模型系数关联分析
# 亲, 你以为结果提交上了, 就完事了？
# 我不会告诉你, 这只是万里长征第一步啊(泪牛满面)！！！这才刚撸完 baseline model 啊！！！还得优化啊！！！
# 看过 Andrew Ng 老师的 machine Learning 课程的同学们, 知道, 我们应该分析分析模型现在的状态了, 是过/欠拟合？
#     以确定我们需要更多的特征还是更多数据, 或者其他操作. 我们有一条很著名的 learning curves 对吧.
# 不过在现在的场景下, 先不着急做这个事情, 我们这个 baseline 系统还有些粗糙, 先再挖掘挖掘.
# 首先, Name 和 Ticket 两个属性被我们完整舍弃了(好吧, 其实是因为这俩属性, 几乎每一条记录都是一个完全不同的值, 我们并没有找到很直接的处理方式).
# 然后, 我们想想, 年龄的拟合本身也未必是一件非常靠谱的事情, 我们依据其余属性, 其实并不能很好地拟合预测出未知的年龄.
#     再一个, 以我们的日常经验, 小盆友和老人可能得到的照顾会多一些, 这样看的话, 年龄作为一个连续值, 给一个固定的系数,
#     应该和年龄是一个正相关或者负相关, 似乎体现不出两头受照顾的实际情况, 所以, 说不定我们把年龄离散化, 按区段分作类别属性会更合适一些.

# 上面只是我瞎想的, who knows 是不是这么回事呢, 老老实实先把得到的 model 系数和 feature 关联起来看看.
print(pd.DataFrame({"columns": list(train_df.columns)[1:], "coef":list(clf.coef_.T)}))
# 首先, 大家回去前两篇文章里瞄一眼公式就知道, 这些系数为正的特征, 和最后结果是一个正相关, 反之为负相关
# 我们先看看那些权重绝对值非常大的 feature, 在我们的模型上:

# Sex 属性, 如果是 female 会极大提高最后获救的概率, 而 male 会很大程度拉低这个概率.
# Pclass 属性, 1 等舱乘客最后获救的概率会上升, 而乘客等级为 3 会极大地拉低这个概率.
# 有 Cabin 值会很大程度拉升最后获救概率(这里似乎能看到了一点端倪, 事实上从最上面的有无 Cabin 记录的 Survived 分布图上看出,
#     即使有 Cabin 记录的乘客也有一部分遇难了, 估计这个属性上我们挖掘还不够)
# Age 是一个负相关, 意味着在我们的模型里, 年龄越小, 越有获救的优先权(还得回原数据看看这个是否合理）
# 有一个登船港口 S 会很大程度拉低获救的概率, 另外俩港口压根就没啥作用(这个实际上非常奇怪, 因为我们从之前的统计图上并没有看到
#     S 港口的获救率非常低, 所以也许可以考虑把登船港口这个 feature 去掉试试).
# 船票 Fare 有小幅度的正相关(并不意味着这个 feature 作用不大, 有可能是我们细化的程度还不够,
#     举个例子, 说不定我们得对它离散化, 再分至各个乘客等级上？)

# 噢啦, 观察完了, 我们现在有一些想法了, 但是怎么样才知道, 哪些优化的方法是 promising 的呢？
# 因为 test.csv 里面并没有 Survived 这个字段(好吧, 这是废话, 这明明就是我们要预测的结果), 我们无法在这份数据上评定我们算法在该场景下的效果…
# 而『每做一次调整就 make a submission, 然后根据结果来判定这次调整的好坏』其实是行不通的…
##################################################################
## 七: 交叉验证
# 重点又来了:
# 『要做交叉验证(cross validation)!』...
# 恩, 重要的事情说三遍. 我们通常情况下, 这么做 cross validation: 把 train.csv 分成两部分, 一部分用于训练我们需要的模型,
#     另外一部分数据上看我们预测算法的效果.
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
# 先简单看看 cross validation 情况下的打分
clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
all_data = df.filter(regex='Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
X = all_data.as_matrix()[:, 1:]
y = all_data.as_matrix()[:, 0]
print(cross_val_score(clf, X, y, cv=5))  # [ 0.81564246  0.81564246  0.78651685  0.78651685  0.81355932]
# 似乎比 Kaggle 上的结果略高哈, 毕竟用的是不是同一份数据集评估的.
# 等等, 既然我们要做交叉验证, 那我们干脆先把交叉验证里面的 bad case 拿出来看看, 看看人眼审核, 是否能发现什么蛛丝马迹, 是我们忽略了哪些信息,
#     使得这些乘客被判定错了. 再把 bad case 上得到的想法和前头系数分析的合在一起, 然后逐个试试.

## 下面我们做数据分割, 并且在原始数据集上瞄一眼 bad case:
split_train, split_cv = train_test_split(df, test_size=0.3, random_state=0)  # 分割数据, 按照 训练数据:cv 数据 = 7:3 的比例
train_df = split_train.filter(regex='Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
# 生成模型
clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
clf.fit(train_df.as_matrix()[:, 1:], train_df.as_matrix()[:, 0])
# 对 cross validation 数据进行预测
cv_df = split_cv.filter(regex='Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass_.*')
predictions = clf.predict(cv_df.as_matrix()[:, 1:])
origin_data_train = pd.read_csv("./tmp_dataset/Kaggle-Titanic/train.csv")
# 下边这行写的好霸气啊!!!
bad_cases = origin_data_train.loc[origin_data_train['PassengerId'].isin(split_cv[predictions != cv_df.as_matrix()[:, 0]]['PassengerId'].values)]
print(bad_cases.head())
# PassengerId  Survived  Pclass  \
# 14           15         0       3
# 49           50         0       3
# 55           56         1       1
# 65           66         1       3
# 68           69         1       3
# 拿到 bad cases 之后, 也会有一些猜测和想法; 其中会有一部分可能会印证在系数分析部分的猜测, 那这些优化的想法优先级可以放高一些

# 现在有了"train_df" 和 "vc_df" 两个数据部分, 前者用于训练 model, 后者用于评定和选择模型. 可以开始可劲折腾了.
# 我们随便列一些可能可以做的优化操作:
# Age 属性不使用现在的拟合方式, 而是根据名称中的『 Mr 』『 Mrs 』『 Miss 』等的平均值进行填充.
# Age 不做成一个连续值属性, 而是使用一个步长进行离散化, 变成离散的类目 feature.
# Cabin 再细化一些, 对于有记录的 Cabin 属性, 我们将其分为前面的字母部分(我猜是位置和船层之类的信息) 和 后面的数字部分
#     (应该是房间号, 有意思的事情是, 如果你仔细看看原始数据, 你会发现, 这个值大的情况下, 似乎获救的可能性高一些).
# Pclass 和 Sex 俩太重要了, 我们试着用它们去组出一个组合属性来试试, 这也是另外一种程度的细化.
# 单加一个 Child 字段, Age<=12 的, 设为 1, 其余为 0(你去看看数据, 确实小盆友优先程度很高啊)
# 如果名字里面有『 Mrs 』, 而 Parch>1 的, 我们猜测她可能是一个母亲, 应该获救的概率也会提高, 因此可以多加一个 Mother 字段,
#     此种情况下设为 1, 其余情况下设为 0
# 登船港口可以考虑先去掉试试(Q 和 C 本来就没权重, S 有点诡异)
# 把堂兄弟/兄妹 和 Parch 还有自己 个数加在一起组一个 Family_size 字段(考虑到大家族可能对最后的结果有影响)
# Name 是一个我们一直没有触碰的属性, 可以做些简单的处理, 比如说男性中带某些字眼的('Capt', 'Don', 'Major', 'Sir')可以统一到一个 Title, 女性也一样.

# 大家接着往下挖掘, 可能还可以想到更多可以细挖的部分. 我这里先列这些了, 然后我们可以使用手头上的"train_df"和"cv_df"
#     开始试验这些 feature engineering 的 tricks 是否有效了.
# 试验的过程比较漫长, 也需要有耐心, 而且我们经常会面临很尴尬的状况, 就是我们灵光一闪, 想到一个 feature, 然后坚信它一定有效,
#     结果试验下来, 效果还不如试验之前的结果. 恩, 需要坚持和耐心, 以及不断的挖掘.

# 我最好的结果是在『 Survived~C(Pclass)+C(Title)+C(Sex)+C(Age_bucket)+C(Cabin_num_bucket)Mother+Fare+Family_Size 』下取得的,
#     结果如下(抱歉, 博主君 commit 的时候手抖把页面关了, 于是没截着图, 下面这张图是在我得到最高分之后, 用这次的结果重新 make commission 的,
#     截了个图, 得分是 0.79426, 不是目前我的最高分哈, 因此排名木有变…):

# 有一个很可能发生的问题是, 我们不断地做 feature engineering, 产生的特征越来越多, 用这些特征去训练模型,
#     会对我们的训练集拟合得越来越好, 同时也可能在逐步丧失泛化能力, 从而在待预测的数据上, 表现不佳, 也就是发生过拟合问题.
# 从另一个角度上说, 如果模型在待预测的数据上表现不佳, 除掉上面说的过拟合问题, 也有可能是欠拟合问题, 也就是说在训练集上, 其实拟合的也不是那么好

# 过拟合就像是你班那个学数学比较刻板的同学, 老师讲过的题目, 一字不漏全记下来了, 于是老师再出一样的题目, 分分钟精确出结果.
#     but 数学考试, 因为总是碰到新题目, 所以成绩不咋地.
# 欠拟合就像是, 连老师讲的练习题也记不住, 于是连老师出一样题目复习的周测都做不好, 考试更是可想而知了.

# 而在机器学习的问题上, 对于过拟合和欠拟合两种情形. 我们优化的方式是不同的.
# 对过拟合而言, 通常以下策略对结果优化是有用的:
# 做一下 feature selection, 挑出较好的 feature 的 subset 来做 training 提供更多的数据, 从而弥补原始数据的 bias 问题, 学习到的 model 也会更准确
# 而对于欠拟合而言, 我们通常需要更多的 feature, 更复杂的模型来提高准确度.

# 著名的 learning curve 可以帮我们判定我们的模型现在所处的状态. 我们以样本数为横坐标, 训练和交叉验证集上的错误率作为纵坐标,
#     两种状态分别如下两张图所示: 过拟合(overfitting/high variace), 欠拟合(underfitting/high bias)

##################################################################
## 我们也可以把错误率替换成准确率(得分), 得到另一种形式的 learning curve(sklearn 里面是这么做的).
# 回到我们的问题, 我们用 scikit-learn 里面的 learning_curve 来帮我们分辨我们模型的状态.
#     举个例子, 这里我们一起画一下我们最先得到的 baseline model 的 learning curve.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve  # 用 sklearn 的 learning_curve 得到 training_score 和 cv_score, 使用 matplotlib 画出 learning curve
def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None, n_jobs=1, train_sizes=np.linspace(.05, 1., 20), verbose=0, plot=True):
    # 画出 data 在某模型上的 learning curve.
    # estimator: 你用的分类器
    # title: 表格的标题
    # X: 输入的 feature, numpy 类型
    # y: 输入的 target vector
    # ylim: tuple 格式的(ymin, ymax), 设定图像中纵坐标的最低点和最高点
    # cv: 做 cross-validation 的时候, 数据分成的份数, 其中一份作为 cv 集, 其余 n-1 份作为 training(默认为 3 份)
    # n_jobs: 并行的的任务数(默认 1)
    train_sizes, train_scores, test_scores = learning_curve(estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes, verbose=verbose)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    if plot:
        plt.figure()
        plt.title(title)
        if ylim is not None: plt.ylim(*ylim)
        plt.xlabel("训练样本数")
        plt.ylabel("得分")
        plt.gca().invert_yaxis()
        plt.grid()
        plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.1, color="b")
        plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.1, color="r")
        plt.plot(train_sizes, train_scores_mean, 'o-', color="b", label="训练集上得分")
        plt.plot(train_sizes, test_scores_mean, 'o-', color="r", label="交叉验证集上得分")
        plt.legend(loc="best")
        plt.draw()
        plt.show()
        plt.gca().invert_yaxis()
    midpoint = ((train_scores_mean[-1] + train_scores_std[-1]) + (test_scores_mean[-1] - test_scores_std[-1])) / 2
    diff = (train_scores_mean[-1] + train_scores_std[-1]) - (test_scores_mean[-1] - test_scores_std[-1])
    return midpoint, diff
plot_learning_curve(clf, "学习曲线", X, y)
##################################################################
## 八: 模型融合
# 好了, 终于到这一步了, 我们要祭出机器学习/数据挖掘上通常最后会用到的大杀器了. 恩, 模型融合.
# 『模型融合(model ensemble)很重要！』
# 啥叫模型融合呢, 我们还是举几个例子直观理解一下好了.
# 大家都看过知识问答的综艺节目中, 求助现场观众时候, 让观众投票, 最高的答案作为自己的答案的形式吧, 每个人都有一个判定结果,
#     最后我们相信答案在大多数人手里.
# 再通俗一点举个例子. 你和你班某数学大神关系好, 每次作业都『模仿』他的, 于是绝大多数情况下, 他做对了, 你也对了.
#     突然某一天大神脑子犯糊涂, 手一抖, 写错了一个数, 于是…恩, 你也只能跟着错了.
# 我们再来看看另外一个场景, 你和你班 5 个数学大神关系都很好, 每次都把他们作业拿过来, 对比一下, 再『自己做』, 那你想想,
#     如果哪天某大神犯糊涂了, 写错了, but 另外四个写对了啊, 那你肯定相信另外 4 人的是正确答案吧？
# 最简单的模型融合大概就是这么个意思, 比如分类问题, 当我们手头上有一堆在同一份数据集上训练得到的分类器
#     (比如 logistic regression, SVM, KNN, random forest, 神经网络), 那我们让他们都分别去做判定, 然后对结果做投票统计, 取票数最多的结果为最后结果.

# 模型融合可以比较好地缓解, 训练过程中产生的过拟合问题, 从而对于结果的准确度提升有一定的帮助.
# 话说回来, 回到我们现在的问题. 你看, 我们现在只讲了 logistic regression, 如果我们还想用这个融合思想去提高我们的结果, 我们该怎么做呢？
# 既然这个时候模型没得选, 那咱们就在数据上动动手脚咯. 大家想想, 如果模型出现过拟合现在, 一定是在我们的训练上出现拟合过度造成的对吧.
# 那我们干脆就不要用全部的训练集, 每次取训练集的一个 subset, 做训练, 这样, 我们虽然用的是同一个机器学习算法,
#     但是得到的模型却是不一样的；同时, 因为我们没有任何一份子数据集是全的, 因此即使出现过拟合, 也是在子训练集上出现过拟合,
#     而不是全体数据上, 这样做一个融合, 可能对最后的结果有一定的帮助. 对, 这就是常用的 Bagging.
# 我们用 scikit-learn 里面的 Bagging 来完成上面的思路, 过程非常简单. 代码如下:
from sklearn.ensemble import BaggingRegressor
train_df = df.filter(regex='Survived|Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass.*|Mother|Child|Family|Title')
train_np = train_df.as_matrix()
y = train_np[:, 0]  # y 即 Survival 结果
X = train_np[:, 1:]  # X 即特征属性值
clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)  # fit 到 BaggingRegressor 之中
bagging_clf = BaggingRegressor(clf, n_estimators=20, max_samples=0.8, max_features=1.0, bootstrap=True, bootstrap_features=False, n_jobs=-1)
bagging_clf.fit(X, y)
test = df_test.filter(regex='Age_.*|SibSp|Parch|Fare_.*|Cabin_.*|Embarked_.*|Sex_.*|Pclass.*|Mother|Child|Family|Title')
predictions = bagging_clf.predict(test)
result = pd.DataFrame({'PassengerId':data_test['PassengerId'].as_matrix(), 'Survived':predictions.astype(np.int32)})
result.to_csv("./tmp_dataset/Kaggle-Titanic/result.csv", index=False)
# 0.75598; 竟然更低了, 可能是 BaggingRegressor 随机分配的时候运气不好
# 上一个结果和博客中作者的结果一毛一样, 第二次竟然不一样了
