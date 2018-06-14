# coding:utf-8
from itertools import groupby

# def func(s):
#     ret = ''
#     for k, v in groupby(s):
#         ret += str(len(list(v)))+str(k)
#     return ret


def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    s = '1'
    while n:
        temp = ''
        for k, v in groupby(s):
            temp += str(len(list(v)))+str(k)
        s = temp
        n -= 1
    return s


print countAndSay(5)

from bisect import bisect_left

# print bisect_left()
from collections import deque

dq = deque([1, 2, 3, 4, 5, 6, 7])
dq.rotate(3)
print list(dq)

lst = [1, 2, 3, 4, 5, 6, 7]
_len = len(lst) - 1
n = 3
while n:
    n -= 1
    _num = lst.pop(_len)
    lst.insert(0, _num)

print lst

dct = {
    'type': 'iptv',
    'filter': {
        'type': 'tv',
        'nums': {
            'num1': 90,
            'num2': {
                'n1': 1,
                'n2': 2
            }
        }
    },
    'params': [
        {
            'opt': 'create'
        },
        {
            'opt': [
                {'n1': 1},
                {'n2': 2}
            ]
        }
    ]
}

{
    'type': 'iptv',
    'filter.type': 'tv',
    'filter.nums': 90,
    'params.0.opt': 'create',
    'params.1.opt': 'modify',
}
from wrapcache import wrapcache


@wrapcache(timeout=10)
def func(dct):
    ret = {}
    for k, v in dct.items():
        k = str(k)
        if isinstance(v, dict):
            temp = {k+'.'+_k: _v for _k,  _v in func(v).items()}
            ret.update(temp)
        elif isinstance(v, list):
            temp = {k+'.'+_k: _v for _k, _v in func(dict(enumerate(v))).items()}
            ret.update(temp)
        else:
            ret[k] = v
    return ret


print func(dct)

{
    'params.1.opt.1.n2': 2,
    'filter.nums.num2.n2': 2,
    'params.0.opt': 'create',
    'params.1.opt.0.n1': 1,
    'type': 'iptv',
    'filter.nums.num2.n1': 1,
    'filter.nums.num1': 90,
    'filter.type': 'tv'
}
