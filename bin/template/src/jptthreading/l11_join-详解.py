#!/usr/bin/python
#coding=utf-8
import threading
def counter(n):
    cnt = 0
    for i in range(n):
        for j in range(i): cnt += j;
    print(cnt)
if __name__ == '__main__':
    th = threading.Thread(target=counter, args=(1000,));  # 初始化一个线程对象, 传入函数 counter, 及其参数 1000
    th.start();  # 启动线程
    th.join();  # 主线程阻塞等待子线程结束
    # 需要注意的是 th.join() 这句, 这句的意思是主线程将自我阻塞, 然后等待 th 表示的线程执行完毕再结束, 如果没有这句, 运行代码会立即结束
    # join 的意思比较晦涩, 其实将这句理解成这样会好理解些 "while th.is_alive(): time.sleep(1)"
    # 虽然意思相同, 但是后面将看到, 使用 join 也有陷阱

