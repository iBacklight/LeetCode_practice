"""
46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

 
示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
 

提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同

medium
"""
from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    res = []
    path = [] # 唯一的共享状态

    def backtrack(available_nums):
        # 结束条件
        if len(path) == len(nums):
            # 必须拷贝一份当前路径到结果
            # 切忌用append(path)，path到最后已经被pop清空了
            res.append(path[:]) 
            return

        for i in range(len(available_nums)):
            num = available_nums[i]

            # --- A. 做选择 (Do) ---
            path.append(num) 

            # --- B. 递归 (Recurse) ---
            # 下一层决策树：剩下的数字里选 (这里用切片模拟了 used 数组)
            backtrack(available_nums[:i] + available_nums[i+1:])

            # --- C. 状态重置 (Undo/Reset) ---
            # 回溯的核心：把刚才放进去的 num 拿出来
            # 否则下一次循环尝试别的数字时，path 里就还有这个 num
            # 例子：从 [1,2,3] 返回到 [1,2]
            # 如果不 pop 掉 3，path 依然是 [1,2,3]。
            # 当我们想去尝试其他分支（比如 [1,2,4]）时，(假设有)
            # path 就会变成错误的 [1,2,3,4]，带着上一次的“脏数据”。
            path.pop() 

    backtrack(nums)
    return res

# 或者使用visitied模板
def permute(nums: List[int]) -> List[List[int]]:
    res = []
    path = []
    # used 数组：记录 nums[i] 是否已经在当前 path 里
    # $O(1)$ 的查重
    used = [False] * len(nums)

    def backtrack():
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            # 关键点：如果 used[i] 是 True，说明这个数字在 path 里了，跳过
            if used[i]: 
                continue

            # 做选择并标记
            used[i] = True
            path.append(nums[i])

            # 递归
            backtrack()

            # 状态重置 (回溯)
            used[i] = False
            path.pop()

    backtrack()
    return res