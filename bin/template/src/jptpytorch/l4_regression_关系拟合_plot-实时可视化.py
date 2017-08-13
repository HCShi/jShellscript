#!/usr/bin/python3
# coding: utf-8
import torch
from torch.autograd import Variable
import torch.nn.functional as F  # 激励函数
import matplotlib.pyplot as plt

torch.manual_seed(1)    # reproducible
##################################################################
## 生成伪数据 并 plot
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # x data (tensor), shape=(100, 1); unsqueeze 将一维变成二维
y = x.pow(2) + 0.2 * torch.rand(x.size())               # noisy y data (tensor), shape=(100, 1)
# torch can only train on Variable, so convert them to Variable
x, y = Variable(x), Variable(y)
plt.scatter(x.data.numpy(), y.data.numpy())
plt.show()
##################################################################
## Neural Networks 定义
class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):  # 定义神经网络搭建所需要的信息, 搭建过程在 forward()
        super(Net, self).__init__()  # 固定步骤
        self.hidden = torch.nn.Linear(n_feature, n_hidden)  # hidden layer; 定义变量同时就命名了
        self.predict = torch.nn.Linear(n_hidden, n_output)  # output layer; 参数是 输入 和 输出 的个数
    def forward(self, x):  # 神经网络搭建过程
        x = F.relu(self.hidden(x))  # activation function for hidden layer; 激励函数激活信息
        x = self.predict(x)         # linear output
        return x
net = Net(n_feature=1, n_hidden=10, n_output=1)  # define the network; 参数依次为: 输入, 隐藏, 输出
print(net)  # net architecture
##################################################################
## 优化神经网络
optimizer = torch.optim.SGD(net.parameters(), lr=0.5)  # 优化器; learning_rate
loss_func = torch.nn.MSELoss()  # this is for regression mean squared loss
##################################################################
## 开始训练
plt.ion()  # something about plotting; not blocking
for t in range(100):  # 训练 100 步
    prediction = net(x)  # input x and predict based on x
    loss = loss_func(prediction, y)  # must be (1. nn output, 2. target)
    # 开始优化
    optimizer.zero_grad()  # clear gradients for next train
    loss.backward()        # backpropagation, compute gradients
    optimizer.step()       # apply gradients
    # 开始可视化; l5_add-layer_build-network_plot-实时可视化.py 进行对比, 两种不同的实时可视化方法
    if t % 5 == 0:
        # plot and show learning process
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
        plt.text(0.5, 0, 'Loss=%.4f' % loss.data[0], fontdict={'size': 20, 'color':  'red'})
        plt.pause(0.1)
plt.ioff()
plt.show()
