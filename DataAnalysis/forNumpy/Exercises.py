# coding:utf-8
import numpy as np

# https://developers.google.cn/machine-learning/crash-course/
# https://www.machinelearningplus.com/101-numpy-exercises-python/
# numpy优秀入门博客  http://blog.csdn.net/pipisorry/article/details/39235753

# numpy quick start
# 101 exercises :50
# 基础数学知识(google 基本要求)
# shell 了解

arr = np.arange(10)

a = np.array([1, 2, 3])
print np.hstack([np.repeat(a, 3), np.tile(a, 3)])

# 寻找多个序列中的相同的元素
print reduce(np.intersect1d, ([1, 3, 4, 3], [3, 1, 2, 1], [6, 3, 4, 2]))

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6, 0])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8, 0])

print np.where(a == b)

print np.nonzero(a == b)  # 非0元素的下标(True 1, False 0)

# a = np.arange(15)
# print a[(5 <= a) & (a <= 10)]
# print a[np.where((5 <= a) & (a <= 10))]


print np.vectorize(lambda x, y: max(x, y))(a, b)
# or
func_max = np.vectorize(lambda x, y: max(x, y))
print func_max(a, b)

arr1 = np.repeat(np.arange(1, 4), 3).reshape(3, -1)
print arr1
print arr1[[1, 0, 2], :]  # 行调换
print arr1[:, [1, 0, 2]]  # 列调换

print arr1[::-1, :]  # 行倒序
print arr1[:, ::-1]  # 列逆序

print np.random.randint(5, 10, (5, 3)) + np.random.random((5, 3))  # 5-10的随机浮点数
print np.random.uniform(5, 10, (5, 3))  # 5-10的随机浮点数

a = np.array([1, 2, 3, np.nan, 5, 6, 7, np.nan])
print a[~np.isnan(a)]

a = np.random.randint(5, 10, 10)
print a
print np.unique(a)
print np.unique(a, return_index=True)

lst1 = ['a', 'a', 'q', 'c', 'e', 'v', 1, 0, 8, 9, 0]
lst2 = ['a', 't', 'e', 'c', 'e', 't', 1, 0, 9, 4, 0]
lst3 = ['a', 'a', 't', 'c', 'e', 'p', 1, 0, 89, 5, 0]

# 算这三个列表的公共元素
print reduce(np.intersect1d, (lst1, lst2, lst3))
print reduce(lambda x, y: set(x) & set(y), (lst1, lst2, lst3))


