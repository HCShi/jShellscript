#!/usr/bin/python3
# coding: utf-8
import tensorflow as tf
import numpy as np
##################################################################
## 部分代码参考 ./l5_add-layer_build-network_plot-实时可视化.py
def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    # add one more layer and return the output of this layer
    layer_name = 'layer%s' % n_layer
    with tf.name_scope(layer_name):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
            tf.summary.histogram(layer_name + '/weights', Weights)  # 对于想看 直方图的 变量添加 histogram
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='b')
            tf.summary.histogram(layer_name + '/biases', biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.add(tf.matmul(inputs, Weights), biases)
        if activation_function is None: outputs = Wx_plus_b
        else: outputs = activation_function(Wx_plus_b, )
        tf.summary.histogram(layer_name + '/outputs', outputs)
    return outputs
##################################################################
## Make up some real data
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise
##################################################################
## 添加层
with tf.name_scope('inputs'):  # add inputs laye
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')  # define placeholder for inputs to network
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')
l1 = add_layer(xs, 1, 10, n_layer=1, activation_function=tf.nn.relu)  # add hidden layer, 会显示 'layer1'
prediction = add_layer(l1, 10, 1, n_layer=2, activation_function=None)  # add output layer, 会显示 'layer2'
##################################################################
## 使用 name_scope 来确定名字, 会显示在 tensorboard 的界面上
with tf.name_scope('loss'):  # the error between prediciton and real data, 会显示 'loss'
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
    tf.summary.scalar('loss', loss)
with tf.name_scope('train'):  # 会显示 'train'
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
##################################################################
## 使用 Session
sess = tf.Session()
merged = tf.summary.merge_all()  # 将所有的 summary 合并

writer = tf.summary.FileWriter("logs/", sess.graph)  # direct to the local dir and run: $ tensorboard --logdir logs

init = tf.global_variables_initializer()
sess.run(init)

for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:  # 每隔 50 步记录一下
        result = sess.run(merged, feed_dict={xs: x_data, ys: y_data})
        writer.add_summary(result, i)
##################################################################
## 总结:
# 1. 使用 with tf.name_scope('loss'): 来将 对应的层展示在 浏览器的 graph 界面上
# 2. 使用 tf.summary.histogram(layer_name + '/outputs', outputs) 来表示
# 3. tf.summary.scalar('loss', loss) 可以来表示 loss 这种 纯量的变化, 在 event 选项卡中
# 4. summary 有两种不同的记录方式: histogram 和 scalar
# 5. 切换到 logs 同级目录 tensorboard --logdir logs; 然后去浏览器查看
