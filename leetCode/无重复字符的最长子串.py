# coding:utf-8

s = "bpfbhmipx"


def lengthOfLongestSubstring(s):
    """
        41%
    :type s: str
    :rtype: int
    """
    _len = 0
    new = []
    for i in s:
        if i not in new:
            new.append(i)
        else:
            _len = max(_len, len(new))
            new = new[new.index(i) + 1:]+[i]

            print new

    return max(_len, len(new))



