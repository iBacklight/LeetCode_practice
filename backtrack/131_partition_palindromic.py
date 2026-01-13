"""
131. 分割回文串
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和倒着读都一样的字符串。

 

示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]


medium
"""
from typing import List
def partition(self, s: str) -> List[List[str]]:
    path = []
    res = []
    n = len(s)

    def backtraces(i):
        # 题目要求切割字串，则必须连续
        # 又要求是回文, 判断回文是主要的

        # 终止条件
        if i == n:
            res.append(path[:])
            return

        # 以当前下标i作为起点，迭代子串直到尾部
        # 
        for j in range(i, n):
            if s[i] == s[j]:# 剪枝
                # 切片当前子串
                sub = s[i:j+1]

                # 判断回文
                if sub == sub[::-1]:
                    # 如果是回文，加入当前子串，并在这个位置切一刀
                    path.append(sub)
                    # 递归到切割后的下一个位置，相当于起点变更到j+1
                    backtraces(j+1)
                    # 拿掉上一个添加的回文串，重新在i起点的下一个子串
                    path.pop()

        return

    backtraces(0)
    return res


# 更快的办法: 回溯 + memo
def partition(self, s: str) -> List[List[str]]:
    n = len(s)

    @cache 
    def dfs(i):
        if i == n:
            return [[]]  # 返回由空列表组成的列表，表示找到一种基准情况

        ans = []
        for j in range(i, n):
            # 先比对首尾字符，不相等则绝不可能是回文
            if s[i] == s[j]: 
                sub = s[i:j+1]
                if sub == sub[::-1]: # 切片检查
                    # 获取当前回文子串的所有的切分结果
                    suffix_partitions = dfs(j + 1)
                    # 将所有后续的回文串拼接到sub后面
                    for p in suffix_partitions:
                        ans.append([sub] + p)
        return ans

    return dfs(0)