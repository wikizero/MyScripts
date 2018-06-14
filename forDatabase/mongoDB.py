# coding:utf-8
'''

（1）新建项目   重命名项目、删除项目
（2）新建版本， 版本信息, 修改版本信息，删除版本
（3）新建模块   删、改
（4）新建接口，  json数据跟接口绑定  删改
（5）查询树形结构数据

***
  https://docs.mongodb.com/manual/reference/operator/update/pop/  (官方文档教程很好)

 版本名字必须不重名

解决方案：
 1、save方法可以实现特殊更新  先做一个对interface数组进行增删改的函数（判断工作量）

 2、树结构  如何在节点绑定信息？？？

 3、文件存储  加载慢 -- 是否可以实现懒加载解决？？？
***


mongoDb
﻿{
    "_id" : ObjectId("5b1531d6a473a47c20b54473"),
    "project" : "CEM基线版",
    "version" : [
        {
            "prefix" : "baseLine-c03",
            "name" : "v100R001C03",
            "desc" : "这是版本描述信息......"
        },
        {
            "prefix" : "baseLine-c05",
            "name" : "v100R001C05",
            "desc" : "这是版本描述信息c05......"
        }
    ]
}

'''
from pymongo import MongoClient
from bson import ObjectId

conn = MongoClient()
db = conn.test


# base  api
def db_save(col_name, data):
    try:
        print db[col_name].insert(data)
    except Exception, e:
        print e


dct = {
    'project': 'CEM基线版',
    'version': [
        {
            'name': 'v100R001C03',
            'prefix': 'baseLine-c03',
            'desc': '这是版本描述信息......',
            'modules': [
                {
                    'name': '业务质量定界',
                    'interface': ['id1', 'id2', 'id3', 'id4']
                },
                {
                    'name': '网络业务质量查询',
                    'interface': ['id1', 'id2', 'id3']
                },
                {
                    'name': '宽带质量查询',
                    'interface': ['id1', 'id2', 'id3']
                },
            ]
        },
    ]
}

api = {
    '_id': 'id1',
    'url': '',
    'name': '',
    'desc': '',
    'comment': '',
    'parameters': {
        'serverType': 'iptv',
        'query': {
            'name': 'test',
            'type': 'type1'
        }
    },
    'json': {
    }
}

# （1）
project = {
    'project': 'CEM基线版',
}
# ﻿5b1531d6a473a47c20b54473
# db_save('base', project)  # 新建项目信息

# db['base'].update_one({'_id': ObjectId('5b1531d6a473a47c20b54473')}, {'$set': {'project': 'CEM基线版本'}})  # 项目重命名

# db['base'].remove({'_id': ObjectId('5b152f9ca473a47b84a755bf')})   # 删除项目

# 新建版本
# version_info = {'name': 'v100R001C05',
#                 'prefix': 'baseLine-c05',
#                 'desc': '这是版本描述信息c05......', }
# ret = db['base'].update({'_id': ObjectId('5b1531d6a473a47c20b54473')}, {'$push': {'version': version_info}})
# print ret  # {'updatedExisting': True, u'nModified': 1, u'ok': 1.0, u'n': 1}   True表示更新成功


# 修改版本名字以及更新版本信息
# ret = db['base'].update({'_id': ObjectId('5b1531d6a473a47c20b54473'), 'version.name': 'v100R001C05'},
#                         {'$set': {'version.$.name': 'v100R001C06'}})

# 删除版本
# ret = db['base'].update({'_id': ObjectId('5b1531d6a473a47c20b54473')},
#                         {'$pull': {'version': {'name': 'v100R001C06'}}})

module = {
    'name': '业务质量定界'
}
# ret = db['base'].update({'_id': ObjectId('5b1531d6a473a47c20b54473'), 'version.name': 'v100R001C03'},
#                         {'$push': {'modules': module}})
# print ret
lst = range(10)
for i in range(0, len(lst), 2):
    print lst[i:i+2]