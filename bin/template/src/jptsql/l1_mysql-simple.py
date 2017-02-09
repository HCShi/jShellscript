#!/usr/bin/python
# coding: utf-8
# sudo apt install ython3-mysqldb
import MySQLdb as mdb
db = mdb.connect(host='127.0.0.1', user='root', password='root', db='myapp')
cursor = db.cursor()                      # 创建游标
cursor.execute('select name from users')  # 执行 sql 语句
result = cursor.fetchall()                # 获得返回的结果
cursor.close()
db.close()  # db.commit() 查询不用提交, 增删改需要 commit
