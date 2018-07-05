class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return reduce(lambda x, y: x^y, nums)
        return 2*sum(set(nums)) - sum(nums)
        