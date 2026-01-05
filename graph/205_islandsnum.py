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
        # (i,j)相邻节点 ind 是在双节点上+'1'
        row_len = len(grid)
        col_len = len(grid[0])
        num = {}
        islands = 0

        def dfs(x, y, row_len, col_len):
            for mov_dir in [(1, 0),(0, 1),(-1, 0),(0, -1)]:
                nx = x + mov_dir[0]
                ny = y + mov_dir[1]
                if nx >= 0 and ny >= 0 and nx < row_len and ny < col_len:
                    if grid[nx][ny] == "1":
                        grid[nx][ny] = "0" # 把走过的地方变成0
                        dfs(nx, ny, row_len, col_len)

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1":
                    islands += 1
                    grid[i][j] = "0"
                    dfs(i,j, row_len, col_len)
      
        return islands

def numIslands_bfs(grid: List[List[str]]) -> int:
        from collections import deque
        # (i,j)相邻节点 ind 是在双节点上+'1'
        row_len = len(grid)
        col_len = len(grid[0])
        num = {}
        islands = 0

        def bfs(x, y, row_len, col_len):
            q = deque()
            for mov_dir in [(1, 0),(0, 1),(-1, 0),(0, -1)]:
                nx = x + mov_dir[0]
                ny = y + mov_dir[1]
                if nx >= 0 and ny >= 0 and nx < row_len and ny < col_len:
                    if grid[nx][ny] == "1":
                        grid[nx][ny] = "0" # 把走过的地方变成0
                        q.append((nx, ny))
            while len(q) > 0:
                nx, ny = q.popleft()
                bfs(nx, ny, row_len, col_len)
            
            return None

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1":
                    islands += 1
                    grid[i][j] = "0"
                    bfs(i,j, row_len, col_len)
      
        return islands