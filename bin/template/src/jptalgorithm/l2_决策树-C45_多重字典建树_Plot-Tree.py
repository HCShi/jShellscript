#!/usr/bin/python3
# coding: utf-8
# 参考: [github AliceDudu](https://github.com/AliceDudu/Learning-Notes/blob/master/Machine-Learning-Algorithms/DecisionTrees/self-learning-c45algorithm-final.ipynb)
from math import log
import operator
import treePlotter
import matplotlib.pyplot as plt
def createDataSet():
    dataSet = [[0, 0, 0, 0, 'N'],
               [0, 0, 0, 1, 'N'],
               [1, 0, 0, 0, 'Y'],
               [2, 1, 0, 0, 'Y'],
               [2, 2, 1, 0, 'Y'],
               [2, 2, 1, 1, 'N'],
               [1, 2, 1, 1, 'Y']]
    labels = ['outlook', 'temperature', 'humidity', 'windy']  # 四个特征 'outlook', 'temperature', 'humidity', 'windy'
    # outlook->  0: sunny | 1: overcast | 2: rain  # temperature-> 0: hot | 1: mild | 2: cool
    # humidity-> 0: high | 1: normal               # windy-> 0: false | 1: true
    return dataSet, labels
def calcShannonEnt(dataSet):
    # 输入: 数据集; 输出: 数据集的香农熵
    # 描述: 计算给定数据集的香农熵; 熵越大, 数据集的混乱程度越大
    numEntries, labelCounts = len(dataSet), {}
    for featVec in dataSet:
        currentLabel = featVec[-1]  # 取最后一列: 标签列
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1      # 数每一类各多少个,  {'Y': 4, 'N': 3}
    shannonEnt = 0.0  # 香农熵
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)  # H(X) = -sigma(p_i * log(p_i))
    return shannonEnt
def majorityCnt(classList):
    # 输入: 分类类别列表; 输出: 子节点的分类
    # 描述: 数据集已经处理了所有属性, 但是类标签依然不是唯一的, 采用多数判决的方法决定该子节点的分类
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1  # 就是去出现次数最多的那个
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reversed=True)
    return sortedClassCount[0][0]
def splitDataSet(dataSet, axis, value):
    # 输入: 数据集, 选择维度, 选择值; 输出: 划分数据集
    # 描述: 按照给定特征划分数据集; 去除选择维度中等于选择值的项
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:          # 只看当第 i 列的值 =value 时的 item
            reduceFeatVec = featVec[:axis]  # featVec 的第 i 列给除去
            reduceFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reduceFeatVec)
    return retDataSet
def chooseBestFeatureToSplit(dataSet):  # 选择最大的 gain ratio 对应的 feature; 信息增益率, 来选择节点的构成方式
    # 输入: 数据集; 输出: 最好的划分维度
    # 描述: 选择最好的数据集划分维度
    numFeatures = len(dataSet[0]) - 1      # feature 个数
    baseEntropy = calcShannonEnt(dataSet)  # 整个 dataset 的熵
    bestInfoGainRatio, bestFeature = 0.0, -1  # Gain(S, A) = Ent(S) - sigma{|S_v|/|S| * Ent(S_v)}
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]  # 每个 feature 的 list
        uniqueVals = set(featList)                      # 每个 list 的唯一值集合
        newEntropy, splitInfo  = 0.0, 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)  # 每个唯一值对应的剩余 feature 的组成子集
            prob = len(subDataSet) / float(len(dataSet))  # |S_v|/|S|
            newEntropy += prob * calcShannonEnt(subDataSet)  # sigma{|S_v|/|S| * Ent(S_v)}
            splitInfo += -prob * log(prob, 2)  # SplitInfo(p, test) = -sigma{p * log(p)}
        infoGain = baseEntropy - newEntropy  # Gain(S, A) = Ent(S) - sigma{|S_v|/|S| * Ent(S_v)}
        if (splitInfo == 0): continue  # fix the overflow bug
        infoGainRatio = infoGain / splitInfo             # 这个 feature 的 infoGainRatio; C4.5 对 ID3 的优化
        if (infoGainRatio > bestInfoGainRatio):          # 选择最大的 gain ratio
            bestInfoGainRatio = infoGainRatio
            bestFeature = i                              # 选择最大的 gain ratio 对应的 feature
    return bestFeature
