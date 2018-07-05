from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        for i in range(len(nums)+1):
            ret += map(list, combinations(nums, i))
        return ret
