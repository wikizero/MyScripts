# coding: utf-8
'''
input 
[2,4,3]
[5,6,4]

output:
[7, 0, 8]
(计算器输入方式)
'''

l1 = [2,4,3]
l2 = [5,6,4]
def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = map(str, l1[::-1])
        l2 = map(str, l2[::-1])
        return list(str(int(''.join(l1))+int(''.join(l2))))[::-1]

print addTwoNumbers(l1, l2)