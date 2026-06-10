"""
73. 矩阵置零

给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

medium
"""
from typing import List
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m, n = len(matrix), len(matrix[0])
    row, col = [False] * m, [False] * n

    for i in range(m): # row
        for j in range(n): # col
            if matrix[i][j] == 0:
                row[i] = col[j] = True # mark
    
    for i in range(m): # row
        for j in range(n): # col
            if row[i] or col[j] == True: # need consider both
                matrix[i][j] = 0 # set zero