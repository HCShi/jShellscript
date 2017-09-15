#!/usr/bin/python3
# coding: utf-8
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

a = tf.constant(10)
b = tf.constant(5)
print(sess.run(a + b))
