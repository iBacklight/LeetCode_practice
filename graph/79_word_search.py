"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例 1：


输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCCED"
输出：true
示例 2：


输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "SEE"
输出：true
示例 3：


输入：board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCB"
输出：false
 

提示：

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board 和 word 仅由大小写英文字母组成

"""
from typing import List
def exist(board: List[List[str]], word: str) -> bool:
    r, c = len(board), len(board[0])
    L = len(word)
    if L > r * c: # 大于总board数量直接返回
        return False

    def dfs(i: int, j: int, k: int) -> bool:
        # k 表示正在匹配 word[k]
        if board[i][j] != word[k]:# 非当前字符直接false
            return False
        if k == L - 1: # 
            return True

        ch = board[i][j]
        board[i][j] = "#"  # 标记访问

        for pos_i, pos_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            now_i, now_j = i + pos_i, j + pos_j
            if 0 <= now_i < r and 0 <= now_j < c and board[now_i][now_j] != "#":
                if dfs(now_i, now_j, k + 1):
                    board[i][j] = ch  # 恢复
                    return True

        board[i][j] = ch  # 恢复，即撤销之前的visited更改
        return False

    for i in range(r):
        for j in range(c):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True
    return False
