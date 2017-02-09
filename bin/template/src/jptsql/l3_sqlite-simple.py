#!/usr/bin/python3
# coding: utf-8
# sqlite 是一个软件库 无服务器的 零配置的 是在世界上最广泛部署的SQL数据库引擎
# sqlite 的 .db 数据库 cat 打开能看到, vim 打开乱码
import os, sqlite3  # 导入 SQLite 驱动
conn = sqlite3.connect('test.db')  # 连接到SQLite数据库, 数据库文件是 test.db, 如果文件不存在, 会自动在当前目录创建
cursor = conn.cursor()             # 创建一个 Cursor, 通过游标执行 SQL 语句

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')  # 执行一条 SQL 语句, 创建 user 表

cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')           # 继续执行一条 SQL 语句, 插入一条记录
print(cursor.rowcount)  # 通过 rowcount 获得插入的行数
conn.commit()   # 提交事务

cursor.execute('select * from user where id=?', ('1',))  # ? 占位符
print(cursor.fetchall())  # 结果集是一个list, 每个元素都是一个tuple

cursor.close()  # 关闭 Cursor
conn.close()    # 关闭 Connection
os.remove('./test.db')  # 删除数据库, 否则老是报错
