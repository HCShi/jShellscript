#!/usr/bin/python3
# coding: utf-8
##################################################################
## 全连接层实现类
# 1. 代码中的 式 2, 式 8 看 (三)
# 2. 这个类一举取代了原先的 Layer、Node、Connection 等类, 不但代码更加容易理解, 而且运行速度也快了几百倍
class FullConnectedLayer(object):
    def __init__(self, input_size, output_size, activator):
        # input_size: 本层输入向量的维度
        # output_size: 本层输出向量的维度
        # activator: 激活函数
        self.input_size = input_size
        self.output_size = output_size
        self.activator = activator
        self.W = np.random.uniform(-0.1, 0.1, (output_size, input_size))  # 权重数组 W
        self.b = np.zeros((output_size, 1))  # 偏置项 b
        self.output = np.zeros((output_size, 1))  # 输出向量
    def forward(self, input_array):  # 前向计算; 式 2
        # input_array: 输入向量, 维度必须等于 input_size
        self.input = input_array
        self.output = self.activator.forward(np.dot(self.W, input_array) + self.b)
    def backward(self, delta_array):  # 反向计算 W 和 b 的梯度; 式 8
        # delta_array: 从上一层传递过来的误差项
        self.delta = self.activator.backward(self.input) * np.dot(self.W.T, delta_array)
        self.W_grad = np.dot(delta_array, self.input.T)  # 式 9
        self.b_grad = delta_array  # 式 10
    def update(self, learning_rate):  # 使用梯度下降算法更新权重
        self.W += learning_rate * self.W_grad
        self.b += learning_rate * self.b_grad
##################################################################
## Sigmoid 激活函数类
class SigmoidActivator(object):
    def forward(self, weighted_input): return 1.0 / (1.0 + np.exp(-weighted_input))  # f(x) = 1 / (1 + e ^ (1 - x)); 函数表达式
    def backward(self, output): return output * (1 - output)  # 求导公式 y = sigmoid(x); y\' = y(1 - y);
##################################################################
## 神经网络类
class Network(object):
    def __init__(self, layers):
        self.layers = []
        for i in range(len(layers) - 1):
            self.layers.append(FullConnectedLayer(layers[i], layers[i+1], SigmoidActivator()))
    def predict(self, sample):  # 使用神经网络实现预测
        # sample: 输入样本
        output = sample
        for layer in self.layers:
            layer.forward(output)
            output = layer.output
        return output
    def train(self, labels, data_set, rate, epoch):  # 训练函数
        # labels: 样本标签
        # data_set: 输入样本
        # rate: 学习速率
        # epoch: 训练轮数
        for i in range(epoch):
            for d in range(len(data_set)):
                self.train_one_sample(labels[d], data_set[d], rate)
    def train_one_sample(self, label, sample, rate):
        self.predict(sample)
        self.calc_gradient(label)
        self.update_weight(rate)
    def calc_gradient(self, label):
        delta = self.layers[-1].activator.backward(self.layers[-1].output) * (label - self.layers[-1].output)
        for layer in self.layers[::-1]:
            layer.backward(delta)
            delta = layer.delta
        return delta
    def update_weight(self, rate):
        for layer in self.layers:
            layer.update(rate)
