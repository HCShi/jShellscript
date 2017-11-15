#!/usr/bin/python3
# coding: utf-8
import tensorflow as tf
import numpy as np
##################################################################
## Save to file; remember to define the same dtype and shape when restore
W = tf.Variable([[1, 2, 3], [3, 4, 5]], dtype=tf.float32, name='weights')
b = tf.Variable([[1, 2, 3]], dtype=tf.float32, name='biases')
init = tf.global_variables_initializer()
saver = tf.train.Saver()  # 用 saver 将所有的 variable 保存到定义的路径
with tf.Session() as sess:
   sess.run(init)
   save_path = saver.save(sess, "tmp.ckpt")
   print("Save to path: ", save_path)
##################################################################
## restore()
# Later, launch the model, use the saver to restore variables from disk, and do some work with the model.
with tf.Session() as sess:
   saver.restore(sess, "tmp.ckpt")  # Restore variables from disk.
   print(sess.run(W))
##################################################################
## 总结:
# 1. saver() 会生成很多的文件 checkpoint, tmp.ckpt.*
