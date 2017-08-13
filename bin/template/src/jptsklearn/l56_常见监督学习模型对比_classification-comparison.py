#!/usr/bin/python3
# coding: utf-8
##################################################################
## 第一步, 加载本次实验需要的模块, 以及 scikit-learn 中常见的分类器
from matplotlib import pyplot as plt                  # 导入绘图模块
import numpy as np                                    # 导入数值计算模块
from sklearn.model_selection import train_test_split  # 导入数据集切分模块
from sklearn.metrics import accuracy_score            # 导入准确度评估模块
import pandas as pd                                   # 加载 pandas 模块
from matplotlib.colors import ListedColormap          # 加载色彩模块

# 集成方法分类器
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.gaussian_process import GaussianProcessClassifier  # 高斯过程分类器

# 广义线性分类器
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import SGDClassifier

from sklearn.neighbors import KNeighborsClassifier  # K 近邻分类器

from sklearn.naive_bayes import GaussianNB  # 朴素贝叶斯分类器

from sklearn.neural_network import MLPClassifier  # 神经网络分类器

# 决策树分类器
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import ExtraTreeClassifier

# 支持向量机分类器
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
##################################################################
## 接下来, 建立预测模型, 采用预设参数即可; 由于方法较多, 所有这里就不再单独新建模型, 而是用列表形式管理
model = [
    AdaBoostClassifier(), BaggingClassifier(), ExtraTreesClassifier(), GradientBoostingClassifier(), RandomForestClassifier(),
    GaussianProcessClassifier(),
    PassiveAggressiveClassifier(), RidgeClassifier(), SGDClassifier(),
    KNeighborsClassifier(),
    GaussianNB(),
    MLPClassifier(),
    DecisionTreeClassifier(), ExtraTreeClassifier(),
    SVC(), LinearSVC()
]  # 依次为模型命名
classifier_Names = ['AdaBoost', 'Bagging', 'ExtraTrees', 'GradientBoosting', 'RandomForest',
                    'GaussianProcess',
                    'PassiveAggressive', 'Ridge', 'SGD',
                    'KNeighbors',
                    'GaussianNB',
                    'MLP',
                    'DecisionTree', 'ExtraTree',
                    'SVC', 'LinearSVC']
##################################################################
## 然后, 读取数据集并切分; 70% 用于训练, 另外 30% 用于测试
data = pd.read_csv("class_data.csv", header=0)  # 读取数据并切分
# data = pd.read_csv("data_moons.csv", header=0)  # sklearn.datasets.make_moons 方法可以生成两个交织间隔圆环样式的数据集
# data = pd.read_csv("data_circles.csv", header=0)  # sklearn.datasets.make_circles 方法可以生成大圆环包小圆环样式的数据集

feature = data[['X', 'Y']]  # 指定特征变量
target = data['CLASS']  # 指定分类变量
X_train, X_test, y_train, y_test = train_test_split(feature, target, test_size=.3)  # 切分数据集
##################################################################
## 准备好数据之后, 就可以开始模型训练和测试了
# 迭代模型
for name, clf in zip(classifier_Names, model):
    clf.fit(X_train, y_train)  # 训练模型
    pre_labels = clf.predict(X_test)  # 模型预测
    score = accuracy_score(y_test, pre_labels)  # 计算预测准确度
    print('%s:%.2f' % (name, score))  # 输出模型准确度
##################################################################
## 总结:
# 这 16 个分类器最终的准确度均在 80% ~ 90% 之间, 差距不是很大;
# 主要有两个原因; 首先, 本次使用的是一个非常规范整洁的线性分类数据集; 其次, 所有的分类器均采用了默认参数
##################################################################
## 接下来, 我们通过可视化的方法将每一个模型在分类时的决策边界展示出来, 这样能更加直观的感受到机器学习模型在执行分类预测时发生的变化
# 绘制数据集
i = 1  # 为绘制子图设置的初始编号参数
cm = plt.cm.Reds  # 为绘制热力图选择的样式
cm_color = ListedColormap(['red', 'yellow'])  # 为绘制训练集和测试集选择的样式

# 栅格化
x_min, x_max = data['X'].min() - .5, data['X'].max() + .5
y_min, y_max = data['Y'].min() - .5, data['Y'].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, .1),
                     np.arange(y_min, y_max, .1))

# 模型迭代
for name, clf in zip(classifier_Names, model):
    ax = plt.subplot(4, 4, i)  # 绘制 4x4 子图

    clf.fit(X_train, y_train)  # 模型训练
    pre_labels = clf.predict(X_test)  # 模型测试
    score = accuracy_score(y_test, pre_labels) # 模型准确度

    # 决策边界判断
    if hasattr(clf, "decision_function"):
        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
        print("decision_function: ", clf)
    else:
        Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
        print("predict_proba: ", clf)

    # 绘制决策边界热力图
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, cmap=cm, alpha=.6)

    # 绘制训练集和测试集
    ax.scatter(X_train['X'], X_train['Y'], c=y_train, cmap=cm_color)
    ax.scatter(X_test['X'], X_test['Y'], c=y_test, cmap=cm_color, edgecolors='black')

    # 图形样式设定
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xticks(())
    ax.set_yticks(())
    ax.set_title('%s | %.2f' % (name, score))

    i += 1
plt.show()  # 显示图
# 上面将决策边界绘制出来, 并用热力图显示; 其中, 颜色越深表示偏向于黄色散点分类的概率越高, 而颜色越浅, 则表示偏向红色散点的概率越高
