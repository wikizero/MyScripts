from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dct = Counter(nums1) & Counter(nums2)
        ret = []
        for k, v in dct.items():
            ret += [k]*v

        return ret
