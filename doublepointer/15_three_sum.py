"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
 

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 
"""

from typing import List
def threeSum_hash(nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res_set = set()

        for i in range(n):
            # 提前去重：相同 i 值只做一次
            # 防止看到[-1, -1, 0, 1, 2, ...]，两次看到同样数字，产生同样结果
            # 前提是，已经排序，后面不会在该循环中看到相同数字
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]: 
                continue

            target = 0-nums[i]
            seen = set()  # 存已见到的数
            # transit to two sum
            for j in range(i+1, n):
                need = target - nums[j]
                if need in seen:
                    res_set.add((nums[i], need, nums[j]))  # 三元组已按升序
                seen.add(nums[j])

        return [list(t) for t in res_set]

def threeSum_doublePointer(nums: List[int]) -> List[List[int]]:
    # 双指针
    nums.sort()
    n = len(nums)
    res = []
    
    for i in range(n):
        # 相同剪枝
        if nums[i] > 0:
            break
        if i >= 1 and nums[i] == nums[i-1]:
            continue

        # 构造双指针
        l = i+1
        r = n-1
        while l < r:# 边界条件：排序后l<r
            num_sum = nums[i] + nums[l] + nums[r]
            if num_sum == 0:
                # 双指针 l 和 r 一次次收缩，遍历过程中生成的解是按升序来的。所以重复一定会相邻出现
                # 只需要作相邻去重(即res最后一个数组和当前不一样即可)
                if len(res) == 0 or [nums[i], nums[l], nums[r]] != res[-1]:# 防止数字重复
                    res.append([nums[i], nums[l], nums[r]])
                l += 1 # 无论如何，都要双边改变指针
                r -= 1
            elif num_sum > 0:
                r -= 1
            elif num_sum < 0:
                l += 1
    return res

print(threeSum_hash([-100,-70,-60,110,120,130,160]))
print(threeSum_doublePointer([-1,0,1,2,-1,-4,-2,-3,3,0,4]))