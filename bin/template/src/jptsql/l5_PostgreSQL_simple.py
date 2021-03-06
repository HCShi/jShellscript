#!/usr/bin/python3
# coding: utf-8
# PostgreSQL 是一個功能強大, 開源對象關係型數據庫係統. 它擁有超過 15 年的持續開發和業經驗證的架構, 具有良好的可靠性, 數據完整性和正確性.
# PostgreSQL 能夠運行在所有主流操作係統, 包括 Linux, UNIX (AIX, BSD, HP-UX, SGI IRIX, Mac OS X 上的 Solaris, Tru64 的) , 和 Windows.
# PostgreSQL 可以用 Python psycopg2 模塊集成.  sycopg2 是 Python 編程語言的 PostgreSQL 數據庫的適配器.  其程序代碼少, 速度快, 穩定.
import psycopg2  # 导入PostgreSQL驱动
try:
    # 连接数据库
    conn = psycopg2.connect(database='workspace', user='workspace',
                            password='123', host='127.0.0.1', port='5432')
    print ("Opened database successfully")
    # 创建游标
    cur = conn.cursor()
    # 创建user表
    cur.execute('''
    drop table if exists vo84_user
    ''')
    cur.execute('''
    create table vo84_user(
    id varchar(10) primary key,
    name varchar(20)
    )''')
    print ("Table created successfully")
    # 插入一行记录, 注意MySQL的占位符是%s:
    cur.execute('insert into vo84_user (id, name) values (%s, %s)', ['1', 'Michael'])
    # print(cur.rowcount)
    # 提交事务
    conn.commit()
    # 运行查询
    cur.execute('select * from vo84_user where id = %s', ('1',))
    values = cur.fetchall()
    print(values)
except Exception as e:
    print(e)
finally:
    # 关闭游标及断开数据库连接
    cur.close()
    conn.close()
