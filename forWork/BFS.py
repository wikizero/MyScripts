# coding:utf-8
from collections import deque

# 无权重有向图

route = {
    'start': ['a', 'b', 'c'],
    'a': ['d'],
    'b': ['d', 'e'],
    'c': ['e', 'f'],
    'd': ['e', 'g'],
    'e': ['g', 'end'],
    'f': ['e', 'end'],
    'g': ['end'],
}

q = deque(['start'])

while q:
    item = q.pop()
    print item
    if item in route:
        sites = route[item]
        if 'end' in sites:
            print 'end'
            break
        else:
            q.extendleft(sites)


