#!/usr/bin/python3
# coding: utf-8
import keras
from keras.datasets import mnist  # 手写数字数据源
from keras.models import Sequential  # Sequential 可以封装各种神经网络层, 包括 Dense 全连接层, Dropout 层, Cov2D 卷积层
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
##################################################################
## 接下来, 我们准备训练集和测试集, 以及一些重要参数
batch_size = 128  # batch_size 太小会导致训练慢, 过拟合等问题, 太大会导致欠拟合; 所以要适当选择
num_classes = 10  # 0-9 手写数字一个有 10 个类别
epochs = 12  # 12 次完整迭代, 差不多够了
img_rows, img_cols = 28, 28  # 输入的图片是 28 * 28 像素的灰度图
(x_train, y_train), (x_test, y_test) = mnist.load_data()  # 训练集, 测试集收集非常方便
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)  # (60000, 28, 28) (60000,) (10000, 28, 28) (10000,)

# keras 输入数据有两种格式, 一种是通道数放在前面, 一种是通道数放在后面, 其实就是格式差别而已
if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)
x_train = x_train.astype('float32') / 255  # 把数据变成 float32 更精确
x_test = x_test.astype('float32') / 255; print(x_train.sum(), x_test.sum())  # 6.14628e+06, 1.03892e+06
print('x_train shape:', x_train.shape)  # (60000, 28, 28, 1)
print(x_train.shape[0], 'train samples')  # 60000 train samples
print(x_test.shape[0], 'test samples')
# 把类别 0-9 变成 2 进制, 方便训练
y_train = keras.utils.np_utils.to_categorical(y_train, num_classes)
y_test = keras.utils.np_utils.to_categorical(y_test, num_classes)
##################################################################
## 然后, 是令人兴奋而且简洁得令人吃鲸的训练构造 cnn 和训练过程
# 牛逼的 Sequential 类可以让我们灵活地插入不同的神经网络层
model = Sequential()
model.add(Conv2D(32,  # 加上一个 2D 卷积层, 32个输出(也就是卷积通道), 激活函数选用 relu, 卷积核的窗口选用 3*3 像素窗口
                 activation='relu',
                 input_shape=input_shape,
                 nb_row=3,
                 nb_col=3))
model.add(Conv2D(64, activation='relu',  # 64 个通道的卷积层
                 nb_row=3,
                 nb_col=3))
model.add(MaxPooling2D(pool_size=(2, 2)))  # 池化层是 2*2 像素的
model.add(Dropout(0.35))  # 对于池化层的输出, 采用 0.35 概率的 Dropout
model.add(Flatten())  # 展平所有像素, 比如 [28*28] -> [784]
model.add(Dense(128, activation='relu'))  # 对所有像素使用全连接层, 输出为 128, 激活函数选用 relu
model.add(Dropout(0.5))  # 对输入采用 0.5 概率的 Dropout
model.add(Dense(num_classes, activation='softmax'))  # 对刚才 Dropout 的输出采用 softmax 激活函数, 得到最后结果 0-9
# 模型我们使用交叉熵损失函数, 最优化方法选用 Adadelta
model.compile(loss=keras.metrics.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])
# 令人兴奋的训练过程
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs,
          verbose=1, validation_data=(x_test, y_test))
##################################################################
## 完整地训练完毕之后, 可以计算一下预测准确率
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
##################################################################
## 总结:
# 1. 需要运行大约 10 min
