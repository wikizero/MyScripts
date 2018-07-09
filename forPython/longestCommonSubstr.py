# coding:utf-8
"""
    动态规划求解最长公共子串
    解法就是用一个矩阵来记录两个字符串中所有位置的两个字符之间的匹配情况，若是匹配则为1,否则为0。
    然后求出对角线最长的1的序列，其对应的位置就是最长匹配子串的位置。
"""
from pprint import pprint


def longestCommonSubstr(str1, str2):
    matrix = [[0] * (len(str1) + 1)] * (len(str2) + 1)  # 构造零矩阵

    max_len = 0  # 最长匹配长度
    p = 0  # 匹配位置
    for i, val1 in enumerate(str2):
        for j, val2 in enumerate(str1):
            if val1 == val2:
                matrix[i + 1][j + 1] = matrix[i][j] + 1  # 向前移一位防止 i-1 / j-1 带来的越界问题
                if matrix[i + 1][j + 1] > max_len:
                    max_len = matrix[i + 1][j + 1]
                    p = i + 1
    return str2[p - max_len:p]


str1 = 'tabcdfgsss'
str2 = 'sssabcdpp'
print longestCommonSubstr(str1, str2)

s = "babaddtattarrattatddetartrateedredividerb"
print longestCommonSubstr(s, s[::-1])
print "ddtattarrattatdd"