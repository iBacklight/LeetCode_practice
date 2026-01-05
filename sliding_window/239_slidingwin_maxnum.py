"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

 

示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：

输入：nums = [1], k = 1
输出：[1]

"""
from collections import deque
from typing import List
# 存储数值
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    
    if not nums or k == 0: return []
    n = len(nums)
    max_list = []
    mdeque = deque() # 单调队列

    # 第一个窗口内全部遍历, 以构建完整单减队列
    for i in range(k):
        while mdeque and mdeque[-1] < nums[i]:
            mdeque.pop() # 这里新来的元素大于deque末尾，说明其不可能成为最大值直接弹出
        # 构建递减队列
        mdeque.append(nums[i])
    max_list.append(mdeque[0])

    # 处理后面所有的数字
    for i in range(k, n):# 可以把i想象成是右指针，此时左指针还在上一轮滑窗的起始位置
        # 开始滑窗，相当于先移动右指针
        if mdeque[0] == nums[i-k]:# 如果最大值对应左指针（移位前）位置的数字
            mdeque.popleft() # 弹出旧的左指针位置的值（因为当前左指针的值不在未来的滑窗内了），然后相当于默认左指针移动到 i-k+1
        while mdeque and mdeque[-1] < nums[i]:
            mdeque.pop()
        mdeque.append(nums[i])
        # 对当前滑窗结果处理完毕，记录最大值，即deque的左值
        max_list.append(mdeque[0])

    return max_list


# 存储下标
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        # 存下标 index
        q = deque() 
        result = []
        
        for i, num in enumerate(nums):
            # 1. 入队前清理min值（维护单调递减）
            # 如果新来的 num 比队尾元素大，那么队尾元素这辈子都不可能成为最大值了
            # 因为 num 比它大，还比它活得久
            while q and nums[q[-1]] < num:
                q.pop() # O(1) 尾部弹出
            
            # 2. 入队
            q.append(i)
            
            # 3. 出队过期元素（维护窗口大小）
            # 检查队头元素是否已经滑出了 k 的范围
            # 当前窗口范围是 [i - k + 1, i]，如果队头下标 < i - k + 1，说明过期
            if q[0] == i - k:
                q.popleft() # O(1) 头部弹出
            
            # 4. 记录结果
            # 当窗口形成后（即 i >= k - 1），队头永远是当前窗口的最大值
            if i >= k - 1:
                result.append(nums[q[0]])
                
        return result