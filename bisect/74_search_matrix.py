"""
给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

 

示例 1：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    def get_r_c(ind, r, c):# 展平拆分下标ind
        i = ind // c 
        j = ind % c 
        return i,j

    row_nums, col_nums = len(matrix),len(matrix[0])
    l,r = 0, row_nums * col_nums-1

    while l <= r: # 二分开始，闭区间
        mid = (l + r) // 2
        i,j = get_r_c(mid, row_nums, col_nums)

        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            l = mid + 1
        else:
            r = mid - 1

    return False