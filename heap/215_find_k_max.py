"""
215. 数组中的第K个最大元素

给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

mid level

示例 1:

输入: [3,2,1,5,6,4], k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4

"""
import heapq
from typing import List
def findKthLargest_heap(nums: List[int], k: int) -> int: #Onlogk
        # 1) 先把前 k 个元素放进最小堆
        heap = nums[:k]
        heapq.heapify(heap)  # O(k)

        # 2) 遍历剩余元素，只有当比堆顶更大时才替换堆顶
        for x in nums[k:]:
                if x > heap[0]:
                        heapq.heapreplace(heap, x)  # 等价于 heappop + heappush，O(log k)

        # 3) 堆顶就是第 k 大
        return heap[0]

def findKthLargest_sort(nums: List[int], k: int) -> int:
        return sorted(nums)[len(nums)-k] #Onlogn

import random
def quickSelect(nums: List[int], k: int) -> int: #期望情况下（随机主元使规模大致按常数比例缩小）On, worst On^2
        """快速选择核心函数：在nums中找到第k大元素"""
        # 随机选择基准元素
        pivot = nums[random.randint(0, len(nums) - 1)]
        
        # 划分为三个子数组：
        # big：存储所有 大于基准 的元素
        # equal：存储所有 等于基准 的元素
        # small：存储所有 小于基准 的元素
        big, equal, small = [], [], []
        for x in nums:
                if x > pivot:
                        big.append(x)
                elif x < pivot:
                        small.append(x)
                else:
                        equal.append(x)
                
        # 根据三个子数组的长度与k比较的情况，决定递归方向
        # 情况1：第k大元素在big数组中（k <= big的长度）
        if k <= len(big):
                return quickSelect(big, k)
        # 情况2：第k大元素在small数组中（k > big + equal的长度）
        elif k > len(big) + len(equal):
                # 调整k：减去big和equal的长度
                return quickSelect(small, k - (len(big) + len(equal)))
        # 情况3：第k大元素在equal数组中（直接返回基准值）
        else:
                return pivot

def findKthLargest_quickselection(nums: List[int], k: int) -> int:
        random.seed()  # 初始化随机数种子，确保每次基准选择随机
        return quickSelect(nums, k)

