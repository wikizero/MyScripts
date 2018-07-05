from itertools import groupby
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        
        n -= 1
        
        while n:
            temp = ''
            for k, v in groupby(s):
                temp += str(len(list(v)))+str(k)
            s = temp
            n -= 1
        return s
