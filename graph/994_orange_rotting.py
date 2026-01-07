"""
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

 

示例 1：


输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
示例 3：

输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] 仅为 0、1 或 2
"""
from typing import List
def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        queue = deque() # deque可以把pop(0)的复杂度变为O(1)
        minutes = 0
        fresh = 0
        r, c = len(grid), len(grid[0])

        # 将腐烂的橘子做为起点入队
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1 # 记录新鲜橘子数量以满足-1返回
        
        if len(queue) == 0 and fresh > 0: # 
            return -1
        elif len(queue) == 0 and fresh == 0:
            return 0
        
        # BFS 开始
        while queue and fresh > 0:# 条件：当前队列中仍然有邻接的腐烂橘子，或者没有新鲜橘子了
        #第二个条件对最少时间至关重要，否则去三年后i
            for ro in range(len(queue)):# 遍历当前所有的腐烂橘子
                i,j = queue.popleft() # 从最近的开始

                # 它的四周开始腐烂
                for pos_i, pos_j in [(-1,0), (1,0), (0,-1), (0,1)]:
                    cur_i, cur_j = i + pos_i, j + pos_j

                    # 边界条件
                    if 0 <= cur_i < len(grid) and 0 <= cur_j < len(grid[0]):
                        if grid[cur_i][cur_j] == 1: # 找到新鲜橘子
                            grid[cur_i][cur_j] = 2
                            queue.append([cur_i, cur_j]) # 新的腐烂橘子入队
                            fresh -= 1
            minutes += 1

        if fresh > 0: # queue空了（所有腐烂橘子均已遍历，没有邻接的新鲜橘子），
        # 但是还有新鲜橘子数量还有，说明剩下的新鲜橘子，均不与腐烂橘子邻接
            return -1
        return minutes