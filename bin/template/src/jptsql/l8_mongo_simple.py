#!/usr/bin/python3
# coding: utf-8
import pymongo
client = pymongo.MongoClient()  # client = MongoClient('localhost', 27017); 连接到 MongoDB 的默认主机与端口
# client = MongoClient('mongodb://localhost:27017/')  # URL 格式

# db = client.test_database  # 没有的会创建, 初始为空, show dbs 查不到
# db = client("test-database")  # 可以通过属性或者字典的形式获取数据库
db = client["test-database"]  # 三种形式...

collection = db.test_collection
# collection = db["test_collection"]  # 也是两种方式

# 数据库以及集合都是延迟创建的, 不会在服务器端进行任何操作, 第一个文档插进去的时候, 它们才会被创建
##################################################################
## 增
post = { "author": "Mike",  # 采用 BSON 格式来表示和存储, BSON 格式是一种二进制的 JSON 格式; 在 PyMongo 中采用字典来表示文档
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": 13 }
collection = db.collection  # 获取一个 collection
result = collection.insert_one(post);
post_id = result.inserted_id; print(post_id)  # 592ae601421aa923827e98c0; insert_one() 返回一个 InsertOneResutl 实例
# 批量插入
posts = [{ "author": "Mike",
           "text": "Another post!",
           "tags": ["bulk", "insert"],
           "date": 14 },
         { "author": "Eliot",
           "title": "MongoDB is fun",
           "text": "and pretty easy too!",
           "date": 15 }]
result = collection.insert_many(posts)
print(result.inserted_ids)
##################################################################
## 查
## find()
print(collection.find_one())  # {'_id': ObjectId('592ae5ea421aa920fe72ea46')...}; 返回查询匹配到的第一个文档, 如果没有则返回 None
print(collection.find_one({"author": "Mike"}))  # 查找作者名为 "Mike" 的文档
# 根据 _id 查要用 ObjectId()
from bson.objectid import ObjectId
print(client.db.collection.find_one({'_id': post_id}))
print(client.db.collection.find_one({'_id': ObjectId(post_id)}))  # 竟然两个都查不到
# 批量查
for post in collection.find(): print(post)
for post in collection.find({"author": "Mike"}): print(post)
## 统计
print(db.collection_names(include_system_collections=False))  # ['collection']; 获取所有 collections
print(collection.count())  # 文档个数
print(collection.find({"author": "Mike"}).count())  # 匹配的文档数
## 高级查询
for post in collection.find({"date": {"$lt": 14}}).sort("author"): print(post)  # $lt 操作符实现范围查询, sort() 方法对查询到的结果进行排序
##################################################################
## 索引; 索引可以加快查询的速度
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)  # 创建一个唯一索引
print(list(db.profiles.index_information()))  # [u'user_id_1', u'_id_']
# 注意我们现在有两个索引了，一个在_id上，它由MongoDB自动创建，另外一个就是刚刚创建的索引了; 然后添加几个文档
user_profiles = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Ziltoid'}]
result = db.profiles.insert_many(user_profiles)  # 这个索引会阻止我们插入已经存在的 user_id
new_profile = {'user_id': 213, 'name': 'Drew'}
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
result = db.profiles.insert_one(new_profile)  # This is fine.
# result = db.profiles.insert_one(duplicate_profile)  # E11000 duplicate key error
