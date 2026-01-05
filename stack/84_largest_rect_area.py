"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10

输入： heights = [2,4]
输出： 4
"""
def largestRectangleArea(self, heights: List[int]) -> int:
    # 技巧：首尾加 0 (哨兵)
    # 左边的 0 防止栈空，右边的 0 强迫所有元素出栈计算
    heights = [0] + heights + [0]
    stack = [] # 存索引
    max_area = 0
    for i, h in enumerate(heights):
        # 循环条件：当前高度 < 栈顶高度
        # 说明栈顶那个柱子遇到了右边的“矮子”，无法延伸了，必须结算！
        while stack and h < heights[stack[-1]]:
            # 核心逻辑：弹栈，算面积
            cur_height_index = stack.pop()
            cur_height = heights[cur_height_index]
            # 此时：
            # i 是cur_height_index右边界 (right boundary) -> 第一个比它矮的
            # stack[-1] 是左边界 (left boundary) -> 栈里剩下的那个肯定是比它矮的
            left_boundary = stack[-1]
            right_boundary = i
            # 宽度计算公式：(右 - 左 - 1), 即面积最多延伸到两边边界（两百年第一个小的数）的上一个
            # 这样可以保证最大化面积
            width = right_boundary - left_boundary - 1
            max_area = max(max_area, cur_height * width)

        #满足单调递增，入栈
        stack.append(i)
    return max_area