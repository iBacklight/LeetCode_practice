"""
198. 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
from typing import List
# 解法一： DP， 如果要偷 i，只需要访问 dp[i-2]，状态方程：
# dp[i] = max(dp[i-1], dp[i-2] + nums[i])
def rob(nums: List[int]) -> int:
    rec = {} 

    def f_max(i):
        # 越界处理 (Base Case)
        if i < 0:
            return 0
        # 查备忘录
        if i in rec:
            return rec[i]

        # 核心转移方程：二选一
        # max(不偷这家, 偷这家并加上前两家的最大值)
        res = max(f_max(i-1), f_max(i-2) + nums[i])
        # 记下来
        rec[i] = res
        return res

    # 从最后一家开始往前推
    return f_max(len(nums) - 1)

# 这种解法也有更加简单的
def rob(nums: List[int]) -> int:
    if not nums: 
        return 0
    if len(nums) <= 2: 
        return max(nums)

    last_last_rob_max = 0 
    last_rob_max = nums[0]

    # 由于我们起始last_rob_max已经假设偷了，所以必须从第二家开始迭代
    for i in range(1, len(nums)):
        # 要么直接拿上一次的最大值，即不偷当前
        # 要么偷当前，但是要加上上次（两步开外）的最大值
        cur_max = max(last_rob_max, last_last_rob_max + nums[i])

        last_last_rob_max = last_rob_max # 整体步进 1，所以上上次最大赋值上次最大
        last_rob_max = cur_max


    return last_rob_max

# 解法二：暴力递归+memo，时间O(N**2)+空间O(N)
def rob(nums: List[int]) -> int:
    # 可以将题目理解为，分治加记忆化
    # 当前只能偷(n-2)!的家庭, 并且最大利润为cur_max + cur_rob
    if len(nums) <= 2:
        return max(nums)

    rec = {} # 用于储存已经迭代过的数值
    rec[0] = nums[0]
    rec[1] = nums[1]
    res = []

    def f_max(i):
        if i in rec:
            return rec[i]
        cur_max = 0
        # 从 n-2开始，遍历(n-2)!求max
        #需要注意由于range取不到最后一个值，所以必须是range(i-1)不是i-2
        for j in reversed(range(i-1)):
            cur_max = max(cur_max, f_max(j) + nums[i])
        rec[i] = cur_max

        return cur_max
	# 遍历名配合f_max中的i-1，这里要从1开始遍历
    for i in range(1, len(nums)):
        res.append(f_max(i))

    return max(res)