# coding:utf-8
import redis
import time

#  任务扔进redis队列  需要不需要序列化（意味着取出来也需要反序列化） （丢任务，优先级） 任务丢到111服务器 大家从111上拉取
#  从redis拉取任务（考虑线程安全）
# 高级：如何监听redis 是否有任务，工人便开始工作
# 连接池实现？
# http://blog.csdn.net/kwsy2008/article/details/48372665

class Tasks:
	def __init__(self):
		self.redis_connect = redis.Redis()

	def push_task(self, key, tasks):
		self.redis_connect.lpush(key, *tasks)  # 双端队列，左边推进任务
		return self.get_len(key)

	def pop_task(self, key, num=1):
		return self.redis_connect.brpop(key), self.get_len(key)  # 双端队列 右边弹出

	def get_len(self, key):
		return self.redis_connect.llen(key)


if __name__ == '__main__':
	task_obj = Tasks()

	# lst = ['task'+str(i) for i in xrange(1, 1001)]
	# task_obj.push_task('task', lst)

	while True:
		print task_obj.pop_task('task')
		time.sleep(1.5)
	#
	# print task_obj.get_len('task')

