#!/usr/bin/python3
# coding: utf-8
# 这里以 mnist 分类来为例, 会穿插回归问题各个部分的讲解, 这样在其他部分就不用每次都注释了
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential  # Sequential 可以封装各种神经网络层, 包括 Dense 全连接层, Dropout 层, Cov2D 卷积层
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
##################################################################
## 数据预处理
(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)  # (60000, 28, 28) (60000,) (10000, 28, 28) (10000,)
print(set(y_train))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

## 全连接层, 将其 3 维变 2 维 ((60000, 28, 28) 变 (60000, 784)), 并进行归一化
X_train = X_train.reshape(X_train.shape[0], -1) / 255.; X_test = X_test.reshape(X_test.shape[0], -1) / 255.
y_train = np_utils.to_categorical(y_train, num_classes=10); y_test = np_utils.to_categorical(y_test, num_classes=10)
print(X_train[1].shape, y_train[0])  # (784,) [ 0.  0.  0.  0.  0.  1.  0.  0.  0.  0.]
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)  # (60000, 784) (600000, 10) (10000, 784) (100000, 10)

## CNN, 要变为 (60000, 1, 28, 28)
X_train = X_train.reshape(-1, 1, 28, 28) / 255.; X_test = X_test.reshape(-1, 1, 28, 28) / 255.
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)  # (60000, 1, 28, 28) (60000, 10) (10000, 1, 28, 28) (10000, 10)
##################################################################
## Sequential()
### 全连接层 FC, (60000, 784) (600000, 10)
## 第一种方式
model = Sequential()
# 第一层必须有两个参数, 输出维度和输入维度; 第二层可以只有一个输出维度, 因为输入是上一层的输出
# keras.layers.core.Dense(units, activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros')
# units: 输出单元的数量, 即全连接层神经元的数量, 作为第一层的 Dense 层必须指定 input_shape
model.add(Dense(32, input_dim=784));
# keras.layers.core.Activation(activation) 预定义激活函数: softmax, softplus, softsign, relu, tanh, sigmoid, hard_sigmoid, linear 等
model.add(Activation('relu'))  # 官网文档说 Activation() 和 activation='' 是等价的
model.add(Dense(10, activation='softmax'))
## 第二种方式, 有点类似于 sklearn 中的 Pipeline, 不喜欢这种定义方式, 因为我还没写好 send-region-to-repl
model = Sequential([
    Dense(32, input_dim=784),  # 对应上面的 (784,); 28x28 传出进行压缩至 32 个 feathers
    Activation('relu'),        # 变成非线性数据, 层与层之间要加激励函数变为非线性
    Dense(10),                 # 对应上面的 {0, 1, ..., 9}, 10 个分类; 上一层的 out 为当前层的 input_dim; output_dim 为 10
    Activation('softmax'),     # 多分类用 softmax
])

