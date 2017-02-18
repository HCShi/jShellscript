#!/usr/bin/python3
# coding: utf-8
# 高级连接池就是一次构建实例的时候, 他会一次性创建出指定个数的链接对象, 然后会把这些链接对象放到队列里面, 会开一个线程专门去维护他们
# 该线程也会定时的去给服务端发送hello, 在redis里面是ping
# 另外, 连接池最好加入一个过期时间的概念, 比如10分钟内没人用, 或者是不管有没有人已经用过了, 我为了各种情况会把链接时间过长的链接给kill掉
# 关于这样的数据类型不能简单的用简单的列表队列了, 需要用有序队列
import MySQLdb
class PooledConnection:
    def __init__(self, maxconnections):  # 构建连接池实例
        from Queue import Queue
        self._pool = Queue(maxconnections)  # create the queue
        self.maxconnections = maxconnections
        for i in range(maxconnections): self.fillConnection(self.CreateConnection()) # 根据你给数目来创建链接, 并写入刚才创建的队列
    def fillConnection(self,conn): self._pool.put(conn)
    def getConnection(self): return self._pool.get()
    def ColseConnection(self,conn):
        self._pool.get().close()
    def CreateConnection(self):
        conndb = MySQLdb.connect(user='root', passwd='root', host='127.0.0.1', port=3306, db='test')
        conndb.clientinfo = 'datasync connection pool';
        conndb.ping();
mysqlpool = PooledConnection(10);
mysqlpool.getConnection()  # 获取连接
