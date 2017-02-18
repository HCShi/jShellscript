#!/usr/bin/python3
# coding: utf-8
# 因为只有使用者才能根据表的结构定义出对应的类来, 所有类只能动态定义, 所以要用到 metaclass
class Field(object):  # 负责保存数据库表的字段名和字段类型
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self): return '<%s:%s>' % (self.__class__.__name__, self.name)
class StringField(Field):
    def __init__(self, name): super().__init__(name, 'varchar(100)')
class IntegerField(Field):
    def __init__(self, name): super().__init__(name, 'bigint')
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model': return type.__new__(cls, name, bases, attrs)  # 排除掉对 Model 类的修改
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():  # 当前类 (比如User) 中查找定义的类的所有属性, 如果找到一个Field属性, 就把它保存到一个__mappings__的dict中
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys(): attrs.pop(k)  # 同时从类属性中删除该 Field 属性, 否则, 容易造成运行时错误 (实例的属性会遮盖类的同名属性)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致, 把表名保存到 __table__ 中, 这里简化为表名默认为类名
        return type.__new__(cls, name, bases, attrs)
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw): super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try: return self[key]
        except KeyError: raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value): self[key] = value
    def save(self):
        fields, params, args = [], [], []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
class User(Model):  # 定义类的属性到列的映射, metaclass 可以隐式地继承到子类, 但子类自己却感觉不到
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
# 编写 ORM 框架实现如下功能, 父类Model和属性类型StringField、IntegerField是由ORM框架提供的, 剩下的魔术方法比如save()全部由metaclass自动完成
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')  # 创建一个实例
u.save()  # 保存到数据库
