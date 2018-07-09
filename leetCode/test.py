# coding:utf-8
import re
from collections import Counter, defaultdict
from itertools import groupby
from operator import itemgetter, getitem

# max、min key
# itemgetter, getitem
# heapq  对比 pandas

dct = {'B': 2, 'A': 1, 'G': 0}

print max(dct.items(), key=itemgetter)
print max(dct)

# max、min妙用
lst = ['abc', 'za', 'xyzd']
# 获取lst中最长字符串
max(lst, key=len)

# operator.itemgetter
print itemgetter(1, 3, 5)('ABCDEFG')


