#!/usr/bin/python3
# coding: utf-8
import tensorflow as tf
##################################################################
## 准备数据, 设置变量
state = tf.Variable(0, name='counter')
# print(state.name)
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)  # 定义规则, 将新的值 赋值给 state
##################################################################
## 准备 init 和 Session
# tf.initialize_all_variables() no long valid from
# 2017-03-02 if using tensorflow >= 0.12
if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
    init = tf.initialize_all_variables()
else:
    init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))  # 直接 print(state) 没用, 一定要把 sess 的指针放到 state 上, 并且 run()
##################################################################
## 总结:
# 1. 用了 Variable 以后一定要定义 init, 并且 run(init)
# 2. 输出 state 一定要用 run(state)
