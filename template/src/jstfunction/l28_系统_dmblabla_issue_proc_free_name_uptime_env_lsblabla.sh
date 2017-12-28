#!/bin/bash
##################################################################
## 系统
dmidecode | grep "Product Name"  # 查看机器型号
dmesg | grep -i eth              # 查看网卡信息

cat /etc/issue     # 查看操作系统版本; 有些系统上没有 lsb_release 命令, 或者 不太好用的, eg. Redhat
cat /etc/*release  # 查看系统发型版本
uname -a && cat /etc/*release  # 最详细的查看系统信息的命令
cat /proc/version  # 和 uname -a 差不多, 有的系统 uname -a 显示的信息很少, eg. 信工所实验室 CentOS 服务器
cat /proc/cpuinfo  # 查看 CPU 信息
cat /proc/meminfo  # 查看 Memory 相关信息
cat /proc/loadavg  # 查看系统负载

cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c  # 查看 CPU 核数 及 型号信息
# 4  Intel(R) Core(TM) i5-3230M CPU @ 2.60GHz  # 4 核, Intel i5
cat /proc/cpuinfo | grep physical | uniq -c  # 从下面的输出得知 4 核是 4 颗单核 CPU
# 1 physical id     : 0
# 1 address sizes   : 36 bits physical, 48 bits virtual
# 1 physical id     : 0
# 1 address sizes   : 36 bits physical, 48 bits virtual
# 1 physical id     : 0
# 1 address sizes   : 36 bits physical, 48 bits virtual
# 1 physical id     : 0
# 1 address sizes   : 36 bits physical, 48 bits virtual
getconf LONG_BIT  # 32, 说明当前 CPU 运行在 32bit 模式下, 但不代表 CPU 不支持 64bit

grep MemTotal /proc/meminfo   # 查看内存总量
grep MemFree /proc/meminfo    # 查看空闲内存量
free -m  # 查看内存使用量和交换区使用量, -m 是以 MB 为单位
free -g  # -g 是以 GB 为单位

uname -a  # 查看所有系统信息; --help 查看 uname 功能
hostname  # 查看计算机名
uptime    # 查看系统运行时间、用户数、负载
env       # 查看环境变量

lsb_release -a  # 查看 系统 版本
lspci -tv       # 列出所有 PCI 设备, 外部设备总线标准
lsusb -tv       # 列出所有 USB 设备
lsmod           # 列出加载的内核模块
##################################################################
## env 排错
env | grep -i proxy  # 查看终端代理
