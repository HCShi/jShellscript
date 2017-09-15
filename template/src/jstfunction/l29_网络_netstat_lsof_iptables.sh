#!/bin/bash
# 查看已经连接的服务端口 ESTABLISHED
##################################################################
## netstat 查看端口使用情况; 显示 tcp 传输协议的连线情况
sudo netstat -antp
# -a/--all         显示所有连线中的 Socket
# -n/--numeric     直接使用 IP 地址, 而不通过域名服务器
# -t/--tcp         显示 TCP 传输协议的连线状况
# -u/--udp         显示 UDP 传输协议的连线状况
# -i/--interfaces  显示网络界面信息表单
# -l/--listening   显示监控中的服务器的 Socket
# -p/--programs    显示正在使用 Socket 的程序识别码和程序名称

netstat -tulpn | grep :21  # 查看 21 号端口, ftp 端口是否打开, 用的是 vsftpd 软件
# tcp        0      0 0.0.0.0:21             0.0.0.0:*               LISTEN
netstat -a | grep ftp
# tcp        0      0 *:ftp                   *:*                     LISTEN

netstat -i  # 查看 MTU 显示网卡列表
netstat -g  # 显示组播组关系
netstat -s  # 显示网络统计信息
netstat -ap  # 查看所有的服务端口 (LISTEN, ESTABLISHED)
netstat -ap | grep 8080  # 查看 8080 端口, 则可以结合 grep 命令
##################################################################
## lsof
# 如查看 8888 端口, 则在终端中输入:
sudo lsof -i:8888  # 一定要用 sudo 权限
# 这个命令也可以查出是哪个 进程 在占用8888 端口; 若要停止使用这个端口的程序, 使用kill +对应的pid即可
##################################################################
## iptables
# CentOS 配置防火墙操作实例 (启、停、开、闭端口)
service   iptables status   # 查询防火墙状态
service   iptables stop     # 停止防火墙
service   iptables start    # 启动防火墙
service   iptables restart  # 重启防火墙
chkconfig   iptables off    # 永久关闭防火墙
chkconfig   iptables on     # 永久关闭后启用
# 查询具体规则
iptables -L -n  # -L 将结果现实到 chain 中, -n 数字形式显示 add port
# Chain INPUT (policy DROP)
# target     prot opt source               destination
# ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0
# ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0           state RELATED,ESTABLISHED
# ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           tcp dpts:6881:6882
# ACCEPT     udp  --  202.54.1.254         0.0.0.0/0           udp dpt:514
# ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0           tcp dpts:80 state NEW,RELATED,ESTABLISHED
# LOG        all  --  0.0.0.0/0            0.0.0.0/0           LOG flags 0 level 4
# DROP       all  --  0.0.0.0/0            0.0.0.0/0
# Chain FORWARD (policy ACCEPT)
# target     prot opt source               destination
# Chain OUTPUT (policy ACCEPT)
# target     prot opt source               destination
# ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0

# 显示 21 号端口被堵塞
# 添加俩个 iptables moudle
modprobe ip_conntrack
modprobe ip_conntrack_ftp
# Iptables Open FTP Port 21 and 20 # for aliyun 6条命令
iptables -A INPUT -p tcp -s 0/0 --sport 1024:65535 -d 115.28.247.19 --dport 21 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp -s 115.28.247.19 --sport 21 -d 0/0 --dport 1024:65535 -m state --state ESTABLISHED -j ACCEPT
# reload
iptables -A INPUT -p tcp -s 0/0 --sport 1024:65535 -d 115.28.247.19 --dport 1024:65535 -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -p tcp -s 115.28.247.19 --sport 1024:65535 -d 0/0 --dport 1024:65535 -m state --state ESTABLISHED -j ACCEPT
# 20 号端口
iptables -A OUTPUT -p tcp -s 115.28.247.19 --sport 20 -d 0/0 --dport 1024:65535 -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p tcp -s 0/0 --sport 1024:65535 -d 115.28.247.19 --dport 20 -m state --state ESTABLISHED -j ACCEPT
# results
# Chain INPUT (policy ACCEPT)
# target     prot opt source               destination
# ACCEPT     tcp  --  0.0.0.0/0            115.28.247.19        tcp spts:1024:65535 dpt:21 state NEW,ESTABLISHED
# ACCEPT     tcp  --  0.0.0.0/0            115.28.247.19        tcp spts:1024:65535 dpts:1024:65535 state RELATED,ESTABLISHED
# ACCEPT     tcp  --  0.0.0.0/0            115.28.247.19        tcp spts:1024:65535 dpt:20 state ESTABLISHED
#
# Chain FORWARD (policy ACCEPT)
# target     prot opt source               destination
#
# Chain OUTPUT (policy ACCEPT)
# target     prot opt source               destination
# ACCEPT     tcp  --  115.28.247.19        0.0.0.0/0            tcp spt:21 dpts:1024:65535 state ESTABLISHED
# ACCEPT     tcp  --  115.28.247.19        0.0.0.0/0            tcp spts:1024:65535 dpts:1024:65535 state ESTABLISHED
# ACCEPT     tcp  --  115.28.247.19        0.0.0.0/0            tcp spt:20 dpts:1024:65535 state RELATED,ESTABLISHED
