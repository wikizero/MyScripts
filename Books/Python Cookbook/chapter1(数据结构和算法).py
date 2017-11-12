# coding:utf-8

'''
Python Cookbook version: 3

'''

# (1) 解压赋值可以使用在任何可迭代的对象上，不仅限于列表，如：字符串、文件对象、迭代器、生成器等
# 使用星号表达式减少变量 Python 3.0以上支持
# grades = [1, 2, 3, 4, 5]
# start, *ign, end = gra、des

# (2)deque 只保留有限的几个元素的历史记录
from collections import deque

dq = deque(maxlen=5)
for i in xrange(1, 20):
	dq.append(i)
print dq
# deque 可以支持左右push和pop，还支持最大队列数量

# (3) headq 从集合中获取最大或最小的n个元素  n=1的时候直接用max、min
import heapq
from operator import getitem

lst = [7, 2, 3, 4, 9, 1]
print heapq.nlargest(3, lst)  # 按大到小排序
print heapq.nsmallest(3, lst)  # 按小到大排序
# Transform list into a heap 堆数据结构重要特征是heap[0]元素永远是最小的
heapq.heapify(lst)
# 还可以使用key，对字典、元组排序
dct = [('A', 10), ('B', 5), ('C', 4), ('D', 18)]
print heapq.nsmallest(3, dct, key=lambda x: x[1])
# 更高级点的列子
portfolio = [
	{'name': 'IBM', 'shares': 100, 'price': 91.1}, {'name': 'AAPL', 'shares': 50, 'price': 543.22},
	{'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75},
	{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print heapq.nlargest(3, portfolio, key=lambda x: x['price'])  # 最贵的三个
from operator import itemgetter
print heapq.nlargest(3, portfolio, key=itemgetter('price', 'name'))  # 不用lambda并且按多个排序
print heapq.nlargest(3, portfolio, key=lambda x: (x['price'], x['name']))  # 最贵的三个

# (4)一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维 护着另外一个链表
# 字典的value进行排序
prices = {
	'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75
}
print dict(zip(prices.values(), prices.keys()))  # 字典反转
print min(zip(prices.values(), prices.keys()))  # 默认一些数学运算都会作用于键，比如直接min(prices)
print sorted(zip(prices.values(), prices.keys()))
# 合并字典
dct = {'A': 1, 'B': 2}
print dict(prices.items() + dct.items())

# (5) 去重
# 列表的列表如何快速去重？
lst2 = [[1, 2], [1, 2], [2, 3]]

# (6) 切片命名 方便阅读
connect = '192.168.1.1:8080'
ip = slice(0, 11)
port = slice(12, 16)
print connect[ip], connect[port]

# (7) groupby 分组
# groupby() 函数扫描整个序列并且查找连续相同值 (或者根据指定key函数返回值相同) 的元素序列，所以先要排序
rows = [
	{'address': '5412 N CLARK', 'date': '07/01/2012'}, {'address': '5148 N CLARK', 'date': '07/04/2012'},
	{'address': '5800 E 58TH', 'date': '07/02/2012'}, {'address': '2122 N CLARK', 'date': '07/03/2012'},
	{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}, {'address': '1060 W ADDISON', 'date': '07/02/2012'},
	{'address': '4801 N BROADWAY', 'date': '07/01/2012'}, {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}, ]

from operator import itemgetter
from itertools import groupby
rows.sort(key=itemgetter('date'))  # 先排序，再分组
for date, iterm in groupby(rows, key=itemgetter('date')):
	print date
	for i in iterm:
		print i
# 不关心（date）顺序，则可以用下面的分组方式，而且速度更快
from collections import defaultdict
import pprint
rows_by_date = defaultdict(list)
for row in rows:
	rows_by_date[row['date']].append(row)
pprint.pprint(rows_by_date)

# (8) 习惯用生成器表达式代替列表生成式，特别在数据量大的情况
print [i**2 for i in xrange(100)]
print (i**2 for i in xrange(100))  # 生成器表达式

# itertools 模块 compress函数

# (9) 生成器表达式参数在某些函数上直接传递(min,max,sum,any,all...)
lst = [1, 3, 5, 7, 9]
print sum(x**2 for x in lst)  # 平方和
import os
files = os.listdir('xxx')
any(name.endswith('.py') for name in files)  # 判断是否存在Python文件

# (10) 字典合并
a = {'x': 1, 'y': 2}
b = {'z': 4, 'w': 3}
a.update(b)  # print a
# 或者
dict(a.items() + b.items())
