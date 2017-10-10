#!/bin/bash
##################################################################
## 信工所 二室 内容组 一台服务器, 开始 Hacking...; For CentOS Linux release 7.2.1511 (Core)
##################################################################
## 0. 基础查询
dmidecode | grep "Product Name"  # 查看机器型号
#        Product Name: P9X79-E WS
dmesg | grep -i eth              # 查看网卡信息; 这个有点乱
uname -a  # Linux localhost.localdomain 3.10.0-327.28.2.el7.x86_64 #1 SMP Wed Aug 3 11:11:39 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
# 竟然没有使用发行版
# Linux localhost 4.4.0-92-generic #115-Ubuntu SMP Thu Aug 10 09:04:33 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux  # 这是我主机上的系统
cat /proc/version / lsb_release -a  # CentOS; uname -a 竟然不好用
# 后来发现使用 yum 可以安装,  应该就是 Fedora/CentOS, 找时间在 Docker 中测试一下
free -m  # 32GB 内存, 但只能用 1.5G 左右; 用下面的命令确认一下
#               total        used        free      shared  buff/cache   available
# Mem:          31955         366        1402         145       30186       31142
# Swap:         63999          68       63931
grep MemTotal /proc/meminfo  # MemTotal:       32722216 kB
grep MemFree /proc/meminfo   # MemFree:         1436484 kB; 真的只分配每个人 2G 吗
cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c  # 8  Intel(R) Core(TM) i7-3820 CPU @ 3.60GHz
cat /proc/cpuinfo | grep physical | uniq -c  # 显示 8 个单核

hostname  # localhost.localdomain; 查看计算机名
uptime    # 查看系统运行时间、用户数、负载
# 15:06:03 up 39 days,  1:27,  8 users,  load average: 0.16, 0.07, 0.06
users  # 看看有哪些用户
w  # 查看当前活动用户; 看看大家都在干什么
##################################################################
## 1. ssh 公钥登录
ssh-copy-id -i ~/.ssh/id_rsa.pub zhangdongjie@159.226.95.132 -p 9999  # 添加公钥
ssh zhangdongjie@159.226.95.132 -p 9999  # 添加 alias
# 后来在自己用户里 ssh-copy-id 不好用, 直接将 id_ras.pub 扔进去了
##################################################################
## 2. 反向代理...
lab$ ssh -CNR 19999:localhost:9999 root@45.78.9.29 -p 28484  # 国外服务器, 太慢了, 等不下去了
lab$ ssh -CNR 19999:localhost:9999 root@116.196.120.62  # 京东云服务器
# 上面两种方法都不行, 因为服务器防火墙已经禁止了外网 IP, 以后再检查...
# 采用 lab_server(外网不能访问) <-> lab_router_os_openwrt <-> 京东云 <-> host, 这种架构才成功连接上, 具体参见 autossh
王长健实验室嵌入式路由器$ autossh -M 5678 -fCNR 12345:localhost:22 root@116.196.90.26  # 一定要提前设置好 路由器到京东云的 公钥登录
# 下面是测试
京东云$ netstat -ant  # 检查是否有 12345 端口在监听
京东云$ ssh localhost -p 12345  # 就可以连接到嵌入式路由器
##################################################################
## 2.1 正向连接; 本来是要三次 ssh 才能最终连接到 lab_server
# lab_server [159.226.95.132:9999] - lab_router [localhost:12345(京东云反向)] - 京东云 [116.196.120.62:22] - host
京东云$ ssh -fN -L 11111:159.226.95.132:9999 root@localhost -p 12345  # ssh 路由器, 将本地 11111 转向到 lab_server 的 9999
京东云$ ssh zhangdongjie@localhost -p 11111  # 此时在京东云上本地的 11111 就可以到 lab
# 接下来将 京东云 11111 映射到本地的
host$ ssh root@116.196.120.62 -fN -L 11112:localhost:11111  # 这里必须用 localhost, 指的是 116.196.120.62, 但不能写 IP...
host$ ssh zhangdongjie@localhost -p 11112  # 登录自己的 11112 的端口
##################################################################
## 3. 创建自己的用户
sudo adduser jiaruipeng
sudo passwd jiaruipeng  # hellojrp
groups  # 查看有哪些 group
sudo usermod -aG wheel jiaruipeng  # add the user to the wheel group; By default, on CentOS, members of the wheel group have sudo privileges
sudo usermod -aG root jiaruipeng  # wheel 并没有 root 权限...
grep jiaruipeng /etc/group  # 查看自己的 root 权限情况, root:x:0:jiaruipeng
su - jiaruipeng  # 可以切换到对应用户
visudo  # 在这个文件中修改可以添加 sudo 权限; 末尾添加下面内容
# jiaruipeng    ALL=(ALL)       ALL
# 还是不添加 sudo 权限了...
##################################################################
## -2. 权限问题
Only the owner which is ‘root’ user can edit the /etc/passwd file, not in the root’s group.
##################################################################
## -1. CentOS 坑记录
sudo yum install python34-tkinter  # On CentOS 7 and Python 3.4
sudo yum install python27-tkinter  # On CentOS 6.5 with python 2.7 I needed to do
