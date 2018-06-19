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


from bisect import bisect_right

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n =3
def merges(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    nums1 = nums1[:m]
    for i in nums2:
        nums1.insert(bisect_right(nums1, i), i)
    print nums1


print range(2, 2)