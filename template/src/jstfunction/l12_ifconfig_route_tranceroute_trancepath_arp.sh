#!/bin/bash
##################################################################
## 1. ifconfig, 以 nginx 配置 虚拟主机为例
##################################################################
ifconfig eth0 192.168.1.9 netmask 255.255.255.0  # 配置 eth0
# 配置 eth0 分设备 配置 虚拟主机
ifconfig eth0:1 192.168.1.7 broadcast 192.168.1.255 netmask 255.255.255.0
ifconfig eth0:2 192.168.1.17 broadcast 192.168.1.255 netmask 255.255.255.0
##################################################################
## 1.1 SDN 当时官方的主机无法访问网页, 但可以 ping
route -n  # 查看那块网卡通信
sudo ifconfig eth1 mtu 1454
##################################################################
## 1.2 配置固定 IP, 机房用自己笔记本上机, 将下面四行丢进一个文件里, 石油大学基础实验楼的配置
sudo ifconfig enx00e04c6804e1 172.20.21.159 netmask 255.255.255.0
sudo route add default gw 172.20.21.254
sudo echo "nameserver 211.87.191.66" >> /etc/resolv.conf  # /etc/resolv.conf 中修改后下次启动会自动删除, 很适合去机房
# 正常连接 Auto Ethernet 就可以了, 配置只能从 ifconfig 中的 enx00e04c6804e1 上看到, 右上角看不到
# 可能 enp4s0f2 会占掉路由, 打开 wireshark 看一下是哪个网卡走的流量, sudo ifconfig enp4s0f2 down 将其禁用
# 好像不用配置 DNS, 可以配置为 211.87.191.66, 211.87.191.77(UPC D402)
sudo service networking restart  # 刷新, 上面的配置失效
##################################################################
## 1.3 配置 IP 地址 (host-only)
# 1. 通过命令直接配置, 服务器重启后, 配置信息丢失
sudo ifconfig eth0 192.168.137.11 netmask 255.255.255.0
sudo route add default gw 192.168.137.1
# 配置 IP 地址后, 需要配置 DNS
sudo vim /etc/resolv.conf  # 在 DNS 解析文件中添加后面的部分, 在 nameserver 那行后面再添加一行
``` nameserver 192.168.137.1 ```
sudo /etc/init.d/networking restart  # 重启网卡配置, 上面的配置就会失效
# 2. 直接修改配置文件, 重启服务器后配置信息不会丢失
su -  # 进入 root 模式
sudo vim /etc/network/interfaces  # 替换有关 eth0 的行, 如果没有关于 eth0 信息, 直接在 loopback 后添加
```
auto lo
iface lo inet loopback
auto enp4s0f2
iface enp4s0f2 inet static
    address 172.20.21.157
    netmask 255.255.255.0
    gateway 172.20.21.254
    # network 192.168.137.0
    # broadcast 192.168.137.255
```
sudo /etc/init.d/networking restart  # 重启网卡服务即可, 可能还需要配置 DNS, 像上面那样
##################################################################
## 1.4 PredictableNetworkInterfaceNames
# The names have two-character prefixes based on the type of interface:
en  # for Ethernet,
wl  # for wireless LAN (WLAN),
ww  # for wireless wide area network (WWAN).

# The names have the following types:
o<index>
    # on-board device index number
s<slot>[f<function>][d<dev_id>]
    # hotplug slot index number. All multi-function PCI devices will carry the [f<function>] number in the device name, including the function 0 device.
x<MAC>
    # MAC address
[P<domain>]p<bus>s<slot>[f<function>][d<dev_id>]
    # PCI geographical location. In PCI geographical location, the [P<domain>] number is only mentioned if the value is not 0. For example:
    # ID_NET_NAME_PATH=P1enp5s0
[P<domain>]p<bus>s<slot>[f<function>][u<port>][..][c<config>][i<interface>]
    # USB port number chain. For USB devices, the full chain of port numbers of hubs is composed.
    # If the name gets longer than the maximum number of 15 characters, the name is not exported.
    # If there are multiple USB devices in the chain, the default values for USB configuration descriptors (c1) and USB interface descriptors (i0) are suppressed.

# example
wlp3s0           # WLAN,     第 3 个总线, 第 0 个插槽
enp4s0f2         # Ethernet, 第 4 个总线, 第 0 个插槽
enx00e04c6804e1
##################################################################
## 2. route
route / route -n  # 等同于 netstat -nr, 第一行会显示路由器的 IP, -n 是将 IP 用数字表示出来
ip route  # 更详细的信息
##################################################################
## 2.1 查看网关地址的三种方法 (eth0 网关地址为 192.168.217.2)
ip route [show]  # show 可以不用写
# default via 192.168.217.2 dev eth0  metric 100
# default via 192.168.10.252 dev wlp3s0  proto static  metric 600
# 169.254.0.0/16 dev wlp3s0  scope link  metric 1000
# 192.168.122.0/24 dev virbr0  proto kernel  scope link  src 192.168.122.1
# 172.17.0.0/16 dev docker0  proto kernel  scope link  src 172.17.0.1 linkdown
# 192.168.217.0/24 dev eth0  proto kernel  scope link  src 192.168.217.129
route -n   # 或者 netstat -rn
# Kernel IP routing table
# Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
# 0.0.0.0         192.168.217.2   0.0.0.0         UG    100    0        0 eth0
# 192.168.122.0   0.0.0.0         255.255.255.0   U     0      0        0 virbr0
# 192.168.217.0   0.0.0.0         255.255.255.0   U     0      0        0 eth0
traceroute www.baidu.com  # tracepath 不会显示网关
# traceroute to www.baidu.com (119.75.218.77), 30 hops max, 60 byte packets
#  1  localhost (192.168.217.2)  0.607 ms  0.546 ms  1.379 ms
#  2  * * *
#  3  * * *
##################################################################
## 3. traceroute && tracepath
tracepath -n 8.8.8.8  # 可以看到自己外网 IP 对应的对面的 IP, -n 是用数字表示 IP
curl ifconfig.me  # 看到自己的外网 IP
# tracepath 比 traceroute 强大, 而且兼容
##################################################################
## 4. arp
arp -n  # 会显示 网关 IP 和 MAC
