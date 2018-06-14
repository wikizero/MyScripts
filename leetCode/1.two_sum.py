# coding:utf-8
import copy
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         min_one = min(nums)
#         lst = copy.deepcopy(nums)
#         lst.remove(min_one)
#         min_two = min(lst)
#         return [nums.index(min_one), nums.index(min_two)]



# 有效方法
nums = [3, 2, 4]
target = 6
from copy import copy
for idx, i in enumerate(nums):
    ret = (target - i)
    temp = copy(nums)
    temp.pop(idx)
    if ret in temp: 
        print [idx, temp.index(ret) + 1] if ret == i else [idx, nums.index(ret)]
