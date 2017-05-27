#!/usr/bin/python3
# coding: utf-8
import sys, os, time, random
##################################################################
# Fork
print('fork: \nProcess (%s) start...' % os.getpid())
pid = os.fork()  # fork 轻松创建子进程
if pid == 0:  # 子进程返回 0, 父进程返回子进程的 id, getppid() 得到父进程 pid
    print('I am child process (%s) and my parent is (%s).' % (os.getpid(), os.getppid()))
    exit(0)  # 子进程执行打这里就退出, 不执行后面的
else: print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
##################################################################
# multiprocessing Process
from multiprocessing import Process # fork 无法在 Windows 上运行, Process 可以跨平台
def run_proc(name): print('Run child process %s (%s)...' % (name, os.getpid()))  # 子进程要执行的代码
print('\nProcess: \nParent process (%s).' % os.getpid())
p = Process(target=run_proc, args=('test',))  # 参数在 args 中传
p.start()  # start() 方法启动, 这样创建进程比 fork() 还要简单
p.join()  # join() 方法可以等待子进程结束后再继续往下运行, 通常用于进程间的同步
##################################################################
# Pool time
from multiprocessing import Pool  # 在 Process 基础上启动大量子进程
# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time(); time.sleep(random.random() * 3)
#     end = time.time(); print('Task %s runs %0.2f seconds.' % (name, (end - start)))
# print('\nPool: \nParent process %s.' % os.getpid())
# p = Pool(4)  # 大小为 4 的线程池, 所以下面 前4个 进程特别快就生成了, 第5个 需要等其中一个运行完
# for i in range(5): p.apply_async(long_time_task, args=(i,))
# p.close()  # 调用 close() 之后就不能继续添加新的 Process 了
# p.join()  # Pool 对象调用 join() 方法会等待所有子进程执行完毕, 调用 join() 之前必须先调用 close()
##################################################################
# subprocess
import subprocess  # 启动一个子进程, 然后控制其输入和输出
print('\nsubprocess 没有控制输入输出: \n$ nslookup www.python.org')  # 不用控制的
r = subprocess.call(['nslookup', 'www.python.org']); print('Exit code:', r)
print('\nsubprocess 控制输入输出: $ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')  # 相当于下面三条命令: set q=mx; python.org; exit
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
p = subprocess.Popen(['nslookup'], stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
p.wait()  # 加上这句话才能在终端等待输入...
p.kill()
print(p.returncode)  # 手动结束的话不会执行到这里, 执行到 kill() 后就会报错 KeyboardInterrupt
