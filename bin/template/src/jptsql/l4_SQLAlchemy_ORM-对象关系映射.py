#!/usr/bin/python3
# coding: utf-8
# 这就是传说中的ORM技术: Object-Relational Mapping, 把关系数据库的表结构映射到对象上, 在 Python 中, 最有名的 ORM 框架是 SQLAlchemy
# 一个表映射成一个类, 一行映射为一个对象
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()                      # 创建对象的基类
class User(Base):                              # 定义 User 对象
    __tablename__ = 'user'                     # 表的名字
    id = Column(String(20), primary_key=True)  # 表的结构 id, name
    name = Column(String(20))
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test')  # 初始化数据库连接, 需要安装 python3-mysql.connector
DBSession = sessionmaker(bind=engine)                                           # 创建 DBSession 类型
# create database test && create table user (id varchar(20) primary key, name varchar(20))
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'

session = DBSession()                # 创建 session 对象, DBSession 对象可视为当前数据库连接
new_user = User(id='5', name='Bob')  # 创建新 User 对象
session.add(new_user)                # 添加到 session
session.commit()                     # 提交即保存到数据库
session.close()                      # 关闭 session

session = DBSession()                                  # 创建Session
user = session.query(User).filter(User.id=='5').one()  # filter 是 where 条件, 最后调用 one() 返回唯一行, 如果调用 all() 则返回所有行
print('type:', type(user))                             # 打印类型和对象的 name 属性
print('name:', user.name)
session.close()                                        # 关闭Session

# 一对多设计表
class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    books = relationship('Book')  # 一对多
class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    user_id = Column(String(20), ForeignKey('user.id'))  # "多"的一方的 book 表是通过外键关联到 user 表的
