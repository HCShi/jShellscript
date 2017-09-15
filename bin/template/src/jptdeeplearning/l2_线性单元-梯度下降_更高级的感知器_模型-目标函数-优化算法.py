#!/usr/bin/python3
# coding: utf-8
import logging
# logging.basicConfig(level=logging.DEBUG)
##################################################################
## 通过继承 Perceptron, 我们仅用几行代码就实现了线性单元
from l1_perceptron_一个简单的感知器 import Perceptron
f = lambda x: x  # 定义激活函数 f
class LinearUnit(Perceptron):
    def __init__(self, input_num):  # 初始化线性单元, 设置输入参数的个数
        Perceptron.__init__(self, input_num, f)
##################################################################
## 用简单的数据进行一下测试
def get_training_dataset():                      # 捏造 5 个人的收入数据
    input_vecs = [[5], [3], [8], [1.4], [10.1]]  # 构建训练数据; 输入向量列表, 每一项是工作年限
    labels = [5500, 2300, 7600, 1800, 11400]     # 期望的输出列表, 月薪, 注意要与输入一一对应
    return input_vecs, labels
def train_linear_unit():                    # 使用数据训练线性单元
    lu = LinearUnit(1)                      # 创建感知器, 输入参数的特征数为 1(工作年限)
    input_vecs, labels = get_training_dataset()
    lu.train(input_vecs, labels, 10, 0.01)  # 训练, 迭代 10 轮, 学习速率为 0.01
    return lu                               # 返回训练好的线性单元
if __name__ == '__main__':
    linear_unit = train_linear_unit()  # 训练线性单元
    print(linear_unit)                 # 打印训练获得的权重
    # 测试
    print('Work 3.4 years, monthly salary = %.2f' % linear_unit.predict([3.4]))
    print('Work 15 years, monthly salary = %.2f' % linear_unit.predict([15]))
    print('Work 1.5 years, monthly salary = %.2f' % linear_unit.predict([1.5]))
    print('Work 6.3 years, monthly salary = %.2f' % linear_unit.predict([6.3]))
##################################################################
## plot
import matplotlib.pyplot as plt
import numpy as np
input_vecs, labels = get_training_dataset()
for i in range(8):  # 8 次 eporch, 就是跑了 8 个循环
    lu = LinearUnit(1)                     # 创建感知器, 输入参数的特征数为 1(工作年限)
    lu.train(input_vecs, labels, i, 0.01)  # 训练, 迭代 10 轮, 学习速率为 0.01
    plt.subplot(4, 2, i+1)
    plt.title('figure ' + str(i+1))
    plt.scatter(input_vecs, labels)
    x = np.arange(1, 10)
    y = lu.weights[0] * x + lu.bias
    plt.plot(x, y)
plt.figure()  # 另一个窗口
for i in range(5):  # 1 次 eporch, 不断变化 input_vecs 的大小
    lu = LinearUnit(1)                         # 创建感知器, 输入参数的特征数为 1(工作年限)
    lu.train(input_vecs[:i], labels, i, 0.01)  # 训练, 迭代 10 轮, 学习速率为 0.01
    plt.subplot(3, 2, i+1)
    plt.title('figure ' + str(i+1))
    plt.scatter(input_vecs, labels)
    x = np.arange(1, 10)
    y = lu.weights[0] * x + lu.bias
    plt.plot(x, y)
plt.show()
##################################################################
## 总结:
# 1. 除了激活函数 f() 外, 感知器 和 线性单元 的模型和训练规则都一样, 参见: 零基础入门深度学习(2): 线性单元和梯度下降
# 2. 可以从 plot 中看到, 第一个 eporch 后就已经好了, 后面的变化不大
#                        在第一个 eporch 中, bias 的影响很小...
# 3. 事实上, 一个机器学习算法其实只有两部分
#        模型:     从输入特征预测输入的那个函数 y=f(wx)
#        目标函数: E(w), 目标函数取最小(最大)值时所对应的参数值, 就是模型的参数的最优值. 很多时候我们只能获得目标函数的局部最小(最大)值, 因此也只能得到模型参数的局部最优值.
#        因此, 如果你想最简洁的介绍一个算法, 列出这两个函数就行了
#    接下来, 你会用优化算法去求取目标函数的最小(最大)值.
#        [随机]梯度{下降|上升}算法就是一个优化算法. 针对同一个目标函数, 不同的优化算法会推导出不同的训练规则. 我们后面还会讲其它的优化算法.
