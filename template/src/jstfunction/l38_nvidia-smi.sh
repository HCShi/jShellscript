#!/bin/bash
##################################################################
## nvidia-smi
# nvidia-smi 简称 NVSMI, 可查询显卡各种硬件规格指标, 支持 Windows 64 位和 Linux, 该工具是 N 卡驱动附带的, 只要安装好驱动后就会有它
# Windows 下程序位置: C:\Program Files\NVIDIA Corporation\NVSMI\nvidia-smi.exe
# Linux 下程序位置: /usr/bin/nvidia-smi
# 应该使用最新驱动, 只少359.00, 才能看到显卡实时功耗及有关运行参数, 否则显示 N/A
nvidia-smi  # 在 GTX 980 上测试
# Thu Sep 21 17:26:04 2017
# +-----------------------------------------------------------------------------+
# | NVIDIA-SMI 375.66                 Driver Version: 375.66                    |
# |-------------------------------+----------------------+----------------------+
# | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
# | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
# |===============================+======================+======================|
# |   0  GeForce GTX 980     Off  | 0000:03:00.0     Off |                  N/A |
# | 26%   39C    P8    20W / 180W |      0MiB /  4037MiB |      0%      Default |
# +-------------------------------+----------------------+----------------------+
# |   1  GeForce GTX 980     Off  | 0000:05:00.0     Off |                  N/A |
# |ERR!   47C    P0   ERR! / 180W |      0MiB /  4038MiB |      0%      Default |
# +-------------------------------+----------------------+----------------------+
#
# +-----------------------------------------------------------------------------+
# | Processes:                                                       GPU Memory |
# |  GPU       PID  Type  Process name                               Usage      |
# |=============================================================================|
# |  No running processes found                                                 |
# +-----------------------------------------------------------------------------+
nvidia-smi -q -x  # -q: 输出更多信息, 太多了...; -x 以 XML 格式输出
nvidia-smi -L  # Display a list of GPUs connected to the system.
