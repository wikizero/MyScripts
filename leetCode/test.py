# coding:utf-8
import re
from collections import Counter

dct = Counter([1, 2]) & Counter([1, 2])
print dct
ret = []
for k, v in dct.items():
    ret += [k]*v

print ret