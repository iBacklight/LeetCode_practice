"""
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 target 的不同组合数少于 150 个。

 

示例 1：

输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
示例 2：

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
示例 3：

输入: candidates = [2], target = 1
输出: []
 

提示：

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
candidates 的所有元素 互不相同
1 <= target <= 40

medium
"""
from typing import List
# 自己写的代码，但是有以下问题：
# 重复计算 sum(path) (最致命)
#   你的写法：每次递归进来都执行 cur_sum = sum(path)。后果：随着路径变长，计算和的时间变成了 $O(L)$（L为路径长度）。这意味着你在做大量重复的加法运算。优化：应该在递归参数中维护一个 remain (剩余目标值) 或 current_sum，这样每次加减只是 $O(1)$ 的操作。
# 缺乏“剪枝” (Pruning)
# 虽然有 cur_sum > target 的判断，但那是在递归进去之后才判断的。这意味着你还是多跑了一层递归栈。优化：先对 candidates 进行排序。在 for 循环里，如果发现 当前数 > 剩余目标值，因为数组是有序的，后面的数肯定更大，直接 break 退出循环。这能砍掉绝大部分无效分支。
# 递归结构不够简洁你的写法：把你“重复选当前数” backtrace(i) 和 “选后面的数” range(i+1, n) 分成了两块逻辑写。这增加了代码复杂度和调用的开销。优化：利用标准的回溯模板，for i in range(start_index, n)，递归时传入 i (而不是 i+1) 就可以天然实现“可重复选取”。
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        path = []
        n = len(candidates)
        
        def backtrace(i):
            path.append(candidates[i])
            cur_sum = sum(path)
            # 终止条件: 相等或者大于
            if cur_sum == target:
                res.append(path[:])
                return 
            elif cur_sum > target:
                return

            cur_target_sum = target - cur_sum
            if cur_target_sum >= candidates[i]:
                # 如果当前sum值大，就一直添加当前num
                backtrace(i)
                path.pop()
            # pop掉最后，然后遍历数组中下一个num
            for j in range(i+1,n):
                backtrace(j)
                path.pop()
        
        for i in range(n):
            path = []
            backtrace(i)

        return res


# 优化后的代码
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    res = []
    path = []
    n = len(candidates)
    
    # 优化点 1: 排序 (为了后续的剪枝)
    candidates.sort()

    # 参数优化: 传入 start_index 控制去重，传入 remain 避免重复计算 sum
    def backtrack(start_index, remain):
        # 终止条件 1: 刚好凑满
        if remain == 0:
            res.append(path[:])
            return
        
        # 循环选择
        for i in range(start_index, n):
            num = candidates[i]
            
            # 优化点 2: 剪枝 (Pruning)
            # 如果当前这个数已经比剩下的目标大了，后面的数肯定更大，直接不看了
            if num > remain:
                break 
            
            # 做选择
            path.append(num)
            
            # 递归
            # 关键点: 传入 i 而不是 i+1，表示当前数字可以重复使用
            # 优化点 3: 传入 remain - num，O(1) 更新状态
            backtrack(i, remain - num)
            
            # 撤销选择 (回溯)
            path.pop()

    backtrack(0, target)
    return res


### 为什么改完后会快很多？

# 1.  **时间复杂度优化**：移除了 `sum(path)`，状态更新从 $O(L)$ 降到了 $O(1)$。
# 2.  **空间与搜索树优化**：`candidates.sort()` 配合 `if num > remain: break`，极大地减少了搜索树的宽度。比如目标是 7，你现在拿着 8，那么 8 后面的 9, 10, 100 根本不会进入下一层递归，直接被截断了。

### 总结模板记忆

# 对于 **[39. 组合总和] (可重复选)：
# * **排序**：必须做。
# * **参数**：`start_index`, `remain_target`。
# * **循环**：`range(start_index, n)`。
# * **递归**：`backtrack(i, ...)` (传 `i` 代表可复用)。
# * **剪枝**：`if num > remain: break`。