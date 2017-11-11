# coding:utf-8
import threading
from functools import wraps
import time
import random


# 装饰器 函数超时设置，并计算函数运行时间
# 待优化： 获取返回值  线程如何获取返回值
def decorator_timer(seconds):
	def outer(func):
		@wraps(func)
		def inner(*args, **kwargs):
			start = time.time()
			thread = threading.Thread(target=func, args=args, kwargs=kwargs)
			thread.start()
			thread.join(seconds)
			if thread.is_alive():
				thread._Thread__stop()
				msg = 'Timeout: {seconds} seconds'.format(seconds=seconds)
				return msg, False
			else:
				msg = time.time() - start
				return msg, True

		return inner

	return outer


@decorator_timer(seconds=5)
def test(a):
	print a
	time.sleep(random.randint(1, 10))
	print 'end test'


for i in xrange(10):
	print test(i)
	print '-'*20

