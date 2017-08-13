#!/usr/bin/python3
# coding: utf-8
import torch
from torch.autograd import Variable
##################################################################
## Variable
# Variable in torch is to build a computational graph,
# but this graph is dynamic compared with a static graph in Tensorflow or Theano.
# So torch does not have placeholder, torch can just pass variable to the computational graph.
tensor = torch.FloatTensor([[1,2],[3,4]])        # build a tensor
variable = Variable(tensor, requires_grad=True)  # build a variable, usually for compute gradients
print(tensor)       # [torch.FloatTensor of size 2x2]
print(variable)     # [torch.FloatTensor of size 2x2]
##################################################################
## 反向传递
# till now the tensor and variable seem the same.
# However, the variable is a part of the graph, it's a part of the auto-gradient.
t_out = torch.mean(tensor * tensor)      # x^2
v_out = torch.mean(variable * variable)  # x^2
print(t_out)  # 7.5
print(v_out)  # 7.5, 还会包含图的信息

v_out.backward()  # backpropagation from v_out; 误差的反向传递
# v_out = 1/4 * sum(variable*variable)
# the gradients w.r.t the variable, d(v_out)/d(variable) = 1/4*2*variable = variable/2
print(variable.grad)  # 反向传递的梯度, 会被 v_out.backward() 影响
print(variable)               # this is data in variable format
print(variable.data)          # this is data in tensor format
print(variable.data.numpy())  # numpy format
