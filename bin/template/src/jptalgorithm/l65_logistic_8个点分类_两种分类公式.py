#!/usr/bin/python3
# coding: utf-8
# 周晓飞, 王泉老师 统计机器学习 第一次作业编程
import numpy as np
import matplotlib.pyplot as plt
##################################################################
## 初始化数据; 数据带 label
x1, y1 = np.array([[1, 1], [1, 2], [2, 2], [1, 0]]), np.array([0, 0, 0, 0])  # 第一类数据
x2, y2 = np.array([[4, 5], [5, 6], [6, 7], [6, 6]]), np.array([1, 1, 1, 1])  # 第二类数据
W, b = np.array([0, 0]), 0
x1 = np.pad(x1, ((0, 0), (0, 1)), 'constant', constant_values=1)  # x 添加一层 1
x2 = np.pad(x2, ((0, 0), (0, 1)), 'constant', constant_values=1)  # x 添加一层 1
W = np.hstack((W, b))  # W 和 b 合并
# 整合 (x, 1), (W, b); 第二种方法中用到, 但第一种方法画图的时候也会用到, 所以放这里
x, y = np.vstack((x1, x2)), np.hstack((y1, y2))  # y = [0 0 0 0 1 1 1 1]; 将 x, y 合并
##################################################################
## 第一种方法: 多元 Logistic 模型; 见 周晓飞 老师的 pdf (Chapter+3+Linear+Classifiers) 课后答案
def calc_cost_1(W, x, y, alpha=1):  # 学习速率为 1
    h = 1 / (1 + np.exp(-np.dot(x, W)))
    dlt = np.dot(h, x)
    W = W - alpha * dlt
    return W
def calc_cost_2(W, x, y, alpha=1):  # 学习速率为 1
    dlt = np.dot((1 / (1 + np.exp(np.dot(x, W)))), x)
    W = W + alpha * dlt
    return W
for _ in range(1000):
    W = calc_cost_1(W, x1, y1)
    W = calc_cost_2(W, x2, y2)
x_ = np.arange(10)
y_ = -(W[0] * x_ + W[2]) / W[1]
plt.subplot(1, 2, 1); plt.scatter(x[:, 0], x[:, 1]); plt.plot(x_, y_); plt.xlabel('W = [%.2f, %.2f]; b = %.2f' % (W[0], W[1], W[2]))
##################################################################
## 第二种: 二项 Logistic 模型; loss = sigma[ylog(h(x)) + (1-y)log((1-h(x)))]
W = np.array([0, 0, 0])  # 上面已经修改了 W, x1, y1, 这里重新定义一下 W 即可, 没有用到 x1, y1
def calc_cost(W, x, y, alpha=1):  # 学习速率为 1
    h = 1 / (1 + np.exp(-np.dot(x, W)))
    # print(x.shape, y.shape, h.shape)  # (8, 3) (8,) (8,); 帮助理解
    dlt = y - h
    W = W + alpha * np.dot(dlt, x)  # 见知乎专栏 逻辑回归 (Logistic Regression)(二)
    # W = W + np.dot((y * (1 - h)), x) - np.dot((h * (1-y)), x)  # 晶晶姑娘那种没有化简求出来的偏导, 结果和上面一毛一样
    # (8, 3)(8,)(8,) 三个怎么样拼出来 (3,) -> 答案是先让 (8,)(8,) 两个向量叉乘, 结果还是 (8,)...
    return W
for _ in range(1000):
    W = calc_cost(W, x, y)
x_ = np.arange(10)
y_ = -(W[0] * x_ + W[2]) / W[1]
plt.subplot(1, 2, 2); plt.scatter(x[:, 0], x[:, 1]); plt.plot(x_, y_); plt.xlabel('W = [%.2f, %.2f]; b = %.2f' % (W[0], W[1], W[2]))
plt.savefig('tmp.jpg')
plt.show()
##################################################################
## 总结:
# 1. 李航书上用的是类似于交叉熵的极大似然估计, 比较直观, 求导过程也比较流畅
# 2. 周晓飞老师上课的方法是 softmax 的推到过程, 使用了多分类简化为二分类的方法, 求导比较麻烦, 要分两次
# 3. 这是一次课后作业, 具体推导过程见提交的作业文档, 或见知乎专栏讲解
