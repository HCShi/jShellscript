#!/usr/bin/python3
# coding: utf-8
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
##################################################################
## 定义添加 layer 代码
def add_layer(inputs, in_size, out_size, activation_function=None):
    # add one more layer and return the output of this layer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs
##################################################################
## Make up some real data
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise
# plot the real data
fig = plt.figure()  # 这里不能直接用 plt.scatter 和 plt.line, 因为 ax 是指针, plt 不行
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion()  # 使 matplotlib 可以刷新
plt.show()  # 这里先看一下大体的形状趋势
##################################################################
## 输入层 1 个神经元, 隐藏层 10 个神经元, 输出层 1 个神经元
# define placeholder for inputs to network, 这里的两个变量相当于 输入层
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])
# add hidden layer
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
# add output layer
prediction = add_layer(l1, 10, 1, activation_function=None)
##################################################################
## 设置 误差表达式, 参考 ./l1_定义简单方程并逐渐学习.py
# the error between prediction and real data
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                     reduction_indices=[1]))  # 设置误差表达式
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)  # 定义优化器
##################################################################
## 构建 Session 和 初始化
# important step
# tf.initialize_all_variables() no long valid from 2017-03-02 if using tensorflow >= 0.12
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(1000):
    # training
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        # to visualize the result and improvement
        try: ax.lines.remove(lines[0])  # 因为第一次可能没有 lines 可能会报错
        except Exception: pass
        # to see the step improvement
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))  # 可以发现误差在逐渐减小

        # plot the prediction
        prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
        plt.pause(1)
