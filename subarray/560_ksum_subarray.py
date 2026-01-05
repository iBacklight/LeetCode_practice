"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。

示例 1:

输入:nums = [1,1,1], k = 2
输出:2
示例 2:

输入:nums = [1,2,3], k = 3
输出:2

双指针/滑动窗口算法不适用，因为无法保证数组非负。

双指针/滑动窗口”只在所有元素非负时才成立（窗口右扩和左缩才能单调地让和增/减）。一旦有负数，窗口和不再单调，双指针会漏数或死循环。因此这题不能用双指针做对。

反例说明“双指针不适用”

nums = [1, -1, 1], k = 1
有效子数组有:[1](idx0), [1, -1, 1](0..2), [1](idx2) → 共 3 个。
滑动窗口无法在含负数时保证不漏这三种，尤其跨越负数时窗口和的单调性被破坏。

"""
from typing import List
from collections import defaultdict

def subarraySum(self, nums: List[int], k: int) -> int:
    """
    当我们走到位置 i,只要过去某个位置 j 的前缀和等于 pre_sum[i] - k,那么 j+1..i 这一段就是一个和为 k 的子数组。
    于是只需记录“历史上每个前缀和出现过多少次”，每次在 pre_sum 更新后，把 cnt[pre_sum - k] 加到答案里即可。
    """
    cnt = defaultdict(int)
    cnt[0] = 1            # 前缀和为0在起点时出现一次（空前缀）
    pre_sum = 0               # 当前前缀和
    ans = 0

    for x in nums:
        pre_sum += x
        ans += cnt[pre_sum - k]   # 以当前为右端点，能形成和为k的子数组数量
        cnt[pre_sum] += 1         # 当前前缀和出现次数+1

    return ans
        