#!/usr/bin/python3
# coding: utf-8
import tensorflow as tf
import numpy as np
##################################################################
## 训练的数据
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise
##################################################################
## 定义节点准备接收数据
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])
##################################################################
## 定义神经层: 隐藏层和预测层
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    # 隐含节点 dropout 率等于 0.5 的时候效果最好，即 keep_prob=0.5，原因是 0.5 的时候 dropout 随机生成的网络结构最多
    Wx_plus_b = tf.nn.dropout(Wx_plus_b, keep_prob=0.5)  # keep_prob 就是保持多少不被 drop, 在迭代时在 sess.run 中被 feed
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)  # add hidden layer 输入值是 xs, 在隐藏层有 10 个神经元
prediction = add_layer(l1, 10, 1, activation_function=None)  # add output layer 输入值是隐藏层 l1, 在预测层输出 1 个结果
##################################################################
## 定义 loss 表达式
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
##################################################################
## 选择 optimizer 使 loss 达到最小, 学习率是 0.1
optimizer = tf.train.GradientDescentOptimizer(0.1)
train_step = optimizer.minimize(loss)
##################################################################
## 对所有变量进行初始化
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)  # 上面定义的都没有运算, 直到 sess.run 才会开始运算
##################################################################
## 迭代 1000 次学习, training train_step 和 loss 都是由 placeholder 定义的运算, 所以这里要用 feed 传入参数
for i in range(10):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
