##################################################################
## 输出正确的信息
ls > car
cat car  # 显示 car 文件内容
rm car  # 显示完毕...
##################################################################
## 输出错误信息
abcd 2> car
cat car  # 显示 car 文件内容
rm car  # 显示完毕...
##################################################################
## 混合输出
ls && abcd &> car  # 这个会分解成两个命令 ls 和 abcd &> car
cat car  # 显示 car 文件内容
rm car  # 显示完毕...
##################################################################
## 信息重定向
# 1) 默认地, 标准的输入为键盘, 但是也可以来自文件或管道 (pipe |)
# 2) 默认地, 标准的输出为终端 (terminal), 但是也可以重定向到文件, 管道或后引号 (backquotes `)
# 3) 默认地, 标准的错误输出到终端, 但是也可以重定向到文件
# 4) 标准的输入, 输出和错误输出分别表示为 STDIN, STDOUT, STDERR, 也可以用0, 1, 2来表示
# 5) 其实除了以上常用的 3 中文件描述符, 还有 3~9 也可以作为文件描述符; 3~9 你可以认为是执行某个地方的文件描述符, 常被用来作为临时的中间描述符
ls Destop Desktop 2>tmp           # 会显示正确的在终端, 错误的在 tmp
ls dektop Desktop 2>&1            # 错误重定向到标准输出, 错误和标准输出, & 和 > 之间不能有空格
ls dektop Desktop 3>&2 2>&1 1>&3  # 标准输出和错误输出的交换, 没什么卵用
ls dektop Desktop 2>&1 1>&2       # 不能实现标准输出和错误输出的交换; 因为 shell 从左到右执行命令, 当执行完 2>&1 后, 错误输出已经和标准输出一样的, 再执行 1>&2 也没有意义

ls dektop Desktop 2>&1 >tmp  # 错误输出到终端, 标准输出被重定向到文件 file
ls dektop Desktop >tmp 2>&1  # 标准输出被重定向到文件 file, 然后错误输出也重定向到和标准输出一样, 所以也错误输出到文件 file
# File descriptor 1 is the standard output (stdout).
# File descriptor 2 is the standard error (stderr).
# Here is one way to remember this construct (although it is not entirely accurate):
# at first, 2>1 may look like a good way to redirect stderr to stdout.
# However, it will actually be interpreted as "redirect stderr to a file named 1".
# & indicates that what follows is a file descriptor and not a filename. So the construct becomes: 2>&1.
