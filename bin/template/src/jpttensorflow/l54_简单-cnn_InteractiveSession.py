#!/usr/bin/python3
# coding: utf-8
# 代码是官方文档 (深入 MNIST --专家级)
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
##################################################################
## 0. 准备数据
mnist = input_data.read_data_sets("./tmp_dataset/mnist", one_hot=True)
##################################################################
## 1. 定义模型
# 为了建立模型, 我们需要先创建一些权值 w 和偏置 b 等参数, 这些参数的初始化过程中需要加入一小部分的噪声以破坏参数整体的对称性, 同时避免梯度为 0.
# 由于我们使用 ReLU 激活函数, 所以我们通常将这些参数初始化为很小的正值; 为了避免重复的初始化操作, 我们可以创建下面两个函数
def weight_varible(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)  # Outputs random values from a truncated normal distribution.
    # stddev: The standard deviation of the truncated normal distribution
    return tf.Variable(initial)
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)
# TensorFlow 同样提供了方便的卷积和池化计算; 怎样处理边界元素? 怎样设置卷积窗口大小?
# 在这个例子中, 我们始终使用 vanilla 版本; 这里的卷积操作仅使用了滑动步长为 1 的窗口, 使用 0 进行填充, 所以输出规模和输入的一致
# 而池化操作是在 2*2 的窗口内采用最大池化技术 (max-pooling); 为了使代码简洁, 同样将这些操作抽象为函数形式
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')  # padding='SAME' 表示通过填充 0, 使得输入和输出的形状一致
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')  # 2x2 图像每次池化都会缩小 2 倍
## 1.1 conv layer-1
# 第一层是卷积层, 卷积层将要计算出 32 个特征映射 (feature map), 对每个 5*5 的 patch; 它的权值 tensor 的大小为 [5, 5, 1, 32].
x = tf.placeholder(tf.float32, [None, 784])  # 占位符, 输入 mnist.train.images
y_ = tf.placeholder(tf.float32, [None, 10])  # 占位符, 输入 mnist.train.labels
x_image = tf.reshape(x, [-1, 28, 28, 1])  # 使得图片与计算层匹配, 我们首先 reshape 输入图像 x 为 4 维的 tensor, 第 2、3 维对应图片的宽和高, 最后一维对应颜色通道的数目
W_conv1 = weight_varible([5, 5, 1, 32])                   # 前两维是 patch 的大小, 第三维输入通道的数目, 最后一维是输出通道的数目/输出特征数目/输出神经元数目
b_conv1 = bias_variable([32])                             # 我们对每个输出通道加上了偏置 (bias)
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)  # 然后, 使用 weight tensor 对 x_image 进行卷积计算, 加上 bias, 再应用到一个 ReLU 激活函数
h_pool1 = max_pool_2x2(h_conv1)                           # [n, 14, 14, 32]; 最终采用最大池化
## 1.2 conv layer-2
# 为了使得网络有足够深度, 我们重复堆积一些相同类型的层; 第二层将会有 64 个特征, 对应每个 5*5 的 patch
W_conv2 = weight_varible([5, 5, 32, 64])  # 第一次处理的是一个通道, 一个特征, 厚度为 1; 后来变成了 32 个特征, 相当于是厚度增加为 32;
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)  # [n, 7, 7, 64] 维度, n = len(patch) 大小有关; 这里 patch 传入的是 50
## 1.3 full connection
# 到目前为止, 图像的尺寸被缩减为 7*7, 我们最后加入一个神经元数目为 1024 的全连接层来处理所有的图像上;
# 接着, 将最后的 pooling 层的输出 reshape 为一个一维向量, 与权值相乘, 加上偏置, 再通过一个 ReLu 函数
W_fc1 = weight_varible([7 * 7 * 64, 1024])  # 此时, 图像 7*7, 厚度变为了 64; 输出 1024 个特征/神经元/厚度
b_fc1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])  # 这里 -1 将会被替换为 patch 大小, 本代码为 50
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)  # [  50 1024]
## 1.4 dropout
# 为了减少过拟合程度, 在输出层之前应用 dropout 技术 (即丢弃某些神经元的输出结果);
# 我们创建一个 placeholder 来表示一个神经元的输出在 dropout 时不被丢弃的概率; Dropout 能够在训练过程中使用, 而在测试过程中不使用;
# TensorFlow 中的 tf.nn.dropout 操作能够利用 mask 技术处理各种规模的神经元输出
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
## 1.5 output layer: softmax
# 最终, 我们用一个 softmax 层, 得到类别上的概率分布. (与之前的 Softmax Regression 模型相同)
W_fc2 = weight_varible([1024, 10])
b_fc2 = bias_variable([10])
y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)  # 最终得到 [n, 10] 的矩阵, n 为 patch 大小 / 50
##################################################################
## 2. 模型训练; model training
# 为了测试模型的性能, 需要先对模型进行训练, 然后应用在测试集上; 和之前 Softmax Regression 模型中的训练、测试过程类似; 区别在于:
# 1. 用更复杂的 ADAM 最优化方法代替了之前的梯度下降
# 2. 增了额外的参数 keep_prob 在 feed_dict 中, 以控制 dropout 的几率
# 3. 在训练过程中, 增加了 log 输出功能 (每 100 次迭代输出一次)
cross_entropy = -tf.reduce_sum(y_ * tf.log(y_conv))  # 计算交叉熵
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.arg_max(y_conv, 1), tf.arg_max(y_, 1))  # 用 one-hot 进行结果比对, 1 表示 第一维
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
##################################################################
## 3. 初始化
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())
##################################################################
## 4. 开始训练
for i in range(1000):
    batch = mnist.train.next_batch(50)  # 返回 [images[:50], labels[:50]]
    if i % 100 == 0:
        train_accuacy = accuracy.eval(feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0})
        print("step %d, training accuracy %g" % (i, train_accuacy))
    train_step.run(feed_dict = {x: batch[0], y_: batch[1], keep_prob: 0.5})
# 测试 shape
batch = mnist.train.next_batch(50)
print(tf.shape(x_image).eval(feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0}))  # [50 28 28  1]
print(tf.shape(W_conv1).eval(feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0}))  # [ 5  5  1 32]
print(tf.shape(h_pool1).eval(feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0}))  # [50 14 14 32]
print(tf.shape(h_pool2).eval(feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0}))  # [50  7  7 64]
print(tf.shape(h_fc1).eval(feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0}))  # [  50 1024]
##################################################################
## 5. 评估结果; accuacy on test
print("test accuracy %g" % (accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0})))
# 最终, 模型在测试集上的准确率大概为 99.2%, 性能上要优于之前的 Softmax Regression 模型
##################################################################
## 总结:
# 1. InteractiveSession 允许你做一些交互操作, 通过创建一个计算流图 (computation graph) 来部分地运行图计算
#    当你在一些交互环境中使用时将更加方便; 如果你不是使用 InteractiveSession, 那么你要在启动一个会话和运行图计算前, 创建一个整体的计算流图
# 2. 因为每层之间的 W 和 b 不太一样, 所以开始我们定义了很多生成 W 和 b 的函数
# 3. Normal Distribution 称为正态分布, 也称为高斯分布, Truncated Normal Distribution 一般翻译为截断正态分布, 也有称为截尾正态分布
#    截断正态分布是截断分布 Truncated Distribution 的一种, 那么截断分布是什么? 截断分布是指, 限制变量 x 取值范围 scope 的一种分布
