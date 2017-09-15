#!/usr/bin/python3
# coding: utf-8
import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation  # Dense 隐藏层, Activation 激励函数
from keras.optimizers import RMSprop
# download the mnist to the path '~/.keras/datasets/' if it is the first time to be called
# X shape (60,000 28x28), y shape (10,000, )
(X_train, y_train), (X_test, y_test) = mnist.load_data()
##################################################################
## data pre-processing
print(X_train.shape, X_train.shape[0])  # (60000, 28, 28), 60000
X_train = X_train.reshape(X_train.shape[0], -1) / 255.   # normalize, -1 表示维度根据前面的计算
print(X_train.shape)  # (60000, 784)
X_test = X_test.reshape(X_test.shape[0], -1) / 255.      # normalize
y_train = np_utils.to_categorical(y_train, num_classes=10)  # 例如: [1] -> [[0. 1. 0 .... 0]]; 将 n 换为 长度为 10 的二进制数组, 第 n 个位置上为 1
y_test = np_utils.to_categorical(y_test, num_classes=10)
##################################################################
## Another way to build your neural net
model = Sequential([
    Dense(32, input_dim=784),  # 28x28; 传出进行压缩至 32 个 feathers
    Activation('relu'),  # 变成非线性数据, 层与层之间要加激励函数变为非线性
    Dense(10),  # 上一层的 out 为当前层的 input_dim; output_dim 为 10
    Activation('softmax'),  # 用 softmax 进行分类
])
##################################################################
## Another way to define your optimizer
rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)
##################################################################
## We add metrics to get more results you want to see; 激活
model.compile(optimizer=rmsprop,
              loss='categorical_crossentropy',  # 不用 mean_square(经常用于线性回归)
              metrics=['accuracy'])  # 同时计算一下误差

# Another way to train the model
print('Training ------------')
model.fit(X_train, y_train, epochs=2, batch_size=32)  # epochs 训练次数

# Evaluate the model with the metrics we defined earlier
print('\nTesting ------------')
loss, accuracy = model.evaluate(X_test, y_test)

print('test loss: ', loss)
print('test accuracy: ', accuracy)
