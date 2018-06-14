# coding:utf-8
from functools import partial
from itertools import groupby

import itertools

import re


def func(ss):
    lst = []
    temp = ''
    s_len = len(ss)
    for i, s in enumerate(ss):
        if temp == '' or temp[0] == s:
            temp += s
            if i+1 == s_len:
                lst.append(temp)
        else:
            lst.append(temp)
            temp = s
            if i+1 == s_len:
                lst.append(temp)
    print lst
    res = ''.join(map(lambda x: str(len(x))+x[0], lst))
    return res

print func('111221')


ss = '111221'
def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + digit
                    for digit, group in itertools.groupby(s))
    return s

for digit, group in itertools.groupby('111221'):
    print digit, group
    print list(group)

print re.findall(r'((.)\2*)', ss)
def fun(n):
    s = '1'
    for _ in range(n - 1):
        s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    return s

import pdir


def repeatedSubstringPattern(str):
    """
    :type str: str
    :rtype: bool
    """
    if not str:
        return False

    # print (str + str)
    ss = (str + str)[1:-1]
    # print ss
    return ss.find(str) != -1

print repeatedSubstringPattern('abcabcabc')
# abab abcabc aaa abcabcab

# abab
# abababab
# bababa

# abcabcd  str
# abcabcdabcabcd  str + trs
# bcabcdabcabc  ss
ss = 'abcabcabc'
# print re.findall(r'(.)\1*', ss)
from string import uppercase
def titleToNumber(s):
        """
        :type s: str
        :rtype: int
        """
        s = reversed(s.upper())
        print uppercase
        dct = {v:k for k, v in enumerate(uppercase, start=1)}
        return sum([(26**idx)*dct[i] for idx, i in enumerate(s)])

# print titleToNumber('ZY')

lst = [1, 2, 2, 2, 3, 4, 5]

def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ret = [i for i in nums if i != val]
        return ret, len(ret)


# print removeElement([3,2,2,3, 2, 3, 4, 5], 3)

nums = [3, 2, 4]
target = 6
from copy import copy
for idx, i in enumerate(nums):
    ret = (target - i)
    temp = copy(nums)
    temp.pop(idx)
    if ret in temp: 
        return [idx, temp.index(ret) + 1] if ret == i else [idx, nums.index(ret)]

