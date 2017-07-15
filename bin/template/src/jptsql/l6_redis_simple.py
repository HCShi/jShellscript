#!/usr/bin/python3
# coding: utf-8
# 内存数据库(可以存盘), 高性能的 key-value 数据库(同时还提供 list, set, zset, hash 等数据结构的存储)
# redis 连接实例是线程安全的, 可以直接将 redis 连接实例设置为一个全局变量, 直接使用
# 需要另一个 Redis 实例 (or Redis数据库) 时, 重新创建 redis 连接实例来获取一个新的连接, python 的 redis 没有实现 select 命令
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('name', 'jrp')  # 如果已经存在 key, 会覆盖, 好喜欢~
r.set('sex', 'male')
print(r.get('name'), r['name'])  # b'jrp'
print(r.keys(), r.dbsize())  # [b'sex', b'name'], 2
r.delete('sex')
r.save()  # 执行 "检查点" 操作, 将数据写回磁盘, 保存时阻塞
print(r.get('sex'))  # None
r.flushdb()
print(r.get('name')) # None

