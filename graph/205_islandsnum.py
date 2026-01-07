"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。


示例 1：

输入：grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
]
输出：1
示例 2：

输入：grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
输出：3

"""
from typing import List
def numIslands_dfs(grid: List[List[str]]) -> int:
    if not grid: return 0
    m, n = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        # 越界或者不是陆地，直接返回
        if not (0 <= r < m and 0 <= c < n and grid[r][c] == '1'):
            return

        grid[r][c] = '0' # 核沉没它！标记为已访问

        # 向四个方向扩散
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j) # dfs相当于将该岛屿直接沉没
    return count

def numIslands_bfs(grid: List[List[str]]) -> int:
    from collections import deque

    island_count = 0
    r, c = len(grid), len(grid[0])

    def bfs(i,j):
        queue = deque() # 起点入队， 并且立即沉没
        queue.append([i,j])
        grid[i][j] = '0' 

        while queue:
            i, j = queue.popleft()

            for pos_i, pos_j in [(-1,0), (1,0), (0,-1), (0,1)]:
                cur_i, cur_j = i + pos_i,  j + pos_j

                if 0 <= cur_i < len(grid) and 0 <= cur_j < len(grid[0]):
                    if grid[cur_i][cur_j] == '1': 
                        queue.append([cur_i, cur_j])    
                        grid[cur_i][cur_j] = '0'# 一样，加入队列，然后立即沉没
                        # 相当于他们是同一“组”

    for i in range(r):
        for j in range(c):
            if grid[i][j] == "1":
                island_count += 1
                bfs(i,j)
    
    return island_count