"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。


示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
示例 3：

输入：intervals = [[4,7],[1,4]]
输出：[[1,7]]
解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。

"""
from typing import List
def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    # 1) 按起点排序
    intervals.sort(key=lambda x: x[0])

    merged = []
    cur_low, cur_up = intervals[0]

    # 2) 线性扫描合并
    for low, up in intervals:
        if low <= cur_up:                   # 有重叠，扩张右边界
            cur_up = max(cur_up, up)
        else:                            # 无重叠，收录上一段，开启新区间
            merged.append([cur_low, cur_up])
            cur_low, cur_up = low, up

    merged.append([cur_low, cur_up])
    return merged


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x:x[0]) #keep in mind 这种用法
    merged = []

    for i in intervals:# 因为已经按照下界排过顺序，只用考虑最后区间一个就好
        if merged == [] or merged[-1][1]<i[0]:# 合并集是空集，或者当前区间的下界在合并集的最后区间以外
            merged.append(i) # 直接添加当前区间
        else:
            merged[-1][1] = max(merged[-1][1],i[1])# 比较当前区间的上届和合并集的最后区间的上届，替换掉较小的一面
            # 逻辑：因为下界顺序排列（当前区间下界大于最后区间下界）且当前区间下界小于最后区间的上届，意味着当前区间必然和最后区间重叠，且不会干涉之前的区间
    return merged
  
# 时间复杂度：O(nlogn)，其中 n 为区间的数量。除去排序的开销，我们只需要一次线性扫描，所以主要的时间开销是排序的 O(nlogn)。
# 空间复杂度：O(logn)，其中 n 为区间的数量。这里计算的是存储答案之外，使用的额外空间。O(logn) 即为排序所需要的空间复杂度。