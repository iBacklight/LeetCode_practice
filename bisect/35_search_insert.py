"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。 Easy level

standard binary lookup.
"""
from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    n = len(nums)
    l = 0
    r = n-1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1

    return l