#!/usr/bin/python3
# coding: utf-8
# 在数据挖掘工作中, 通常处理的是一个包含大量特征且含义未知的数据集, 并基于该数据集挖掘到有用的特征. 那么这里面一般是四个步骤:
#     特征工程、特征选择、模型构造、模型融合.
# 特征工程主要是清洗特征、删除无用特征和构造新特征, 经过特征工程这个过程我们可能会得到大量的特征;
# 而特征选择的目的就是从这大量的特征中挑选出优秀的特征, 因为好的特征更能够提升模型性能, 同时也通过降维达到了避免维度灾难的目的.
# 本文主要利用 sklearn 这个工具来实现常用的特征选择方法.

# 特征选择有两个功能: 1.减少特征数量, 起到降维作用, 使泛化能力更强; 2.减少过拟合, 增强对特征和特征值之间的理解
# 本文主要基于 sklearn 介绍两大类特征选择方法:
# 单变量特征选择方法, 这里面主要包括皮尔森相关系数、最大信息系数、距离相关系数等, 主要思想是衡量特征和标签变量之间的相关性;
# 基于模型的特征选择方法, 这主要是指模型在训练过程中对特征的排序, 如基于随机森林的特征选择、基于逻辑回归的特征选择等

# sklearn.feature_selection 模块中的类能够用于数据集的特征选择/降维, 以此来提高预测模型的准确率或改善它们在高维数据集上的表现
##################################################################
## 1. 移除低方差的特征(Removing features with low variance)
from sklearn.feature_selection import VarianceThreshold
# VarianceThreshold 是特征选择中的一项基本方法. 它会移除所有方差不满足阈值的特征.
# 默认设置下, 它将移除所有方差为 0 的特征, 即那些在所有样本中数值完全相同的特征.

