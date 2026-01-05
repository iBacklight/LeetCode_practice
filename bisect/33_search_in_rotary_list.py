"""
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 向左旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 下标 3 上向左旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

mid level


"""
from typing import List

def search(nums: List[int], target: int) -> int:
    if not nums:
        return -1
    
    l, r = 0, len(nums) - 1
    # We can treat this as a two section, separated by the rotary point
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[0] <= nums[mid]: # mid droped in the first section
            if nums[0] <= target < nums[mid]: # target also droped in the first section, locked in
                r = mid - 1
            else:
                l = mid + 1 # so traget still got chance to the another section
        else: # mid droped in the second section
            if nums[mid] < target <= nums[len(nums) - 1]: # target also droped in the second section, locked in
                l = mid + 1
            else:
                r = mid - 1
    return -1


def search_2(nums: List[int], target: int) -> int:
    """
    虽然旋转后的数组整体不是单调的，但它是部分有序的。

    二分利用这个“有序性断点”定位到最小值，也就是旋转点。

    所以，二分不要求整个数组有序，只要能在每一步判断目标在那一侧，就能用二分。
    """
    n = len(nums)
    if n == 0:
        return -1
    # 1) 找旋转点（最小值下标）
    l, r = 0, n - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    rot = l  # 最小值的位置

    # 2) 选择有序区间做二分
    if nums[rot] <= target <= nums[-1]:
        l, r = rot, n - 1
    else:
        l, r = 0, rot - 1

    # 3) 常规二分
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1


