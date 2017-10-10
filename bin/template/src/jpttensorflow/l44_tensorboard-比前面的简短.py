#!/usr/bin/python3
# coding: utf-8
import tensorflow as tf
def add_layer(inputs, in_size, out_size, activation_function=None):
    with tf.name_scope('layer'):  # 区别: 大框架, 定义层 layer, 里面有小部件
        with tf.name_scope('weights'):  # 区别: 小部件
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
        with tf.name_scope('biases'): biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
        with tf.name_scope('Wx_plus_b'): Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)
        if activation_function is None: outputs = Wx_plus_b
        else: outputs = activation_function(Wx_plus_b, )
        return outputs
with tf.name_scope('inputs'):  # 区别: 大框架, 里面有 inputs x, y
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)  # add hidden layer
prediction = add_layer(l1, 10, 1, activation_function=None)  # add output layer
with tf.name_scope('loss'):  # 区别: 定义框架 loss
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
with tf.name_scope('train'):  # 区别: 定义框架 train
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
sess = tf.Session()
writer = tf.summary.FileWriter("logs/", sess.graph)  # direct to the local dir and run: $ tensorboard --logdir logs
# init = tf.global_variables_initializer()
# sess.run(init)
##################################################################
## 总结
# 1. 用 with tf.name_scope 定义各个框架
# 2. 和不用 tensorboard 的区别用 '区别:' 标出来了
# 3. sess.graph 把所有框架加载到一个文件中放到文件夹 "logs/" 里
#    接着打开 terminal, 进入你存放的文件夹地址上一层, 运行命令 tensorboard --logdir='logs/', 会返回一个地址, 然后用浏览器打开这个地址, 在 graph 标签栏下打开
