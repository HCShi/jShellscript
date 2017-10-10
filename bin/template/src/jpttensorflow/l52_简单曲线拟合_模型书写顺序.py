#!/usr/bin/python3
# coding: utf-8
import tensorflow as tf
import numpy as np
##################################################################
## 0. 准备数据; 模拟生成 100 对数据对, 对应的函数为 y = x * 0.1 + 0.3
x_data = np.random.rand(100).astype("float32"); print(x_data.shape)  # (100,); 100 个 [0, 1) 的数据组成的向量
y_data = x_data * 0.1 + 0.3; print(y_data.shape)  # (100,)
##################################################################
## 1. 定义模型; 指定 w 和 b 变量的取值范围 (注意我们要利用 TensorFlow 来得到 w 和 b 的值)
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b
##################################################################
## 2. 模型训练; 最小化均方误差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
##################################################################
## 3. 初始化
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)  # 运行数据流图 (注意在这一步才开始执行计算过程)
##################################################################
## 4. 开始训练; 观察多次迭代计算时, w 和 b 的拟合值
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))
# 最好的情况是 w 和 b 分别接近甚至等于 0.1 和 0.3
##################################################################
## 总结:
# 1. 查看节点 sess.run(W)
