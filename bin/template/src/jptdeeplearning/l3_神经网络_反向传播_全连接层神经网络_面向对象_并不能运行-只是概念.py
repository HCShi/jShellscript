#!/usr/bin/python3
# coding: utf-8
# 具体讲解见: 零基础入门深度学习(三)
##################################################################
## 节点类, 负责记录和维护节点自身信息以及与这个节点相关的上下游连接, 实现输出值和误差项的计算
class Node(object):
    def __init__(self, layer_index, node_index):
        self.layer_index = layer_index  # 节点所属的层的编号
        self.node_index = node_index    # 节点的编号
        self.downstream = []            # 存放 Connection 对象
        self.upstream = []
        self.output = 0
        self.delta = 0
    def set_output(self, output):  self.output = output                         # 设置节点的输出值; 如果节点属于输入层会用到这个函数;
    def append_downstream_connection(self, conn): self.downstream.append(conn)  # 添加一个到下游节点的连接
    def append_upstream_connection(self, conn): self.upstream.append(conn)      # 添加一个到上游节点的连接
    def calc_output(self):  # 根据式 1 计算节点的输出 y = sigmoid(w * x)
        output = reduce(lambda ret, conn: ret + conn.upstream_node.output * conn.weight, self.upstream, 0)
        self.output = sigmoid(output)
    def calc_hidden_layer_delta(self):  # 节点属于隐藏层时, 根据式 4 计算 delta_i = a_i * (1 - a_i) * Sigma_k(w_ki * delta_k)
        downstream_delta = reduce(lambda ret, conn: ret + conn.downstream_node.delta * conn.weight, self.downstream, 0.0)
        self.delta = self.output * (1 - self.output) * downstream_delta
    def calc_output_layer_delta(self, label):  # 节点属于输出层时, 根据式 3 计算 delta_i = y_i * (1 - y_i) * (t_i - y_i)
        self.delta = self.output * (1 - self.output) * (label - self.output)
    def __str__(self):  # 打印节点的信息
        node_str = '%u-%u: output: %f delta: %f' % (self.layer_index, self.node_index, self.output, self.delta)
        downstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn), self.downstream, '')
        upstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn), self.upstream, '')
        return node_str + '\n\tdownstream:' + downstream_str + '\n\tupstream:' + upstream_str
##################################################################
## ConstNode 对象, 为了实现一个输出恒为 1 的节点 (计算偏置项时需要, 作为下一层的 x_0)
class ConstNode(object):
    def __init__(self, layer_index, node_index):  # 构造节点对象
        self.layer_index = layer_index            # 节点所属的层的编号
        self.node_index = node_index              # 节点的编号
        self.downstream = []                      # 对 upstream 没有影响, 所以不用管
        self.output = 1
    def append_downstream_connection(self, conn): self.downstream.append(conn)  # 添加一个到下游节点的连接
    def calc_hidden_layer_delta(self):  # 节点属于隐藏层时, 根据式 4 计算 delta_i = a_i * (1 - a_i) * Sigma_k(w_ki * delta_k)
        downstream_delta = reduce(lambda ret, conn: ret + conn.downstream_node.delta * conn.weight, self.downstream, 0.0)
        self.delta = self.output * (1 - self.output) * downstream_delta  # 1 - self.output 恒为 0; 所以这个函数只是为了调用时候的一致性
    def __str__(self):  # 打印节点的信息
        node_str = '%u-%u: output: 1' % (self.layer_index, self.node_index)
        downstream_str = reduce(lambda ret, conn: ret + '\n\t' + str(conn), self.downstream, '')
        return node_str + '\n\tdownstream:' + downstream_str
##################################################################
## Layer 对象, 负责初始化一层; 此外, 作为 Node 的集合对象, 提供对 Node 集合的操作
class Layer(object):
    def __init__(self, layer_index, node_count):  # 初始化一层
        # layer_index: 层编号
        # node_count: 层所包含的节点个数
        self.layer_index = layer_index
        self.nodes = []
        for i in range(node_count):
            self.nodes.append(Node(layer_index, i))
        self.nodes.append(ConstNode(layer_index, node_count))  # 最后添加一个偏置项
    def set_output(self, data):  # 设置层的输出; 当层是输入层时会用到, 赋值初始值
        for i in range(len(data)):
            self.nodes[i].set_output(data[i])
    def calc_output(self):  # 计算层的输出向量, 正向...
        for node in self.nodes[:-1]:  # 最后的偏置项不用管
            node.calc_output()
    def dump(self):  # 打印层的信息
        for node in self.nodes:
            print node
