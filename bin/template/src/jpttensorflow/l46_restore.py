#!/usr/bin/python3
# coding: utf-8
import tensorflow as tf
import numpy as np
##################################################################
## restore variables; redefine the same shape and same type for your variables
W = tf.Variable(np.arange(6).reshape((2, 3)), dtype=tf.float32, name="weights")
b = tf.Variable(np.arange(3).reshape((1, 3)), dtype=tf.float32, name="biases")
# not need init step
saver = tf.train.Saver()  # 用 saver 从路径中将 save_net.ckpt 保存的 W 和 b restore 进来
sess = tf.Session()
with tf.Session() as sess:
    saver.restore(sess, "tmp.ckpt")
    print("weights:", sess.run(W))
    print("biases:", sess.run(b))
##################################################################
## 总结:
# 1. 必须定义和存储中一样的结构
# 2. 没有运行 sess.run(init), 就直接将值赋进去了
