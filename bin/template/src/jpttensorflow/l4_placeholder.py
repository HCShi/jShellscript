#!/usr/bin/python3

# coding: utf-8
import tensorflow as tf
##################################################################
## 准备数据
input1 = tf.placeholder(tf.float32)  # 先占着地方, 后面填入数据
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1: [7.], input2: [2.]}))  # 使用 feed_dict 来传入数据
##################################################################
## 总结:
# 1. placeholder 和 feed_dict 是绑定的
