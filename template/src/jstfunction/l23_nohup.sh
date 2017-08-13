##################################################################
## nohup
# 无论是否将 nohup 命令的输出重定向到终端, 输出都将附加到当前目录的 nohup.out 文件中。
# 如果当前目录的 nohup.out 文件不可写, 输出重定向到 $HOME/nohup.out 文件中。
# 如果没有文件能创建或打开以用于追加, 那么 Command 参数指定的命令不可调用

nohup php test.php &  # 想在 vps 上运行一个 .php
nohup jupyter notebook --no-browser --matplotlib=inline > /dev/null 2>&1 &!
nohupzsh() { nohup ${*} > /dev/null 2>&1 &! }  # shellscript 中的一个命令
# nohup means: Do not terminate this process even when the stty is cut off.
# > /dev/null means: stdout goes to /dev/null (which is a dummy device that does not record any output).
# 2>&1 means: stderr also goes to the stdout (which is already redirected to /dev/null).
# You may replace &1 with a file path to keep a log of errors, e.g.: 2>/tmp/myLog
# & at the end means: run this command as a background task.
# ! is for zsh, in bash don't need !

# 思考: 问题 1 为什么 ssh 一关闭, 程序就不再运行了?

# 元凶: SIGHUP 信号
# 让我们来看看为什么关掉窗口/断开连接会使得正在运行的程序死掉。
# 在Linux/Unix中, 有这样几个概念:
#
# 进程组(process group): 一个或多个进程的集合, 每一个进程组有唯一一个进程组 ID, 即进程组长进程的 ID
# 会话期(session): 一个或多个进程组的集合, 有唯一一个会话期首进程(session leader), 会话期 ID 为首进程的 ID
#
# 会话期可以有一个单独的控制终端(controlling terminal)
# 与控制终端连接的会话期首进程叫做控制进程(controlling process)
# 当前与终端交互的进程称为前台进程组; 其余进程组称为后台进程组
#
# 根据 POSIX.1 定义:
# 挂断信号(SIGHUP)默认的动作是终止程序
# 当终端接口检测到网络连接断开, 将挂断信号发送给控制进程(会话期首进程)
# 如果会话期首进程终止, 则该信号发送到该会话期前台进程组
#
# 一个进程退出导致一个孤儿进程组中产生时, 如果任意一个孤儿进程组进程处于STOP状态,
# 发送 SIGHUP 和 SIGCONT 信号到该进程组中所有进程
# (关于孤儿进程参照: http://blog.csdn.net/hmsiwtv/article/details/7901711)
#
# 结论: 因此当网络断开或终端窗口关闭后, 也就是SSH断开以后, 控制进程收到SIGHUP信号退出, # 会导致该会话期内其他进程退出
# 简而言之: 就是 ssh 打开以后, bash 等都是他的子程序, 一旦ssh关闭, 系统将所有相关进程杀掉!!
