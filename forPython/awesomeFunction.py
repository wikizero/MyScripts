# coding:utf-8
import bisect
from itertools import groupby

# 1、字典,集合,列表等等对象是不适合作为函数默认值的；
# 2、”is”是判断2个对象的身份, ==是判断2个对象的值
# 3、Python支持try-except-else（不抛异常执行else部分）, while-else（不break执行else部分）, for-else（不break执行else部分）,

# （1）bisect
lst = [1, 2, 5, 8, 10]
# 获取将某个插入一个有序列表中的位置（使用的算法：二分法）
print bisect.bisect_right(lst, 7)  # .bisect 相当于 .bisect_right 还有对应的 .bisect_left
# 直接插入一个元素
bisect.insort(lst, 7)  # print lst查看插入后的状态
# 举个栗子，获取对应分数的等级
get_grade = lambda x: 'FDCBA'[bisect.bisect_right([60, 70, 80, 90], x)]
print get_grade(78)  # 78分是等级是C


def groupby_(items, size):
    print [iter(items)] * size
    return zip(*[iter(items)] * size)


print groupby_([1, 2, 45, 7, 0, 9, 1, 5], 3)
from itertools import izip_longest, starmap

for i in izip_longest(*[iter([1, 2, 45, 7, 0, 9, 1, 5])] * 3, fillvalue=''):
    print i

# itertools详细介绍  http://outofmemory.cn/code-snippet/2390/python-itertools-module-learn-note
# starmap  对序列seq的每个元素作为func的参数列表执行, 返回执行结果的迭代器
for i in starmap(pow, [(2, 2), (3, 2)]):  # 4, 9
    print i

# 脚本性能分析 python -m cProfile my_script.py

# 列表展平
from compiler.ast import flatten
from itertools import chain

lst = [[1, 3], [2, 4], [4, 6]]
print flatten(lst)
print list(chain.from_iterable(lst))

# 列表推导式、字典推导式、集合推导式、生成器表达式
print {i for i in xrange(10)}
print (i ** 2 for i in xrange(10))
