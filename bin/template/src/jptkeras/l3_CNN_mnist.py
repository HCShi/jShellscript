#!/usr/bin/python3
# coding: utf-8
import numpy as np
np.random.seed(1337)
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Convolution2D, MaxPooling2D, Flatten
from keras.optimizers import Adam
##################################################################
## 一: 数据预处理
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train.shape, y_train.shape)  # (60000, 28, 28) (60000,)
X_train = X_train.reshape(-1, 1, 28, 28) / 255.; X_test = X_test.reshape(-1, 1, 28, 28) / 255.
y_train = np_utils.to_categorical(y_train, num_classes=10); y_test = np_utils.to_categorical(y_test, num_classes=10)
print(X_train.shape, y_train.shape)  # (60000, 1, 28, 28) (60000, 10)
print(X_test.shape, y_test.shape)  # (10000, 1, 28, 28) (10000, 10)
##################################################################
## 二: 建立模型
model = Sequential()
## 第一层卷基层 池化层
model.add(Convolution2D(
    input_shape=(1, 28, 28),  # (batch, channels, height, width); 对应下面的 channels_first
    filters=32,      # 卷积核的数目, 32个 输出(也就是卷积通道); Integer, the dimensionality of the output space
    kernel_size=5,   # 卷积核的尺寸, 卷积核的窗口选用 5*5 像素窗口; width and height of the 2D convolution window.
    strides=1,       # 卷积核移动的步长, 分为行方向和列方向; the strides of the convolution along the width and height
    padding='same',  # 边界模式; Padding method; one of "valid" or "same"
    data_format='channels_first',  # 默认是 channels_last
))
model.add(Activation('relu'))
model.add(MaxPooling2D(  # pooling(池化, 下采样), 分辨率长宽各降低一半, 输出数据 shape 为 (32, 14, 14)
    pool_size=2,     # 池化核尺寸
    strides=2,       # 池化核移动步长
    padding='same',  # 边界模式; Padding method
    data_format='channels_first',
))
## 第二层卷积和第二层 pooling
model.add(Convolution2D(64, 5, strides=1, padding='same', data_format='channels_first', activation='relu'))  # Conv layer 2 output shape (64, 14, 14)
model.add(MaxPooling2D(2, 2, 'same', data_format='channels_first'))  # Pooling layer 2 (max pooling) output shape (64, 7, 7)
## 第三层全连接层, 经过以上处理之后数据 shape 为(64, 7, 7), 需要将数据抹平成一维, 再添加全连接层 1
model.add(Dropout(0.25))  # 防止过拟合
model.add(Flatten())  # 展平所有像素, 比如 [28*28] -> [784]
model.add(Dense(1024, activation='relu'));
model.add(Dropout(0.5))  # 防止过拟合
## 第四层全连接层, 添加全连接层 2(即输出层)
model.add(Dense(10, activation='softmax'))  # 0-9 手写数字一个有 10 个类别
model.compile(optimizer='adadelta', loss='categorical_crossentropy', metrics=['accuracy'])
##################################################################
## 模型训练
model.fit(X_train[:5000], y_train[:5000], epochs=1, batch_size=64, validation_data=(X_test, y_test))  # acc 涨得好快
# Epoch 1/1
# 5000/5000 [==============================] - 72s - loss: 0.8619 - acc: 0.7272 - val_loss: 0.2550 - val_acc: 0.9200
##################################################################
## 评估模型
loss, accuracy = model.evaluate(X_test, Y_test, verbose=0)
print('Test score:', loss)
print('Test accuracy:', accuracy)
