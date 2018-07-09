# coding:utf-8
from operator import mul


def uniquePaths(m, n):
    """
        解法为排列组合知识
    :type m: int
    :type n: int
    :rtype: int
    """
    factorial = lambda x: reduce(mul, range(1, x + 1))
    return factorial(m + n - 2) / (factorial(n - 1) * factorial(m - 1))


print uniquePaths(7, 3)