# 假设我们有一个带有布尔特征的数据集, 我们要移除那些超过 80% 的数据都为 1 或 0 的特征.
# 布尔特征是伯努利随机变量, 该类变量的方差为: var(x) = p(1 - p); 所以我们可以使用阈值 .8 * (1 - .8)
X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]; print(X)
sel = VarianceThreshold(threshold=(.8*(1-.8)))
print(sel.fit_transform(X))  # [[0 1] [1 0] [0 0] [1 1] [1 0] [1 1]]; 可以发现, 将第一列删除了...
# 果然, VarianceThreshold 移除了第一列特征, 第一列中特征值为 0 的概率达到了 p = 5/6 > 0.8
##################################################################
## 2. 单变量特征选择(Univariate feature selection)
# 单变量特征选择基于单变量的统计测试来选择最佳特征.
# SelectKBest 移除得分前 k 名以外的所有特征
# SelectPercentile 移除得分在用户指定百分比以后的特征
# 对每个特征使用通用的单变量统计测试:  假正率(false positive rate) SelectFpr, 伪发现率(false discovery rate) SelectFdr, 或族系误差率 SelectFwe.
# GenericUnivariateSelect 可以设置不同的策略来进行单变量特征选择. 同时不同的选择策略也能够使用超参数寻优, 从而让我们找到最佳的单变量特征选择策略.
# 比如, 我们可以对样本进行一次 :math:`chi^2 测试来选择最佳的两项特征:
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
iris = load_iris()
X, y = iris.data, iris.target; print(X.shape)  # (150, 4)
X_new = SelectKBest(chi2, k=2).fit_transform(X, y); print(X_new.shape)  # (150, 2)
##################################################################
## 3. 递归特征消除(Recursive feature elimination)
# The Recursive Feature Elimination (RFE) method is a feature selection approach. It works by recursively removing attributes and
#     building a model on those attributes that remain. It uses the model accuracy to identify which attributes (and combination of attributes)
#     contribute the most to predicting the target attribute.
from sklearn import datasets
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
dataset = datasets.load_iris()  # load the iris datasets
model = LogisticRegression()  # create a base classifier used to evaluate a subset of attributes
rfe = RFE(model, 3)  # create the RFE model and select 3 attributes
rfe = rfe.fit(dataset.data, dataset.target)
# summarize the selection of the attributes
print(rfe.support_)  # [False  True  True  True]
print(rfe.ranking_)  # [2 1 1 1]
X_new = rfe.transform(dataset.data); print(X_new.shape)  # (150, 3)
# 对于一个伪数据特征指定权重的预测模型(例如, 线性模型对应参数 coefficients), 递归特征消除 (RFE)通过递归减少考察的特征集规模来选择特征.
#     首先, 预测模型在原始特征上训练, 每项特征指定一个权重. 之后, 那些拥有最小绝对值权重的特征被踢出特征集.
#     如此往复递归, 直至剩余的特征数量达到所需的特征数量.
##################################################################
## 4. 使用 SelectFromModel 选择特征(Feature selection using SelectFromModel)
# SelectFromModel 作为 meta-transformer, 能够用于拟合后任何拥有 coef_ 或 feature_importances_ 属性的预测模型.
#     如果特征对应的 coef_ 或 feature_importances_ 值低于设定的阈值 threshold, 那么这些特征将被移除.
#     除了手动设置阈值, 也可通过字符串参数调用内置的启发式算法(heuristics)来设置阈值,
#     包括: 平均值("mean"), 中位数("median")以及他们与浮点数的乘积, 如" 0.1*mean ".
##################################################################
## 4.1. 基于 L1 的特征选择(L1-based feature selection)
# 使用 L1 范数作为惩罚项的: ref:Linear models <linear_model> 会得到稀疏解: 大部分特征对应的系数为 0.
#     当你希望减少特征的维度以用于其它分类器时, 可以通过 feature_selection.SelectFromModel 来选择不为 0 的系数.
#     特别指出, 常用于此目的的稀疏预测模型有 linear_model.Lasso (回归),  linear_model.LogisticRegression 和 svm.LinearSVC (分类):
from sklearn.svm import LinearSVC
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel
iris = load_iris()
X, y = iris.data, iris.target; print(X.shape)  # (150, 4)
lsvc = LinearSVC(C=0.01, penalty="l1", dual=False).fit(X, y)
model = SelectFromModel(lsvc, prefit=True)
X_new = model.transform(X); print(X_new.shape)  # (150, 3)
# 对于 SVM 和逻辑回归, 参数 C 控制稀疏性: C 越小, 被选中的特征越少.
# 对于 Lasso, 参数 alpha 越大, 被选中的特征越少 .
##################################################################
## 4.2. 随机稀疏模型(Randomized sparse models)
##################################################################
## 4.3. 基于树的特征选择(Tree-based feature selection)
# 基于树的预测模型(见 sklearn.tree 模块, 森林见 sklearn.ensemble 模块)能够用来计算特征的重要程度,
#      因此能用来去除不相关的特征(结合 sklearn.feature_selection.SelectFromModel ):
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectFromModel
iris = load_iris()
X, y = iris.data, iris.target; print(X.shape)  # (150, 4)
clf = ExtraTreesClassifier()
clf = clf.fit(X, y)
print(clf.feature_importances_)  # [ 0.09409518  0.08364283  0.34668866  0.47557332]
model = SelectFromModel(clf, prefit=True)
X_new = model.transform(X); print(X_new.shape)  # (150, 2)
##################################################################
## 5. 特征选择融入 pipeline(Feature selection as part of a pipeline)
# 特征选择常常被当作学习之前的一项预处理. 在 scikit-learn 中推荐使用 sklearn.pipeline.Pipeline:
clf = Pipeline([
  ('feature_selection', SelectFromModel(LinearSVC(penalty="l1"))),
  ('classification', RandomForestClassifier())
])
clf.fit(X, y)
# 在此代码片段中, 我们将 sklearn.svm.LinearSVC 和 sklearn.feature_selection.SelectFromModel 结合来评估特征的重要性, 并选择最相关的特征.
# 之后 sklearn.ensemble.RandomForestClassifier 模型使用转换后的输出训练, 即只使用被选出的相关特征. 你可以选择其它特征选择方法,
#     或是其它提供特征重要性评估的分类器. 更多详情见 sklearn.pipeline.Pipeline 相关示例.
