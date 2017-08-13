#!/usr/bin/python3
# coding: utf-8
import tensorflow as tf
##################################################################
## 准备数据
matrix1 = tf.constant([[3, 3]])  # 一行两列
matrix2 = tf.constant([[2], [2]])  # 两行一列
##################################################################
## 定义操作
product = tf.matmul(matrix1, matrix2)  # matrix multiply np.dot(m1, m2)
##################################################################
## 生成会话
# method 1
sess = tf.Session()
result = sess.run(product)  # 运算的结果会返回
print(result)
sess.close()
# method 2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
