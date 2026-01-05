"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

 

示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
示例 2：

输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。

"""
from typing import List
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 不成功的情况：
        # 1. 互为prerequisite或者是更前置课程的
        # 2. 是否开设该课程 -> 好像不用考虑
        # 可以跳过的情况
        # 1. 在新的搜索中发现之前已经上过的，可以直接累加前面的课
        crse_table = {}
        if len(prerequisites) == 0:
            return True

        for crse, pre in prerequisites:
            if crse not in crse_table:
                crse_table[crse] = [pre]
            else:
                crse_table[crse].append(pre)

        
        # 创建state table
        state = [0] * numCourses # 0没到 1正在 2完成

        def dfs(crse):
            if state[crse] == 1: # 说明回到正在链上搜索的课程，证明有环，直接false
                return False
            if state[crse] == 2: # 回到之前已经上过的课程，后面都是对的，直接true
                return True 
            state[crse] = 1 # 把当前crse加入到搜索链中

            if crse in crse_table:
                for pre in crse_table[crse]:
                    if not dfs(pre):
                        return False
            
            # 如果搜索链正确，则最后一个crse的crse_table[crse]为空，会跳过循环
            state[crse] = 2
            return True

        for crse in range(numCourses): # 遍历每节课
            if state[crse] == 0 and not dfs(crse):
                return False

        return True