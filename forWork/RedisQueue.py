# coding:utf-8
import redis
import re
import json
import time
from datetime import datetime, date


#  （1）任务队列支持避免重复任务插入      Done
#      方案：1、是否去重为可选参数；
#           2、每次push任务的时候先set()去重；
#           3、每次push任务把任务也同时添加redis中set的数据结构中
#  （2）获取任务数量                   Done
#  （3）通过装饰器来实现队列任务
#  （4）任务持久化（保存在硬盘？）


class ExpandJsonEncoder(json.JSONEncoder):
    '''
        采用json方式序列化传入的任务参数，而原生的json.dumps()方法不支持datetime、date
    '''
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


class RedisQueue:

    def __init__(self):
        self.redis_connect = redis.Redis()

    def get_len(self, key):
        keys = self.get_keys(key)
        # 每个键的任务数量
        key_len = [(k, self.redis_connect.llen(k)) for k in keys]
        # 所有键的任务数量
        task_len = sum(dict(key_len).values())
        return task_len, key_len

    def get_keys(self, key):
        # redis中所有的键
        keys = self.redis_connect.keys()
        # 找出符合的键
        keys = [k for k in keys if re.match(key+'-\d+', k)]
        # 按优先级将键降序排序
        keys = sorted(keys, key=lambda x: int(x.split('-')[-1]), reverse=True)
        return keys

    def set_task(self, key, tasks):
        # 将不在原来redis队列中的数据过滤出来
        return [t for t in tasks if not self.redis_connect.sismember(key, t)]

    def push_task(self, key, tasks, repeat=True, level=1):
        '''
        :param repeat: 是否允许重复，默认True(允许重复数据)
        :param level: 优先级(int类型)，数值越大优先级越高，默认1
        :return: 任务队列任务数量
        '''
        # 重新定义优先队列的key
        new_key = key + '-' + str(level)
        # 序列化任务参数
        tasks = [json.dumps(t, cls=ExpandJsonEncoder) for t in tasks]

        if not repeat:
            tasks = self.set_task(key, tasks)

        print 'RedisQueue info > the number of push tasks:', len(tasks)

        if not tasks:
            return self.get_len(key)

        # 将任务同时保存在redis的集合(set)中
        self.redis_connect.sadd(key, *tasks)
        # 双端队列，左边推进任务
        self.redis_connect.lpush(new_key, *tasks)
        return self.get_len(key)

    def pop_task(self, key, repeat=True, num=1):
        while True:
            # 双端队列 右边弹出任务
            # 小知识点：brpop() 接收两个参数，默认timeout为0，这样当队列为空会永远等下去
            keys = self.get_keys(key)
            if keys:
                ret = self.redis_connect.brpop(keys)
                return json.loads(ret[1])
            time.sleep(2)


if __name__ == '__main__':
    task_obj = RedisQueue()

    # 把任务推入redis 队列
    lst = [i for i in xrange(50, 400)]
    # task_obj.redis_connect.sadd('task', *lst)
    print task_obj.push_task('task', lst, repeat=False, level=9)

    # 从redis queue取出任务
    # while True:
    #     print task_obj.pop_task('task')
    #     time.sleep(0.1)

    count, key_len = task_obj.get_len('task')
    print key_len
