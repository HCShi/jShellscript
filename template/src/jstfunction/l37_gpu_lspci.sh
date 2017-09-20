#!/bin/bash
## GPU 检测, 要做深度学习了
##################################################################
## lspci 是一个用来显示系统中所有 PCI 总线设备或连接到该总线上的所有设备的工具
# -nn PCI 厂商和设备代码
lspci
# 00:00.0 Host bridge: Intel Corporation 3200/3210 Chipset DRAM Controller  # 主板芯片
# 00:1a.7 USB Controller: Intel Corporation 82801I (ICH9 Family) USB2 EHCI Controller #2 (rev 02)  # USB 控制器
# 00:1c.0 PCI bridge: Intel Corporation 82801I (ICH9 Family) PCI Express Port 1 (rev 02)  # 接口插槽
# 02:00.0 VGA compatible controller: Matrox Graphics, Inc. MGA G200e [Pilot] ServerEngines (SEP1) (rev 02)  # 显卡
# 03:02.0 Ethernet controller: Intel Corporation 82541GI Gigabit Ethernet Controller (rev 05)  # 网卡
lspci | grep -i nvidia  # -i ignore case
# 自己电脑, 华硕 X550VC
# 01:00.0 3D controller: NVIDIA Corporation GF117M [GeForce 610M/710M/810M/820M / GT 620M/625M/630M/720M] (rev a1)
# 实验室服务器, 八路泰坦
# 03:00.0 VGA compatible controller: NVIDIA Corporation GM204 [GeForce GTX 980] (rev a1)
# 03:00.1 Audio device: NVIDIA Corporation GM204 High Definition Audio Controller (rev a1)
# 05:00.0 VGA compatible controller: NVIDIA Corporation GM204 [GeForce GTX 980] (rev a1)
# 05:00.1 Audio device: NVIDIA Corporation GM204 High Definition Audio Controller (rev a1)
lspci -vnn | grep -i nvidia  -A 12  # -A 在往下多输出 12 行
# 自己电脑, 华硕 X550VC
# 01:00.0 3D controller [0302]: NVIDIA Corporation GF117M [GeForce 610M/710M/810M/820M / GT 620M/625M/630M/720M] [10de:1140] (rev a1)
#         Subsystem: ASUSTeK Computer Inc. GeForce GT 720M [1043:124d]
#         Flags: bus master, fast devsel, latency 0, IRQ 29
#         Memory at f6000000 (32-bit, non-prefetchable) [size=16M]
#         Memory at e0000000 (64-bit, prefetchable) [size=256M]
#         Memory at f0000000 (64-bit, prefetchable) [size=32M]
#         I/O ports at e000 [size=128]
#         Expansion ROM at f7000000 [disabled] [size=512K]
#         Capabilities: <access denied>
#         Kernel driver in use: nouveau
#         Kernel modules: nvidiafb, nouveau
lspci -vnn | grep VGA -A 12
# 自己电脑, 华硕 X550VC
# 00:02.0 VGA compatible controller [0300]: Intel Corporation 3rd Gen Core processor Graphics Controller [8086:0166] (rev 09) (prog-if 00 [VGA controller])
#         Subsystem: ASUSTeK Computer Inc. 3rd Gen Core processor Graphics Controller [1043:124d]
#         Flags: bus master, fast devsel, latency 0, IRQ 30
#         Memory at f7400000 (64-bit, non-prefetchable) [size=4M]
#         Memory at d0000000 (64-bit, prefetchable) [size=256M]
#         I/O ports at f000 [size=64]
#         Expansion ROM at <unassigned> [disabled]
#         Capabilities: <access denied>
#         Kernel driver in use: i915
#         Kernel modules: i915
# 第一行输出便有硬件厂商、型号名称/序列号和 PCI ID.
# 8086:0416, 其中冒号前半部分的 8086 表示厂商 ID(这里是 Intel), 后半部分 0416 表示 PCI ID, 用于指示图形单元模型.
##################################################################
## lshw 查看显卡驱动 && modinfo 查看驱动详细信息
sudo lshw -C display  # 相当于 lspci -vnn | grep -i VGA/nvidia -A 12 两个命令结合
sudo lshw -c video | grep configuration  # 系统上所使用的显卡驱动名称
#   configuration: driver=nouveau latency=0
#   configuration: driver=i915 latency=0
# 可以看到输出的显卡驱动名称有两条, 其中一条为 driver=i915, 我们则可以使用如下命令来检查显卡驱动的详情
modinfo nouveau  # 显示是 Nvidia 公司的
modinfo i915  # 结果很长, 显示是 Intel 公司的
##################################################################
## 总结:
# 1. 大多数 Linux 发行版都可以检测出显卡品牌, 但并不总能正确识别型号, 我们可能需要手动查看显卡型号/序列号
# 2. /proc/iomem 描述了系统中所有的设备 I/O 在内存地址空间上的映射
# 3. lspci 主要扫描 /sys/bus/pci/devices 中的文件, 并根据 pci 设备的 vender 及 device 到 /usr/share/hwdata/pci.ids 去做设备名称匹配并输出
##################################################################
## 常见缩写
# VGA: Video Graphics Array
