#!/usr/bin/python3
# coding: utf-8
import torch
import numpy as np
##################################################################
## convert numpy to tensor or vise versa
np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)  # 从 numpy 转化为 torch
tensor2array = torch_data.numpy()       # 从 torch 转化为 numpy
##################################################################
## abs
data = [-1, -2, 1, 2]
tensor = torch.FloatTensor(data)  # 32-bit floating point
print('\nnumpy: ', np.abs(data))  # [1 2 1 2]
print('\ntorch: ', torch.abs(tensor))  # [1 2 1 2]
##################################################################
## sin
print('\nnumpy: ', np.sin(data))       # [-0.84147098 -0.90929743  0.84147098  0.90929743]
print('\ntorch: ', torch.sin(tensor))  # [-0.8415 -0.9093  0.8415  0.9093]
##################################################################
## mean
print('\nnumpy: ', np.mean(data))       # 0.0
print('\ntorch: ', torch.mean(tensor))  # 0.0
##################################################################
## matrix multiplication
data = [[1,2], [3,4]]
tensor = torch.FloatTensor(data)  # 32-bit floating point
# correct method
print('\nnumpy: ', np.matmul(data, data))     # [[7, 10], [15, 22]]
print('\ntorch: ', torch.mm(tensor, tensor))  # [[7, 10], [15, 22]]
# incorrect method
data = np.array(data)
print('\nnumpy: ', data.dot(data))      # [[7, 10], [15, 22]]
print('\ntorch: ', tensor.dot(tensor))  # this will convert tensor to [1,2,3,4], you'll get 30.0
