"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。

 

示例 1:

输入:nums = [-2,1,-3,4,-1,2,1,-5,4]
输出:6
解释:连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2:

输入:nums = [1]
输出:1
示例 3:

输入:nums = [5,4,-1,7,8]
输出:23

mid
"""
from typing import List
def maxSubArray(nums: List[int]) -> int:
        num_len = len(nums)
        if num_len == 1:
            return nums[0]
        
        max_sum = cur_sum = -1e5

        # 什么时候切换字符串？:
        # 前面数字的和相加小于等于当前数字（选后面）
        for num in nums:
            if num > cur_sum and cur_sum < 0:
                cur_sum = num
                max_sum = max(cur_sum, max_sum)
            elif num + cur_sum < 0 and cur_sum > 0: # 当前为正，新加为负数
                max_sum = max(cur_sum, max_sum)
                cur_sum = 0
            else:
                cur_sum += num # 正常
                max_sum = max(cur_sum, max_sum)
            # print(num, cur_sum, max_sum)
                
        return max_sum


def maxSubArray(nums: List[int]) -> int:
    # 假设f[i]为以第i个元素结尾的最大和连续子数组
    # f[i]=nums[i] 初始i==0时
    # f[i]=max(f[i-1] + nums[i],num[i])
    # 最终返回max(f)
    f = []
    for i in range(len(nums)):
        if i == 0:
            f.append(nums[i])
        else:
            f.append(max(f[i-1]+nums[i],nums[i]))
    
    return max(f)


def maxSubArray(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    
    max_sum = cur_sum = nums[0]
    
    for num in nums[1:]:
        cur_sum = max(num, cur_sum+num)
        max_sum = max(max_sum, cur_sum)

    return max_sum