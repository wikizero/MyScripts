# coding:utf-8
from itertools import groupby
from math import ceil
lst = [1,0,0,0,1,0,1,0, 0, 0, 0, 1, 1, 0, 1]

# i = 0
# max_len = 0
# temp = 0
# for k, v in groupby(lst):
#     i += 1
#     _len = len(list(v))
#     if k == 0 and max_len < _len:
#         max_len = _len
#         temp = i
# if temp == 1 or temp == i:
#     return max_len
# else:
#     return ceil(max_len/2)

from string import letters, digits

print letters + digits

