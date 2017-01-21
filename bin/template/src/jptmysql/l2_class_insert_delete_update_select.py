#!/usr/bin/python
# coding: utf-8
import MySQLdb as mdb
class Jsql():  # 数据库用的是 ~/github/jTemplate/database/mysql/example.sql 中的
    def __init__(self, host, name, passwd, dbname):
        self.conn = mdb.connect(host, name, passwd, dbname, charset="utf8")
        self.cur = self.conn.cursor()
    def __del__(self):
        if self.conn:
            self.conn.close()  # 一定要执行这个
    def select(self, command):
        self.cur.execute(command)
        return self.cur.fetchall()
    def insert(self, command):
        self.cur.execute(command)
        self.conn.commit()
    def delete(self, command):
        self.cur.execute(command)
        self.conn.commit()
    def update(self, command):
        self.cur.execute(command)
        self.conn.commit()
if __name__ == '__main__':
    msql = Jsql('127.0.0.1', 'root', 'root', 'myapp')
    cmd_select = 'select name from users'
    cmd_insert = "insert into users values (10, 'jrp', 20)"
    cmd_update = "update users set name='jrp', age=22 where id=10"
    cmd_delete = "delete from users where id=10"
    ress = msql.select(cmd_select)
    for res in ress:
        print res[0]
