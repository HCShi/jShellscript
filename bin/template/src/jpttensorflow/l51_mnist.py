#!/usr/bin/python3
# coding: utf-8
# 我们见到的大多数机器学习示例都将使用 MNIST 手写体数字数据集, 手写体数字识别已经在诸如邮局邮政编码识别等方面得到了广泛的运用
# MNIST 包含 60000 张训练图片(包括 5000 张验证图片), 10000 张测试图片(黑盒),
# 这些图片已经进行了归一化, 并且大小固定, 每张手写数字图片其实是一张可以被转化成矩阵的 28 x 28 的灰度图片
# 在 TensorFlow 中, 使用 MNIST 非常简单, 它将帮助我们去下载数据并将自动地载入 numpy 中的 array 对象, 同时还可以进行独热编码等数据预处理
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('./tmp_dataset/mnist', one_hot=True)  # 'count', 'index', 'test', 'train', 'validation' 有这些属性
# 第一次执行会从网上下载, 所以这个命令的速度和网速有关...; 所以还是 keras 中的 mnist 加载快
##################################################################
## 简单使用方式
xs_train = mnist.train.images  # 形状为 55000 * 784 位的 tensor, 一个多维数组, 第一维表示图片的索引, 第二维表示图片中像素的索引
ys_train = mnist.train.labels
xs_test = mnist.test.images
ys_test = mnist.test.labels

# 下面进行属性测试
##################################################################
## count, index 是内置函数, 类似于 list.count()
print(['a', 'b', 'c'].count('a'))  # 1
print(['a', 'b', 'c'].index('a'))  # 0
##################################################################
## test 含有 'epochs_completed', 'images', 'labels', 'next_batch', 'num_examples' 等属性
print(mnist.test.num_examples)  # 10000
test_labels = mnist.test.labels; print(test_labels.shape)  # (10000, 10); 因为 one_hot=True, 所以是 10
test_images = mnist.test.images; print(test_images.shape)  # (10000, 784); 28*28 = 784
##################################################################
## train 含有 'epochs_completed', 'images', 'labels', 'next_batch', 'num_examples' 等属性
print(mnist.train.num_examples)  # 55000
train_labels = mnist.train.labels; print(train_labels.shape)  # (55000, 10)
train_images = mnist.train.images; print(train_images.shape)  # (55000, 784)
##################################################################
## validation 含有 'epochs_completed', 'images', 'labels', 'next_batch', 'num_examples'
print(mnist.validation.num_examples)  # 5000
validation_labels = mnist.validation.labels; print(validation_labels.shape)  # (5000, 10)
validation_images = mnist.validation.images; print((validation_images.shape))  # (5000, 784)
##################################################################
## next_batch() 以 test 为例, 获取接下来的 100 张图片以及标签
# next_batch() 函数可以遍历整个数据集并返回所需的部分数据集样本; 这么做可以节省内存, 将数据集切成块, 避免加载整个数据集
for i in range(1000):
    batch_xs, batch_ys = mnist.test.next_batch(100)  # 每一次的循环中, 我们取训练数据中的 100 个随机数据, 这种操作成为批处理 (batch)
    print(batch_xs.shape, batch_ys.shape)  # (100, 784) (100, 10)
