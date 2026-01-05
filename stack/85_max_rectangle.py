"""
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
示例 2：

输入：matrix = [["0"]]
输出：0
示例 3：

输入：matrix = [["1"]]
输出：1
"""
from typing import List
def maximalRectangle(matrix: List[List[str]]) -> int:
    # 这是 84 题的原题代码，直接搬过来作为 helper function
    def largestRectangleArea(heights: List[int]) -> int:
        heights = [0] + heights + [0] # 哨兵技巧
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                h_idx = stack.pop()
                width = i - stack[-1] - 1
                max_area = max(max_area, heights[h_idx] * width)
            stack.append(i)
        return max_area


    if not matrix: return 0
    n = len(matrix[0])
    heights = [0] * n  # 初始化高度数组，相当于把二维压扁成一维
    max_matrix_area = 0

    # 逐行遍历
    for row in matrix:
        for i in range(n):
            if row[i] == "1":
                heights[i] += 1  # 累加高度
            else:
                heights[i] = 0   # 遇到 0，柱子断裂，高度重置
        # 每一行更新完后，都调用一次 84 题的逻辑
        current_layer_max = largestRectangleArea(heights)
        max_matrix_area = max(max_matrix_area, current_layer_max)

    return max_matrix_area