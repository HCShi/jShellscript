#!/usr/bin/python3
# coding: utf-8
import tensorflow as tf  # 导入好慢啊
import numpy as np
##################################################################
## 准备数据
x_data = np.random.rand(100).astype(np.float32);  # 100 个 [0, 1); uniform 均匀分布
y_data = x_data * 0.1 + 0.3; print(y_data)  # 系数接近 0.1， 常数项接近 0.3
##################################################################
## create tensorflow structure start
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))  # 矩阵大写; 变量要用 Variable; 统一分布 [] 是 shape, -1.0， 1.0
biases = tf.Variable(tf.zeros([1]))  # 权重和常数项 ..., 后面会逐渐学习到 0.1 和 0.3

y = Weights * x_data + biases  # 目标函数式, 逐渐提升准确度

loss = tf.reduce_mean(tf.square(y - y_data))  # 预测值 - 真实值
optimizer = tf.train.GradientDescentOptimizer(0.5)  # 根据上面的误差建立优化器; 0.5 是学习效率
train = optimizer.minimize(loss)  # 用优化器减少误差

# init = tf.initialize_all_variables()  # 固定步骤, 要初始化变量...
# tf.initialize_all_variables() no long valid from 2017-03-02 if using tensorflow >= 0.12
if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
    init = tf.initialize_all_variables()
else:
    init = tf.global_variables_initializer()
## create tensorflow structure end ###
##################################################################
## 准备 Session
sess = tf.Session()  # 定义 Session
sess.run(init)

for step in range(201):  # 训练 201 步
    sess.run(train)  # 开始训练
    if step % 20 == 0:  # 每隔 20 步打印结果
        print(step, sess.run(Weights), sess.run(biases))
##################################################################
## 总结:
# 1. 学习 y = 0.1x + 0.3
# 2. 步骤: 准备数据 -> 目标函数式 -> 误差表达式 -> 优化器优化误差 train -> 初始化变量
#          初始化 Session -> run(init) -> run(train) -> run(variables) -> loop
# 3. Session 相当于 requests 中的会话, 可以保存状态
