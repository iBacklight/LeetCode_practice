"""
238. 除了自身以外数组的乘积
已解答
中等
相关标签
premium lock icon
相关企业
提示
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。

 

示例 1:

输入: nums = [1,2,3,4]
输出: [24,12,8,6]
示例 2:

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
medium
"""
from typing import List
def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        prefix = 1
        postfix = 1

        for i in range(n):
            # 左边的前缀积乘到当前位置
            answer[i] *= prefix
            prefix *= nums[i]
            
            # 右边的后缀积乘到对称位置
            right_idx = n - 1 - i
            answer[right_idx] *= postfix
            postfix *= nums[right_idx]

        return answer

def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n  # 初始化结果数组

    # 从左往右，把当前元素左边的所有【前缀积】存入 answer
    prefix = 1
    for i in range(n):
        answer[i] = prefix   # 此时 answer[i] 只包含了它左边所有数的乘积
        prefix *= nums[i]    # 滚动更新下一个位置的前缀积

    # 从右往左，动态计算【后缀积】，并直接乘到 answer 里去
    postfix = 1
    for i in range(n - 1, -1, -1):  # 刚学的倒序遍历 range 派上用场了！
        answer[i] *= postfix # 此时的 answer[i] = 原本的左边积 * 现在的右边积
        postfix *= nums[i]   # 滚动更新下一个位置的后缀积

    return answer

def productExceptSelf(self, nums: List[int]) -> List[int]:
    answer = []
    pre_mul  = {}
    post_mul = {}
    n = len(nums)

    for i, num in enumerate(nums):
        if i == 0:
            pre_mul[i] = 1
        else:
            pre_mul[i] =  nums[i-1] * pre_mul[i-1]

    for j, num in enumerate(reversed(nums)):
        if j == 0:
            post_mul[j] = 1
        else:
            post_mul[j] = nums[n-j] * post_mul[j-1]

    for i in range(n):
        answer.append(pre_mul[i]*post_mul[n-i-1])

    return answer