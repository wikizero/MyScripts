# coding:utf-8

'''
example:
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''

path = '../a/./b/../../c/./../d/r/t/q/w/../'
# path = "../a/../b/../../c/../u/"


def simplify_path(_path):
	lst = filter(lambda x: x.strip() and x != '.', _path.split('/'))
	ret = []
	for i in lst:
		if i == '..':
			if ret:
				ret.pop()
		else:
			ret.append(i)

	return '/'+'/'.join(ret)

print simplify_path(path)

lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
from collections import Counter  # map(lambda x: sorted(list(x)), lst)
print Counter(map(lambda x: ''.join(sorted(list(x))), lst))