def createTree(dataSet, labels):  # 多重字典构建树
    # 输入: 数据集, 特征标签; 输出: 决策树
    # 描述: 递归构建决策树, 利用上述的函数
    classList = [example[-1] for example in dataSet]         # 提取类别; ['N', 'N', 'Y', 'Y', 'Y', 'N', 'Y']
    if classList.count(classList[0]) == len(classList): return classList[0]  # classList 所有元素都相等, 即类别完全相同, 停止划分; splitDataSet(dataSet, 0, 0) 此时全是 N, 返回 N
    if len(dataSet[0]) == 1: return majorityCnt(classList)   # [0, 0, 0, 0, 'N']; 遍历完所有特征时返回出现次数最多的
    bestFeat = chooseBestFeatureToSplit(dataSet)             # 0 -> 2; 选择最大的 gain ratio 对应的 feature
    bestFeatLabel = labels[bestFeat]                         # outlook -> windy
    myTree = {bestFeatLabel:{}}                              # 多重字典构建树 {'outlook': {0: 'N'
    del(labels[bestFeat])                                    # ['temperature', 'humidity', 'windy'] -> ['temperature', 'humidity']
    featValues = [example[bestFeat] for example in dataSet]  # [0, 0, 1, 2, 2, 2, 1]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]                                # ['temperature', 'humidity', 'windy']
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)  # 划分数据, 为下一层计算准备
    return myTree
##################################################################
## 下面是测试
dataSet, labels = createDataSet(); labels_tmp = labels[:]
desicionTree = createTree(dataSet, labels_tmp)  # 因为建树的过程中会 del(labels[key]), 所以用了一个临时量
treePlotter.createPlot(desicionTree)  # 画出决策树
def classify(inputTree, featLabels, testVec):  # 对新数据进行分类 # 输入 -> 决策树, 分类标签, 测试数据; 输出 -> 决策结果; 描述 -> 跑决策树
    firstStr = list(inputTree.keys())[0]  # ['outlook'], outlook
    secondDict = inputTree[firstStr]  # {0: 'N', 1: 'Y', 2: {'windy': {0: 'Y', 1: 'N'}}}
    featIndex = featLabels.index(firstStr)  # outlook 所在的列序号 0
    for key in secondDict.keys():  # secondDict.keys() = [0, 1, 2]
        if testVec[featIndex] == key:  # secondDict[key] = N; test 向量的当前 feature 是哪个值, 就走哪个树杈
            if type(secondDict[key]).__name__ == 'dict': classLabel = classify(secondDict[key], featLabels, testVec)  # 如果 secondDict[key] 仍然是字典, 则继续向下层走
            else: classLabel = secondDict[key]  # secondDict[key] 已经只是分类标签了, 则返回这个类别标签
    return classLabel
print(classify(desicionTree, labels, [0, 1, 0, 0]))  # N
##################################################################
## 多个样例测试
def classifyAll(inputTree, featLabels, testDataSet): # 输入 -> 决策树, 分类标签, 测试数据集; 输出 -> 决策结果; 描述 -> 跑决策树
    classLabelAll = []
    for testVec in testDataSet: classLabelAll.append(classify(inputTree, featLabels, testVec))  # 逐个 item 进行分类判断
    return classLabelAll
print('classifyResult:\n', classifyAll(desicionTree, labels, [[0, 1, 0, 0], [2, 1, 0, 1]]))  # ('classifyResult:\n', ['N', 'N'])