### CNN, (60000, 1, 28, 28) (60000, 10)
model = Sequential()
## 第一层卷基层 池化层
# keras.layers.convolutional.Conv2D(filters, kernel_size, strides=(1,1), padding='valid', data_format=None, dilation_rate=(1,1), activation=None)
# 二维卷积层对二维输入进行滑动窗卷积, 当使用该层作为第一层时, 应提供 input_shape 参数
model.add(Convolution2D(
    input_shape=(1, 28, 28),  # (channels, height, width); 对应下面的 channels_first
    filters=32,      # 卷积核的数目, 32个 输出(也就是卷积通道); Integer, the dimensionality of the output space
    kernel_size=5,   # 卷积核的尺寸, 卷积核的窗口选用 5*5 像素窗口; width and height of the 2D convolution window.
    strides=1,       # 卷积核移动的步长, 分为行方向和列方向; the strides of the convolution along the width and height
    padding='same',  # 边界模式; Padding method; one of "valid" or "same"
    data_format='channels_first',  # 默认是 channels_last
    # 以 128x128 的 RGB 图像为例, "channels_first" 应将数据组织为 (3, 128, 128), 而 "channels_last" 应将数据组织为 (128, 128, 3)
))
model.add(Activation('relu'))
# keras.layers.pooling.MaxPooling2D(pool_size=(2,2), strides=None, padding='valid', data_format=None) 对空域信号进行最大值池化
model.add(MaxPooling2D(  # pooling(池化, 下采样), 分辨率长宽各降低一半, 输出数据 shape 为 (32, 14, 14)
    pool_size=2,     # 池化核尺寸
    strides=2,       # 池化核移动步长
    padding='same',  # 边界模式; Padding method
    data_format='channels_first',
))
## 第二层卷积和第二层 pooling
model.add(Convolution2D(64, 5, strides=1, padding='same', data_format='channels_first', activation='relu'))  # Conv layer 2 output shape (64, 14, 14)
model.add(MaxPooling2D(2, 2, 'same', data_format='channels_first'))  # Pooling layer 2 (max pooling) output shape (64, 7, 7)
# keras.layers.core.Dropout(p): 将在训练过程中每次更新参数时随机断开一定百分比 p 的输入神经元连接, Dropout 层用于防止过拟合.
model.add(Dropout(0.25))  # 防止过拟合
## 第三层全连接层, 经过以上处理之后数据 shape 为(64, 7, 7), 需要将数据抹平成一维, 再添加全连接层 1
# keras.layers.core.Flatten(): 层用来将输入"压平", 即把多维的输入一维化, 常用在从卷积层到全连接层的过渡. Flatten 不影响 batch 的大小.
model.add(Flatten())  # 展平所有像素, 比如 [28*28] -> [784]
model.add(Dense(1024, activation='relu')); model.add(Dropout(0.5))  # 防止过拟合
## 第四层全连接层, 添加全连接层 2(即输出层)
model.add(Dense(10, activation='softmax'))  # 0-9 手写数字一个有 10 个类别
##################################################################
## compile(optimizer, loss, metrics=None, sample_weight_mode=None, weighted_metrics=None, **kwargs)
# 编译用来配置模型的学习过程, 其参数有:
# optimizer 优化器: 字符串(预定义优化器名) 或 优化器对象
# loss 损失函数: 字符串(预定义损失函数名) 或 目标函数; 分类和回归问题的不一样, 用的是交叉熵
# metrics: 列表, 包含评估模型在训练和测试时的网络性能的指标, 里面可以放入需要计算的 cost, accuracy, score 等,
#     这里如果没有 metrics, 下面的 evaluate() 就不能用了, 而且 fit() 不会出现 acc 信息

## 回归问题:
model.compile(optimizer='sgd', loss='mse')  # 均方误差, 随机梯度下降; 回归其实不用 accuracy, 因为会一直是 0...

## 分类问题:
# 设置 adam 优化方法, loss 函数, metrics 方法来观察输出结果
model.compile(optimizer='adadelta', loss='categorical_crossentropy', metrics=['accuracy'])
model.compile(optimizer=keras.optimizers.Adadelta(), loss=keras.metrics.categorical_crossentropy)
# 设置学习率
rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)  # 学习率, ...
rmsprop = RMSprop(lr=0.001)  # It is recommended to leave the parameters of this optimizer at their default values (except the learning rate)
model.compile(optimizer=rmsprop, loss='categorical_crossentropy', metrics=['accuracy'])  # 最终采用这个
##################################################################
## 自定义 batch_size 就是 MBGD; train_on_batch 将批次手动传入模型, 是 BGD
## fit(self, x, y, batch_size=32, epochs=10, verbose=1, callbacks=None, validation_split=0.0, validation_data=None, shuffle=True, class_weight=None, sample_weight=None, initial_epoch=0)
# batch_size 太小会导致训练慢, 过拟合等问题, 太大会导致欠拟合; 所以要适当选择
# verbose: 日志显示, 0 为不在标准输出流输出日志信息, 1 为输出进度条记录, 2 为每个 epoch 输出一行记录;
# validation_split: 0~1 之间的浮点数, 用来指定训练集的一定比例数据作为验证集. 验证集将不参与训练, 并在每个 epoch 结束后测试的模型的指标, 如损失函数, 精确度等;
# validation_data: 形式为(X, y) 的 tuple, 是指定的验证集. 此参数将覆盖 validation_spilt.

## 全连接层: fit() 和 train_on_batch() 两种里面选一种训练就行了
model.fit(X_train, y_train, epochs=2, batch_size=32)  # ** epochs=2 就这么高的识别率, 还是数据集比较多的好 **
# Epoch 1/2
# 60000/60000 [==============================] - 4s - loss: 0.3606 - acc: 0.8988
# Epoch 2/2
# 60000/60000 [==============================] - 4s - loss: 0.2040 - acc: 0.9413
model.fit(X_train, y_train, epochs=2, batch_size=32, validation_data=(X_test, y_test))  # 添加 validation_data 会多一些 val_* 信息
# Epoch 1/2
# 60000/60000 [==============================] - 4s - loss: 0.1640 - acc: 0.9527 - val_loss: 0.1552 - val_acc: 0.9557
# Epoch 2/2
# 60000/60000 [==============================] - 5s - loss: 0.1410 - acc: 0.9592 - val_loss: 0.1432 - val_acc: 0.9576
# train_on_batch(x, y, class_weight=None, sample_weight=None): Single gradient update over one batch of samples.
for step in range(10):
    cost = model.train_on_batch(X_train, y_train)  # 默认不会自己输出信息, 需要下面的手动输出
    if step % 9 == 0: print('train cost: ', cost)  # 第 0 次, 和第 9 次会输出

