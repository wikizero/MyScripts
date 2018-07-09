# coding:utf-8
from collections import defaultdict

# 字谜分组
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

maps = zip(map(lambda x: ''.join(sorted(x)), strs), strs)

ret = defaultdict(list)
for i, j in maps:
    ret[i].append(j)

print ret.values()
# [['tan', 'nat'], ['bat'], ['eat', 'tea', 'ate']]