##################################################################
## Connection 对象, 主要职责是记录连接的权重, 以及这个连接所关联的上下游节点
class Connection(object):
    def __init__(self, upstream_node, downstream_node):  # 初始化连接, 权重初始化为是一个很小的随机数
        # upstream_node: 连接的上游节点, 单个, 不是 list
        # downstream_node: 连接的下游节点
        self.upstream_node = upstream_node
        self.downstream_node = downstream_node
        self.weight = random.uniform(-0.1, 0.1)
        self.gradient = 0.0  # 这里记录梯度
    # 下面是 全连接层 的 随机梯度下降公式
    def calc_gradient(self): self.gradient = self.downstream_node.delta * self.upstream_node.output  # 计算梯度
    def get_gradient(self): return self.gradient                                                     # 获取当前的梯度
    def update_weight(self, rate):                                                                   # 根据梯度下降算法更新权重
        self.calc_gradient()
        self.weight += rate * self.gradient
    def __str__(self):  # 打印连接信息
        return '(%u-%u) -> (%u-%u) = %f' % (
            self.upstream_node.layer_index,
            self.upstream_node.node_index,
            self.downstream_node.layer_index,
            self.downstream_node.node_index,
            self.weight)
##################################################################
## Connections 对象, 提供 Connection 集合操作
class Connections(object):
    def __init__(self): self.connections = []
    def add_connection(self, connection): self.connections.append(connection)
    def dump(self):
        for conn in self.connections:
            print conn
##################################################################
## Network 对象, 提供 API
class Network(object):
    def __init__(self, layers):  # 初始化一个全连接神经网络
        # layers: 二维数组, 描述神经网络每层节点数
        self.connections = Connections()
        self.layers = []
        layer_count = len(layers)
        node_count = 0;
        for i in range(layer_count):
            self.layers.append(Layer(i, layers[i]))
        for layer in range(layer_count - 1):
            connections = [Connection(upstream_node, downstream_node)  # 这里进行全连接
                           for upstream_node in self.layers[layer].nodes
                           for downstream_node in self.layers[layer + 1].nodes[:-1]]
            for conn in connections:  # 这里将网络搭建好
                self.connections.add_connection(conn)
                conn.downstream_node.append_upstream_connection(conn)
                conn.upstream_node.append_downstream_connection(conn)
    def train(self, labels, data_set, rate, iteration):  # 训练神经网络
        # labels: 数组, 训练样本标签; 每个元素是一个样本的标签
        # data_set: 二维数组, 训练样本特征; 每个元素是一个样本的特征
        for i in range(iteration):
            for d in range(len(data_set)):
                self.train_one_sample(labels[d], data_set[d], rate)
    def train_one_sample(self, label, sample, rate):  # 内部函数, 用一个样本训练网络
        # 先正向一遍, 再反向误差传播一遍, 最后更新权重
        self.predict(sample)
        self.calc_delta(label)
        self.update_weight(rate)
    def calc_delta(self, label):  # 内部函数, 计算每个节点的 delta
        output_nodes = self.layers[-1].nodes
        for i in range(len(label)):
            output_nodes[i].calc_output_layer_delta(label[i])  # 先计算输出层的
        for layer in self.layers[-2::-1]:                      # beg:end:len;
            for node in layer.nodes:
                node.calc_hidden_layer_delta()                 # 再计算隐藏层的
    def update_weight(self, rate):  # 内部函数, 更新每个连接权重
        for layer in self.layers[:-1]:
            for node in layer.nodes:
                for conn in node.downstream:
                    conn.update_weight(rate)
    def calc_gradient(self):  # 内部函数, 计算每个连接的梯度
        for layer in self.layers[:-1]:
            for node in layer.nodes:
                for conn in node.downstream:
                    conn.calc_gradient()
    def get_gradient(self, label, sample):  # 获得网络在一个样本下, 每个连接上的梯度
        # label: 样本标签
        # sample: 样本输入
        self.predict(sample)
        self.calc_delta(label)
        self.calc_gradient()
    def predict(self, sample):  # 根据输入的样本预测输出值
        # sample: 数组, 样本的特征, 也就是网络的输入向量
        self.layers[0].set_output(sample)
        for i in range(1, len(self.layers)):
            self.layers[i].calc_output()  # 正向计算一次
        return map(lambda node: node.output, self.layers[-1].nodes[:-1])  # 最有还有一个输出恒为 1 的偏置项
    def dump(self):  # 打印网络信息
        for layer in self.layers: layer.dump()
