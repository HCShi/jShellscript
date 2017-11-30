#!/usr/bin/python3
# coding: utf-8
import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.models import Sequential
from keras.layers import Dense, Activation
import matplotlib.pyplot as plt # 可视化模块
##################################################################
## 一: 数据预处理, 自己手动生成数据
X = np.linspace(-1, 1, 200); np.random.shuffle(X); Y = 0.5 * X + 2 + np.random.normal(0, 0.05, (200, ))
plt.scatter(X, Y); plt.show()
X_train, Y_train = X[:160], Y[:160]; X_test, Y_test = X[160:], Y[160:]; print(X_train.shape, Y_train.shape)  # (160,) (160,)
##################################################################
## 二: 模型建立, 简单的一层全连接网络
model = Sequential()
model.add(Dense(1, input_dim=1))  # 对应上面的 (160,) (160,), 所以是 1, 1

# 一旦模型设置完毕, 使用 compile() 设置学习进程
model.compile(loss='mse', optimizer='sgd')  # 均方误差, 随机梯度下降; 每次的 compile() 和后面的没有影响
model.compile(loss='mse', optimizer='sgd', metrics=['accuracy'])  # 回归其实不用 accuracy, 因为会一直是 0...
##################################################################
## 三: 开始训练, 测试不同的训练参数
## fit(x, y, batch_size=32, epochs=10, verbose=1, callbacks=None, validation_split=0.0, validation_data=None, shuffle=True, class_weight=None)
model.fit(X_train, Y_train)
model.fit(X_train, Y_train, epochs=5, batch_size=64, validation_data=(X_test, Y_test))  # 使用 validation 会每次多验证两列
model.fit(X_train, Y_train, epochs=5, batch_size=64, validation_data=(X_test, Y_test), verbose=1)  # verbose 目前没用

# 如果只运行上面的 fit() 会发现还是有较大的偏差, 因为 epochs=5..., 下面的为 301
for step in range(301):
    cost = model.train_on_batch(X_train, Y_train)  # Single gradient update over one batch of samples;
    if step % 100 == 0: print('train cost: ', cost)
##################################################################
## 四: 检验模型, 深入到 Tensorflow 底层
cost = model.evaluate(X_test, Y_test, batch_size=40); print("test cost:",cost)

print(model.layers[0])  # <keras.layers.core.Dense object at 0x7f78206b5898>
print(model.layers[0].get_weights())  # [array([[ 1.5692327]], dtype=float32), array([ 0.52575564], dtype=float32)]
W, b = model.layers[0].get_weights(); print("Weights:", W, "baise:",b)  # Weights: [[ 1.5692327]] baise: [ 0.52575564]
## 下面开始探索 model.layers
print(dir(model.layers[0]))  # 对于上面每一层的查询, 很多方法啊!
# 'activation', 'activity_regularizer', 'add_loss', 'add_update', 'add_weight', 'assert_input_compatibility',
# 'batch_input_shape', 'bias', 'bias_constraint', 'bias_initializer', 'bias_regularizer', 'build', 'built',
# 'call', 'compute_mask', 'compute_output_shape', 'count_params',
# 'dtype', 'from_config',
# 'get_config', 'get_input_at', 'get_input_mask_at', 'get_input_shape_at', 'get_losses_for', 'get_output_at',
#     'get_output_mask_at', 'get_output_shape_at', 'get_updates_for', 'get_weights',
# 'inbound_nodes', 'input', 'input_mask', 'input_shape', 'input_spec',
# 'kernel', 'kernel_constraint', 'kernel_initializer', 'kernel_regularizer',
# 'losses', 'name', 'non_trainable_weights', 'outbound_nodes', 'output', 'output_mask', 'output_shape',
# 'set_weights', 'supports_masking', 'trainable', 'trainable_weights', 'units', 'updates', 'use_bias', 'weights']
layer = model.layers[0]
print(type(layer.bias))  # <class 'tensorflow.python.ops.variables.Variable'>
print(layer.bias.name)  # dense_2/bias:0
print(layer.bias.initial_value)  # Tensor("dense_2/Const:0", shape=(1,), dtype=float32)
print(layer.input_shape)  # (None, 1)
print(layer.name)  # dense_2
##################################################################
## 五: 结果可视化
Y_pred = model.predict(X_test)
plt.scatter(X_test, Y_test); plt.plot(X_test, Y_pred); plt.show()
