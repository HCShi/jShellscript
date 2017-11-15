##################################################################
## 无法 ping www.baidu.com
# 先换成手机热点是一下是不是路由器加了防火墙

ping 127.0.0.1  # 如果能显示, 说明一下三种情况
tracepath www.baidu.com  # 查看是哪一跳被中断
# 1. You may be running a firewall that is discarding pings or ICMP (outbound or inbound)
# 2. There may be a router between the client and the server blocking or throttling pings or ICMP traffic
# 3. The host you are pinging may be set not to respond to pings or ICMP traffic
