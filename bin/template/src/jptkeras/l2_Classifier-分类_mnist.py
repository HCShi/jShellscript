#!/usr/bin/python3
# coding: utf-8
import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
##################################################################
## 一: 数据预处理
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)  # (60000, 28, 28) (60000,) (10000, 28, 28) (10000,)
print(set(y_train))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# 将其 3 维变 2 维 ((60000,28,28) 变 (60000, 784)), 并进行归一化
X_train = X_train.reshape(X_train.shape[0], -1) / 255.   # normalize
X_test = X_test.reshape(X_test.shape[0], -1) / 255.      # normalize
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)
print(X_train[1].shape, y_train[0])  # (784,) [ 0.  0.  0.  0.  0.  1.  0.  0.  0.  0.]
##################################################################
## 二: 建立模型
model = Sequential([
    Dense(32, input_dim=784),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
])
rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
model.compile(optimizer=rmsprop, loss='categorical_crossentropy', metrics=['accuracy'])
##################################################################
## 三: 训练网络
model.fit(X_train, y_train, epochs=2, batch_size=32)
# Epoch 1/2
# 60000/60000 [==============================] - 4s - loss: 0.3606 - acc: 0.8988
# Epoch 2/2
# 60000/60000 [==============================] - 4s - loss: 0.2040 - acc: 0.9413
##################################################################
## 四: 测试模型
# Evaluate the model with the metrics we defined earlier
loss, accuracy = model.evaluate(X_test, y_test)
print('loss: ', loss, 'accuracy: ', accuracy)  # loss:  0.175076550314 accuracy:  0.9485

print(len(model.layers[0].get_weights()))  # 2; W 和 b
print(len(model.layers[0].get_weights()[0]), len(model.layers[0].get_weights()[1]))  # 784, 32; W 对应输入 784 维, b 对应输出 32 维
##################################################################
## 五: 预测
y_pred = model.predict(X_test)
print(y_pred.shape, y_pred[0])  # (10000, 10); 分类问题从来不要求精确输出, 只要有大小关系就行了
# [  5.10046857e-06   5.12467118e-08   3.87858381e-05   7.80041737e-04
#    1.25964021e-08   1.95981374e-06   3.14197601e-09   9.99122083e-01
#    8.86169164e-06   4.31045592e-05]

y_pred_classes = model.predict_classes(X_test)
print(y_pred_classes.shape, set(y_pred_classes))  # (10000,) {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(y_pred_classes[0])  # 7; predict_classes() 就是按照 predict() 结果里的最大的那个来定类别的
# 所以 np_utils.to_categorical() 对多分类问题很重要
