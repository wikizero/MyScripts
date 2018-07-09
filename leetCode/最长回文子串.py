# coding:utf-8

s = "adam"


def longestCommonSubstr(str1, str2):
    matrix = [[0] * (len(str1) + 1)] * (len(str2) + 1)  # 构造零矩阵

    ret = []
    for i, val1 in enumerate(str2):
        for j, val2 in enumerate(str1):
            if val1 == val2:
                matrix[i + 1][j + 1] = matrix[i][j] + 1  # 向前移一位防止 i-1 / j-1 带来的越界问题
                ss = str2[(i - matrix[i + 1][j + 1]):i + 1]
                if len(ss) > 1 and ss == ss[::-1]:
                    ret.append(ss)

    print ret
    return max(ret, key=len)


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    return longestCommonSubstr(s, s[::-1])


print longestPalindrome("babaddtattarrattatddetartrateedredividerb")

