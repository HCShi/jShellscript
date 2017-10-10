#!/usr/bin/python3
# coding: utf-8
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
##################################################################
## 0. 准备数据
mnist = input_data.read_data_sets("/tmp/data", one_hot=True)
##################################################################
## 1. 定义模型
# 占位符, 后期传数据
x = tf.placeholder(tf.float32, [None, 784])  # [None, 784] 二维的 tensor 来表示 mnist.train.images, 其中 None 表示可以为任意值
# paras
W = tf.Variable(tf.zeros([784, 10]))  # 784*10, 要将一个 784 维的像素值经过相应的权值之乘转化为 10 个类别上
b = tf.Variable(tf.zeros([10]))  # 十个类别上累加的偏置值
# softmax regression 模型
y = tf.nn.softmax(tf.matmul(x, W) + b)  # 实现 softmax regression 模型仅需要一行代码
##################################################################
## 2. 模型训练 / 损失函数 / 代价函数
y_ = tf.placeholder(tf.float32, [None, 10])  # mnist.train.labels; 需要先设置一个占位符在存放图片的正确 label 值
# loss func; 交叉熵函数作为 损失函数/代价函数
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))  # H(y) = -sigma(y_1 * log(y_i))
# 注意, 以上的交叉熵不是局限于一张图片, 而是整个可用的数据集
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)  # 学习率为 0.01 的梯度下降算法来最小化代价函数
##################################################################
## 3. 初始化
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
##################################################################
## 4. 开始训练
for i in range(100):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
# 理论上, 我们应该在每一次循环过程中, 利用所有的训练数据来得到正确的梯度下降方向, 但这样将非常耗时
# 所以这里我们每一次循环只选择了 100 个数据
##################################################################
## 5. 评估结果
correct_prediction = tf.equal(tf.arg_max(y, 1), tf.arg_max(y_, 1))  # tf.argmax() 得到预测和实际的图片 label 值, tf.equal() 判断预测值和真实值是否一致
# correct_prediction 是一个布尔值的列表, [True, False, True, True]; tf.cast() 函数将其转换为 [1, 0, 1, 1], 以方便准确率的计算
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print("Accuarcy on Test-dataset: ", sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
# 因为 y = tf.nn.softmax(tf.matmul(x, W) + b), 所以也要把 x 传入 accuracy
##################################################################
## 总结:
# 1. 总共两个 placeholder, 对应 xs, ys;
# 2. placeholder 中都用 None 来表示 batch 的大小, 其他位置要考虑输入的维度
# 3. equal, arg_max 等都是 numpy 的函数, 只是在这里实现更加方便一点
