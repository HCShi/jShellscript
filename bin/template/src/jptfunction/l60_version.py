#!/usr/bin/python3
# coding: utf-8
import tensorflow as tf
print(tf.__version__)
# 小于 0.12 的
if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
    init = tf.initialize_all_variables()
    print("低版本")
else:
    init = tf.global_variables_initializer()
    print("高版本")
