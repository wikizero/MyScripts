# coding:utf-8
import redis
import time
import re

#  任务扔进redis队列  需要不需要序列化（意味着取出来也需要反序列化） （丢任务，优先级） 任务丢到111服务器 大家从111上拉取
#  从redis拉取任务（考虑线程安全）
# 高级：如何监听redis 是否有任务，工人便开始工作
# 连接池实现？
# http://blog.csdn.net/kwsy2008/article/details/48372665

# 查询keys


class Tasks:
    def __init__(self):
        self.redis_connect = redis.Redis()

    def push_task(self, key, tasks, level=1):
        '''

        :param key:
        :param tasks:
        :param level: 优先级，数值越大优先级越高
        :return:
        '''
        key = key + '-' + str(level)  # 重新定义优先队列的key
        self.redis_connect.lpush(key, *tasks)  # 双端队列，左边推进任务
        return self.get_len(key)

    def pop_task(self, key, num=1):
        keys = self.redis_connect.keys()  # redis中所有的键
        keys = [k for k in keys if re.match(key+'-\d+', k)]  # 找出符合的键
        keys = sorted(keys, key=lambda x: int(x.split('-')[-1]), reverse=True)  # 按优先级将键排序
        for k in keys:
            if self.get_len(k) > 0:
                return self.redis_connect.brpop(k)
        # return self.redis_connect.brpop(key), self.get_len(key)  # 双端队列 右边弹出任务
        # 小知识点：brpop() 接收两个参数，默认timeout为0，这样当队列为空会永远等下去

    def get_len(self, key):
        return self.redis_connect.llen(key)


if __name__ == '__main__':
    task_obj = Tasks()

    # lst = ['task'+str(i) for i in xrange(20, 30)]
    # task_obj.push_task('task', lst, level=5)

    while True:
        print task_obj.pop_task('task')
        # time.sleep(0.5)

    # print task_obj.get_len('task')

    # task_obj.pop_task('task')

