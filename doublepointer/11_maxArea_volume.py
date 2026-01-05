"""
11. 盛最多水的容器

给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

示例 1：

输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1
"""
from typing import List
def maxArea(height: List[int]) -> int:
    # 双指针，中心碰撞

    l,r = 0, len(height)-1
    max_volume = cur_volume = 0

    # volume = min_height * (r - l )

    while l < r:
        min_height = min(height[l], height[r])
        cur_volume = min_height * (r -l)
        max_volume = max(max_volume, cur_volume)

        # 哪边短，收缩哪边
        if height[l] >= height[r]:
            r -= 1
        else:
            l += 1

    return max_volume