# coding:utf-8

matrix = [
    [1, 2, 1],
    [3, 0, 1],
    [1, 1, 1]
]


# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    idxs = [idx for idx, row in enumerate(zip(*matrix)) if 0 in row]

    matrix[:] = [[0] * len(row) if 0 in row else row for row in matrix]
    matrix[:] = map(list, zip(*[[0] * len(row) if idx in idxs else row for idx, row in enumerate(zip(*matrix))]))
