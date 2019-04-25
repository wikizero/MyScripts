# coding:utf-8
from itertools import groupby

lst = [1, 2, 3, 5, 6, 7, 10, 12, 13]

# input:   lst
# output:  [[1, 2, 3], [5, 6, 7], [10], [12, 13]]

ret = []
for k, v in groupby(enumerate(lst), key=lambda x: x[1] - x[0]):
    ret.append([i[1] for i in v])

print(ret)