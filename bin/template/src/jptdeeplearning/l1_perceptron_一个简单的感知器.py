#!/usr/bin/python3
# coding: utf-8
from functools import reduce
import logging
# logging.basicConfig(level=logging.DEBUG)  # debug, info, warning, error 几个级别; 会影响大后面 import /l1_perceptron_一个简单的感知器.py 的文件, 所以最好注释掉
##################################################################
## 定义感知器类
class Perceptron(object):
    def __init__(self, input_num, activator):  # 初始化感知器, 设置输入参数的个数, 以及激活函数. 激活函数的类型为 double -> double
        self.activator = activator
        self.weights = [0.0 for _ in range(input_num)]  # 权重向量初始化为 0
        self.bias = 0.0  # 偏置项初始化为 0
    def __str__(self):  # 打印学习到的权重、偏置项
        return 'weights\t:%s\nbias\t:%f\n' % (self.weights, self.bias)
    def predict(self, input_vec):  # 输入向量, 输出感知器的计算结果
        return self.activator(reduce(lambda a, b: a + b,                 # reduce() 求和
                                     map(lambda x: x[0] * x[1],          # map() 函数计算 [x1*w1, x2*w2, x3*w3]
                                         zip(input_vec, self.weights)),  # zip() 把 input_vec[x1,x2,x3...] 和 weights[w1,w2,w3,...] 打包在一起变成 [(x1,w1),(x2,w2),(x3,w3),...]
                                     0)
                              + self.bias)
    def train(self, input_vecs, labels, iteration, rate):  # 输入训练数据: 一组向量、与每个向量对应的 label; 以及训练轮数、学习率
        logging.debug('Init weights: ' + str(self.weights) + '; Init bias: ' + str(self.bias) + '; Init rate: ' + str(rate))
        logging.debug('delta  = label - output')
        logging.debug('Weight = Weight + rate * delta * x_i  # x 是 w 的偏导值')
        logging.debug('Bias   = Bias   + rate * delta)')
        for i in range(iteration):
            logging.debug('第 ' + str(i) + ' 次 train...')
            self._one_iteration(input_vecs, labels, rate)
    def _one_iteration(self, input_vecs, labels, rate):  # 一次迭代, 把所有的训练数据过一遍
        # 把输入和输出打包在一起, 成为样本的列表 [(input_vec, label), ...]; 而每个训练样本是(input_vec, label)
        samples = list(zip(input_vecs, labels))
        for (input_vec, label) in samples:                        # 对每个样本, 按照感知器规则更新权重
            output = self.predict(input_vec)                      # 计算感知器在当前权重下的输出
            logging.debug('    input_vec: ' + str(input_vec) + '; label: ' + str(label) + '; output: ' + str(output))
            self._update_weights(input_vec, output, label, rate)  # 更新权重
    def _update_weights(self, input_vec, output, label, rate):  # 按照感知器规则更新权重
        # 把 input_vec[x1,x2,x3,...] 和 weights[w1,w2,w3,...] 打包在一起; 变成 [(x1,w1),(x2,w2),(x3,w3),...]; 然后利用感知器规则更新权重
        delta = label - output
        self.weights = list(map(lambda x: x[1] + rate * delta * x[0], zip(input_vec, self.weights)))  # 这很坑, python3 中要加 list() 强制换型一下
        self.bias += rate * delta  # 更新bias
        logging.debug('        delta: ' + str(delta) + '; weights: ' + str(self.weights) + '; bias: ' + str(self.bias))
##################################################################
## 接下来, 我们利用这个感知器类去实现 and 函数.
# f = lambda x: x  # 这样的激活函数就是线性单元
def f(x): return 1 if x > 0 else 0  # 定义激活函数 f
def get_training_dataset():                    # 基于 and 真值表构建训练数据
    input_vecs = [[1,1], [0,0], [1,0], [0,1]]  # 构建训练数据: 输入向量列表
    labels = [1, 0, 0, 0]                      # 期望的输出列表, 注意要与输入一一对应; [1,1] -> 1, [0,0] -> 0, [1,0] -> 0, [0,1] -> 0
    return input_vecs, labels
def train_and_perceptron():
    # 使用 and 真值表训练感知器
    p = Perceptron(2, f)                  # 创建感知器, 输入参数个数为 2 (因为and是二元函数), 激活函数为f
    input_vecs, labels = get_training_dataset()
    p.train(input_vecs, labels, 10, 0.1)  # 训练, 迭代 10 轮, 学习速率为 0.1
    return p                              # 返回训练好的感知器
if __name__ == '__main__':
    and_perception = train_and_perceptron()  # 训练 and 感知器
    print(and_perception)  # 打印训练获得的权重
    # 测试
    print('1 and 1 = %d' % and_perception.predict([1, 1]))
    print('0 and 0 = %d' % and_perception.predict([0, 0]))
    print('1 and 0 = %d' % and_perception.predict([1, 0]))
    print('0 and 1 = %d' % and_perception.predict([0, 1]))
##################################################################
## 总结:
# 1. delta = label - output;
#    delta 为 + 时, bias 会增加 rate * delta, 在这里是 0.1
#                   weights 会逐项增加 rate * delta * x_i
#                   weights 会根据 delta 和 x_i 的值变化
#    delta 为 0 时, bias 和 weights 不发生变化
# 2. x_i 是常亮, weights 和 bias 是变量, 对变量求偏导就是 x_i
# 3. 运行代码, 发现第 5 次训练后就没有什么变化了
# 4. 激励函数是 越阶函数 def f(x): return 1 if x > 0 else 0
# 5. 将 labels = [2, 0, 0, 0];
#       f(x): return 2 if x > 0 else 0; 能得到同样的效果
#
#       labels = [2, 0, 0, 0];
#       f(x): return 1 if x > 0 else 0; 会永远训练不好
#    说明 激励函数 对结果的影响很大
# 6. 单个感知器只能实现 and or 这种简单的分类问题, 不能解决分类问题
# 7. 感知器规则 (因为是跃阶函数, 对应的只能是 and/or 这种简单的模型, 所以规则比较简单):
#        delta = label - output
#        w_i = w_i + rate * delta * x_i
#        b_i = b_i + rate * delta
# 8. 感知器有一个问题, 当面对的数据集不是线性可分的时候, 『感知器规则』可能无法收敛, 这意味着我们永远也无法完成一个感知器的训练.
#    为了解决这个问题, 我们使用一个可导的线性函数来替代感知器的阶跃函数, 这种感知器就叫做线性单元.
#    线性单元在面对线性不可分的数据集时, 会收敛到一个最佳的近似上.

#                                      predict() 调用预测值与 lable 比较
#                                         ^
#                                         |
# 9. Perceptron 类中是按照 train -> _one_iteration_ -> _update_weights 调用顺序来训练的
