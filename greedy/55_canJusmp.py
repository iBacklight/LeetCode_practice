"""
mid
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

 

示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

"""
from typing import List
def canJump(nums: List[int]) -> bool:
    nums_len = len(nums)
    total_max_steps = 0 # 行走过的总和

    for i in range(nums_len):
        if i <= total_max_steps: # 如果最远的步长达不到正在遍历的下标，说明卡住了
            total_max_steps = max(total_max_steps, i+nums[i]) # 贪心
            if total_max_steps >= nums_len - 1:# 如果超过，说明已经到达
                return True
        else:
            return False # 直接判定无法到达

    return False

def canJump_dp(nums: List[int]) -> bool:
    """
    思路：反向动态规划 / 贪心
    从后往前遍历，记录“最后一个可以到达终点的位置（last_good）”。
    若当前位置 i 能跳到 last_good，则更新 last_good = i。
    最后如果 last_good == 0，说明起点也能到达终点。
    """

    # 初始化：最后一个位置显然是“可达终点”的位置
    last_good = len(nums) - 1

    # 从倒数第二个位置开始往前检查
    for i in range(len(nums) - 2, -1, -1):
        # 如果当前位置可以跳到（或超过）最后的可达点
        # 说明当前位置也可达终点
        if i + nums[i] >= last_good:
            last_good = i  # 向左扩展“可达区间”

    # 如果最后“可达区间”扩展到了 0，说明起点能到达终点
    return last_good == 0