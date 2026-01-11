"""
78. 子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

medium
"""
from typing import List
def subsets(self, nums: List[int]) -> List[List[int]]: 
        res = [[]]
        path = []
        n = len(nums)
        if n == 0:
            return res

        def backtrace(i):
            path.append(nums[i])
            res.append(path[:])
            # 中止条件：全部都加到数组了
            if i >= n-1:
                return
            # 遍历当前以后的，因为不能回头
            for j in range(i+1, n):
                backtrace(j)
                # 同一阶段，pop掉最后的值才能继续连接新值
                # 比如 [1,2](下一步值循环一次就返回了),[1,2,3]（不循环直接返回） -> [1,3]
                path.pop()

            return
        

        for i in range(n):
            path = []
            backtrace(i)

        return res