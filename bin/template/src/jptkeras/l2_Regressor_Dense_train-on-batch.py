#!/usr/bin/python3
# coding: utf-8
import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.models import Sequential  # 按顺序添加层
from keras.layers import Dense  # 全连接层, 作为 Sequential 的第一个隐藏层
import matplotlib.pyplot as plt
##################################################################
## create some data
X = np.linspace(-1, 1, 200)
np.random.shuffle(X)    # randomize the data, will change X.
Y = 0.5 * X + 2 + np.random.normal(0, 0.05, (200, ))
##################################################################
## plot data
plt.scatter(X, Y)
plt.show()
##################################################################
## split to train and test data
X_train, Y_train = X[:160], Y[:160]  # first 160 data points
X_test, Y_test = X[160:], Y[160:]    # last 40 data points
##################################################################
## build a neural network from the 1st layer to the last layer
model = Sequential()  # 默认第二层输入是第一层的输出
model.add(Dense(units=1, input_dim=1))  # 添加全连接层, 隐藏层
# choose loss function and optimizing method
model.compile(loss='mse', optimizer='sgd')  # mean square, 优化器
##################################################################
## training
print('Training -----------')
for step in range(301):
    cost = model.train_on_batch(X_train, Y_train)  # 不断的训练
    if step % 100 == 0:
        print('train cost: ', cost)  # 误差
##################################################################
## test
print('\nTesting ------------')
cost = model.evaluate(X_test, Y_test, batch_size=40)
print('test cost:', cost)  # 误差
W, b = model.layers[0].get_weights()  # Dense 层的相关信息
print('Weights=', W, '\nbiases=', b)  # Weights = 0.5; biase = 2
##################################################################
## plotting the prediction
Y_pred = model.predict(X_test)
plt.scatter(X_test, Y_test)
plt.plot(X_test, Y_pred)
plt.show()
##################################################################
## 总结:
# 1. 两次画出 plot
# 2. Dense 层适合做回归分析
# 3. 使用 for 循环来训练数据
