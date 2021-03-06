#!/bin/bash
##################################################################
## 1. dns
cat /etc/resolvconf
# Dynamic resolv.conf(5) file for glibc resolver(3) generated by resolvconf(8)
#     DO NOT EDIT THIS FILE BY HAND -- YOUR CHANGES WILL BE OVERWRITTEN
nameserver 127.0.1.1
##################################################################
## 2. nmcli
nmcli dev  # 查看当前网络设备
nmcli con  # 会显示已链接的网络设备, 竟然看到了 802-3-ethernet
nmcli dev show | grep dns  # 查看当前的 DNS
nmcli dev show | grep gateway  # 查看当前的网关
##################################################################
## 3. dhclient 重新申请 DHCP 的 IP 地址, 没弄成
sudo dhclient –v  # say "hello" to our DHCP server, verbose
# Listening on LPF/wlan0/68:a3:c4:93:47:46
# Sending on   LPF/wlan0/68:a3:c4:93:47:46
# Sending on   Socket/fallback
# DHCPDISCOVER on wlan0 to 255.255.255.255 port 67 interval 4
# DHCPREQUEST on wlan0 to 255.255.255.255 port 67
# DHCPOFFER from 192.168.2.1
# DHCPACK from 192.168.2.1
# RTNETLINK answers: File exists
# bound to 192.168.2.4 -- renewal in 42516 seconds.
sudo dhclient –r -v  # 释放 DHCP lease
sudo vim /etc/dhcp/dhclient.conf  # 添加下面这句话 send dhcp-requested-address 172.18.140.157;
sudo vim /var/lib/dhcp/dhclient.leases  # 这里面写着 lease, 改了也不行
sudo rm /var/lib/dhcp/dhclient.leases
sudo dhclient  # Ubuntu will contact the network’s DHCP server and obtain a new address.
sudo dhclient -4 -d -v -cf /etc/dhcp/dhclient.conf  # 为所有的 if 申请
sudo dhclient -4 -d -v -cf /etc/dhcp/dhclient.conf enx00e04c6804e1  # 为指定 if 申请
