# Linux下有很多强大网络扫描工具, 网络扫描工具可以分为: 主机扫描、主机服务扫描、路由扫描等
# nc, namp 是端口扫描(即主机服务扫描, namp同时有主机扫描的功能, 比较弱, 可以用 zenmap(GUI) 扫描主机, 同样也有些 Bug)
# fping 是主机扫描工具
##################################################################
## nc 端口扫描, Chat Server
##################################################################
nc -h 2>tmp  # 这个命令比较奇葩, 各种管道不好用, 2>tmp 就好用了
nc -h >tmp 2>&1  # 效果和上面相同
# 2>&1 causes stderr of a program to be written to the same file descriptor as stdout.
# nc writes to stderr by default, pipe will only get stdout hence grep will miss the data.

nc -vz localhost 1-2000 2>&1 | grep succeeded           # 检测本地那些端口开放, 本地好像不用设置时限, 不会卡住
nc -vz -w 1 baidu.com 80-100      # 1s 时限, 加快扫描, 否则会卡到 81 端口
nc -vz -w 1 115.28.247.19 80-100  # 扫描端口范围
nc -v 115.28.247.19 80           # 会阻塞等待用户输入请求
nc -vz 115.28.247.19 80          # 只是显示服务器的 80 端口有没有开
# -z 参数告诉netcat使用0 IO,连接成功后立即关闭连接,  不进行数据交换, 来告诉 nc 报告开放的端口, 而不是启动连接
#   nc 命令中使用 -z 参数时, 你需要在主机名/ip 后面限定端口的范围和加速其运行
# -v 参数指使用冗余选项
# -vv 更加详细的信息
# -n 使用纯数字 IP 地址, 即不用 DNS 来解析 IP 地址
# -x addr[:port]	Specify proxy address and port
# -w 设置超时限制

# Chat Server
nc -l 1567  # 在1567端口启动了一个tcp 服务器, 所有的标准输出和输入会输出到该端口
# Chat Client, 另一个终端
nc 127.0.0.1 1567  # 可以开始聊天了

# git ssh代理 ~/.ssh/config
Host github.com
    User                    git
    ProxyCommand            nc -x localhost:1080 %h %p
nc -x localhost:1080 github.com 22  # 相当于翻译成这句话, 会显示 banner
nc github.com 22  # 也会显示 banner, 和上面的 Chat Client 效果差不多
nc github.com ssh  # 等同于 22

# sock 所有使用 C/S 模式的都可以用 类似的
nc -U /var/run/docker.sock  # netcat 进行 UDP 链接, -U 表示是 UDP, 后面是 docker 的 sock 地址
GET /info HTTP/1.1  # 紧接着在交互式的命令行中输入, 敲两次回车
GET / HTTP/1.1

# 获取 baidu 首页
nc -v www.baidu.com 80  # Connection to www.baidu.com 80 port [tcp/http] succeeded!
GET / HTTP/1.0  # 敲一次回车
Host: www.baidu.com  # 敲两次回车
# GET 表示一个读取请求, 将从服务器获得网页数据,
# / 表示 URL 的路径, URL 总是以 / 开头, / 就表示首页
# 最后的 HTTP/1.1 指示采用的 HTTP 协议版本是 1.1.
# 目前 HTTP 协议的版本就是 1.1, 但是大部分服务器也支持 1.0 版本, 主要区别在于 1.1 版本允许多个 HTTP 请求复用一个 TCP 连接, 以加快传输速度.
# 响应代码: 200 表示成功, 3xx 表示重定向, 4xx 表示客户端发送的请求有错误, 5xx 表示服务器端处理时发生了错误
# 响应类型: 由 Content-Type 指定
# HTTP 协议格式为： POST /PATH /1.1 /r/n Header1:Value  /r/n .. /r/n HenderN:Valule /r/n Body:Data

##################################################################
## nmap
##################################################################
nmap baidu.com -v
nmap 127.0.0.1 -v  # 域名, IP 扫描
nmap 127.0.0.1,2,3  # , 分隔, 扫描多个主机(127.0.0.2 响应好慢啊)
nmap 127.0.0.1-3  # 同上
nmap 127.0.0.1-100  --exclude 127.0.0.3  # 排除一些主机
nmap -A 127.0.0.1
# -A: Enable OS detection, version detection, script scanning, and traceroute. 提到了traceroute, 实在并无此内容, 删除之
# -O: Enable OS detection 会显示系统类型, -A 并不会显示

##################################################################
## fping
##################################################################
fping -asg 127.0.0.1/24  # 254 alive, 因为 loopback 一直都可以 ping 通
fping -asg 127.0.0.0/24  # 254 alive, .0 是网络号, 不会去 ping it
fping -asg 127.0.0.2/24  # 254 alive, 这里计算的是网段, 所以不用管最有一个. 后面的
fping -asg 124.18.125.0/24 > tmp  # 只会把能 ping 通的 IP 写入文件, 最后的统计信息会 print 出来
# -a show targets that are alive
# -s print final stats
# -g generate target list (only if no -f specified)
# -u show targets that are unreachable