## CNN, 因为 CNN 网络太复杂, 所以去了前 5000 来训练, 否则太慢
model.fit(X_train[:5000], y_train[:5000], epochs=1, batch_size=64, validation_data=(X_test, y_test))  # acc 涨得好快
# Epoch 1/1
# 5000/5000 [==============================] - 72s - loss: 0.8619 - acc: 0.7272 - val_loss: 0.2550 - val_acc: 0.9200
##################################################################
## evaluate(x, y, batch_size=32, verbose=1, sample_weight=None): Computes the loss on some input data, batch by batch
## 回归问题 只有 loss,  因为回归问题 compile() 中一般也不定义 metrics=
## 下面的回归分析在 ./l1_Regressor-回归分析.py, 这里只是比较一下
loss = model.evaluate(X_test, y_test); print("test loss:", loss)  # 这样写是因为 compile() 里没写 metrics=''
W, b = model.layers[0].get_weights(); print("Weights:", W, "baise:",b)  # Weights: [[ 1.5692327]] baise: [ 0.52575564]

## 分类问题
loss, accuracy = model.evaluate(X_test, y_test)  # Evaluate the model with the metrics we defined earlier, 前面的 compile() 要加上 metrics
print('loss:', loss, 'accuracy: ', accuracy)  # loss: 0.175076550314 accuracy:  0.9485
print(len(model.layers[0].get_weights()))  # 2; W 和 b
print(len(model.layers[0].get_weights()[0]), len(model.layers[0].get_weights()[1]))  # 784, 32; W 对应输入 784 维, b 对应输出 32 维
print(len(model.layers[1].get_weights()))  # 0; 激活层没有权重
print(len(model.layers[2].get_weights()))  # 2; W 和 b
print(len(model.layers[2].get_weights()[0]), len(model.layers[2].get_weights()[1]))  # 32 10; W 对应输入 32 维, b 对应输出 10 维
##################################################################
## predict(x, batch_size=32, verbose=0): Generates output predictions for the input samples.
y_pred = model.predict(X_test)
print(y_pred.shape, y_pred[0])  # (10000, 10); 分类问题从来不要求精确输出, 只要有大小关系就行了
# [  5.10046857e-06   5.12467118e-08   3.87858381e-05   7.80041737e-04
#    1.25964021e-08   1.95981374e-06   3.14197601e-09   9.99122083e-01
#    8.86169164e-06   4.31045592e-05]

y_pred_classes = model.predict_classes(X_test)
print(y_pred_classes.shape, set(y_pred_classes))  # (10000,) {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(y_pred_classes[0])  # 7; predict_classes() 就是按照 predict() 结果里的最大的那个来定类别的
# 所以 np_utils.to_categorical() 对多分类问题很重要

y_pred_proba = model.predict_proba(X_test)
print(y_pred_proba.shape, y_pred_proba[0])  # (10000, 10)
# [  5.10046857e-06   5.12467118e-08   3.87858381e-05   7.80041737e-04
#    1.25964021e-08   1.95981374e-06   3.14197601e-09   9.99122083e-01
#    8.86169164e-06   4.31045592e-05]
##################################################################
## 分类问题处理流程:
# 1. X_train: 降维, 归一化;     y_train: to_categorical()
# 2. model.compile(optimizer=RMSprop(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
# 3. loss, accuracy = model.evaluate(X_test, y_test)

## 回归问题处理流程:
# 1. X_train: 数值化;     y_train: 数值化
# 2. model.compile(optimizer='sgd', loss='mse')  # 这里一般没有 metrics(会一直是 0, 不会精确的计算得到), 所以回归问题 evaluate() 只有 loss
# 3. loss = model.evaluate(X_test, y_test); print("test loss:", loss)

## 常见的还是分类问题
## 注意:
# 1. batch 是在 fit() 和 evaluate() 中才考虑的, Sequential() 模型中不用考虑
