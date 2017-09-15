#!/bin/bash
# 建立两个内网 和 一个公网
docker network create --subnet=172.19.0.0/16 net19
docker network create --subnet=172.20.0.0/16 net20
docker network create --subnet=172.21.0.0/16 net21  # 公网
# 运行两台内网主机 和 一台公网主机
docker run -i -t --net net19 --ip 172.19.0.2 --name con19 coder352/ubuntu:16.04
docker run -i -t --net net20 --ip 172.20.0.2 --name con20 coder352/ubuntu:16.04
docker run -i -t --net net21 --ip 172.21.0.2 --name con21 coder352/ubuntu:16.04  # 公网
$ ifconfig && ping  # 分别查看, ping 发现不能相互连接
# 将公网主机分别和内网主机相连
docker network connect net21 con19  # 会添加 eth1(172.21.0.3) 的网卡
docker network connect net21 con20  # 会添加 eth1(172.21.0.4) 的网卡
# 只要 con21 不主动访问 con19 和 con20 就相当于两个内网了
