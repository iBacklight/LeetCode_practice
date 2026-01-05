"""
给你一个按照非递减顺序排列的整数数组 nums,和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target,返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

 

示例 1:

输入:nums = [5,7,7,8,8,10], target = 8
输出:[3,4]
示例 2:

输入:nums = [5,7,7,8,8,10], target = 6
输出:[-1,-1]
示例 3:

输入:nums = [], target = 0
输出:[-1,-1]


"""
from typing import List
def searchRange_halfopen(nums: List[int], target: int) -> List[int]: # 半开区间

    # 似乎要先找到taget,再在左右继续寻找相邻节点
    
    n = len(nums)
    if n == 0:
        return [-1, -1]

    # 找到第一个 >= target 的下标
    def lower_bound(x: int) -> int:
        l, r = 0, n  # 半开区间 [l, r)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= x:
                r = mid
            else:
                l = mid + 1
        return l  # 可能等于 n（越界,表示都 < x）

    # 找到第一个 > target 的下标
    def upper_bound(x: int) -> int:
        l, r = 0, n  # 半开区间 [l, r)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > x:
                r = mid
            else:
                l = mid + 1
        return l  # 可能等于 n
    """
    two functions 的差别就在于:

    一个用 >=

    一个用 >

    含义区别
    函数	        条件	    目标	                举例说明
    lower_bound	   >= x	   找 第一个 >= x 的位置	第一次遇到 x 或比 x 大的地方
    upper_bound	   > x	   找 第一个 > x 的位置	    跳过所有等于 x 的地方
        """
    left = lower_bound(target)
    # 若 left 越界或不是 target,说明不存在
    if left == n or nums[left] != target:
        return [-1, -1]

    right = upper_bound(target) - 1
    return [left, right]



def searchRange_closed(nums: List[int], target: int) -> List[int]: # 全闭空间
    # 似乎要先找到taget,再在左右继续寻找相邻节点
    
    n = len(nums)
    if n == 0:
        return [-1, -1]

    # 找到第一个 >= target 的下标
    def lower_bound(x: int) -> int:
        l, r = 0, n-1  # 全闭区间 [l, r]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= x:
                r = mid-1
            else:
                l = mid + 1
        return l  # 可能等于 n（越界,表示都 < x）

    # 找到第一个 > target 的下标
    def upper_bound(x: int) -> int:
        l, r = 0, n-1  # 全闭区间 [l, r]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > x:
                r = mid-1
            else:
                l = mid + 1
        return l  # 可能等于 n

    left = lower_bound(target)
    # 若 left 越界或不是 target,说明不存在
    if left == n or nums[left] != target:
        return [-1, -1]

    right = upper_bound(target)-1
    return [left, right]


def searchRange_unifunction(nums: List[int], target: int) -> List[int]:
    if not nums: return [-1, -1]

    # 这是一个通用的找“左侧边界”的模版 (>= target 的第一个位置)
    def find_start(target_val):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target_val:
                l = mid + 1
            else:
                # nums[mid] >= target_val
                # 我们希望锁定左边界，所以即使相等，也要让 r 向左收缩
                r = mid - 1
        return l

    # 1. 找 target 的起始位置
    start_idx = find_start(target)

    # 校验 start_idx 是否越界，或者是否真的等于 target
    if start_idx == len(nums) or nums[start_idx] != target:
        return [-1, -1]

    # 2. 找 target 的结束位置
    # 技巧：找 (target + 1) 的左边界，它的前一个位置一定是 target 的结束位置
    # 例如 [5, 7, 7, 8, 8, 10], target=8
    # find_start(8) 返回下标 3 (第一个8)
    # find_start(9) 返回下标 5 (数字10的位置)
    # 结束位置 = 5 - 1 = 4
    end_idx = find_start(target + 1) - 1

    return [start_idx, end_idx]