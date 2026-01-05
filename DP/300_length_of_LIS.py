from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    """
    Greedy & bisect find
    
    遍历数组，把每个数放到一个“牌堆”里。

    规则：新数必须放到最左边的那个大于等于它的堆顶上；如果没有堆顶 ≥ 它，就新开一个堆。

    最后堆的数量，就是 LIS 的长度。 

    e.g.
        例子： [1,3,6,7,9,4,10,5,6]

        执行过程：

            放 1 → [1]

            放 3 → [1,3]

            放 6 → [1,3,6]

            放 7 → [1,3,6,7]

            放 9 → [1,3,6,7,9]

            放 4 → [1,3,4,7,9] （更新堆顶 6→4)

            放 10 → [1,3,4,7,9,10]

            放 5 → [1,3,4,5,9,10] （更新堆顶 7→5)

            放 6 → [1,3,4,5,6,10] （更新堆顶 9→6)

            结果堆数 = 6 → 最长递增子序列长度是 6。
    
    """
    from bisect import bisect_left
    tails = []  # tails[i] = 长度为 i+1 的递增子序列的最小结尾
    for x in nums:
        i = bisect_left(tails, x)  # 找到第一个 >= x 的位置
        if i == len(tails):
            tails.append(x)        # 新开一个堆
        else:
            tails[i] = x           # 更新堆顶为更小的值
    return len(tails)



def lengthOfLIS(nums: List[int]) -> int:
    """
    状态定义

        dp[i] = 以 nums[i] 作为子序列最后一个元素时，最长递增子序列的长度。

    初始化

        每个元素自己就是一个子序列，所以初始值都设为 1。

    状态转移

        枚举 j 在 [0, i):
        如果 nums[j] < nums[i]，说明 nums[i] 可以接在 nums[j] 之后：

        dp[i]=max(dp[i],dp[j]+1)

    答案

        取所有 dp[i] 的最大值，即 max(dp)。

    e.g.

    输入：[1,3,6,7,9,4,10,5,6]

        初始:dp = [1,1,1,1,1,1,1,1,1]

        i=1 (3)：比 1 大 → dp[1] = 2

        i=2 (6)：比 1,3 大 → dp[2] = 3

        i=3 (7)：比 1,3,6 大 → dp[3] = 4

        i=4 (9)：比 1,3,6,7 大 → dp[4] = 5

        i=5 (4)：比 1,3 大 → dp[5] = 3

        i=6 (10)：比 1,3,6,7,9,4 大 → dp[6] = 6

        i=7 (5)：比 1,3,4 大 → dp[7] = 4

        i=8 (6)：比 1,3,4,5 大 → dp[8] = 5

        最终 max(dp) = 6。
    """
    if not nums: return 0
    dp = [1] * len(nums)  # dp[i] 表示以 nums[i] 结尾的 LIS 长度
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

