"""
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]

medium
"""
from typing import List
def generateParenthesis(self, n: int) -> List[str]:
    path = []
    res = []
    max_len = n * 2
    fq_count = bq_count = n

    def backtraces(fq_count, bq_count):
        # 终止条件
        if len(path) == max_len:
            str_path = "".join(path)
            res.append(str_path)
            return

        # 每次进来都回溯两次，一次加前括号，一次加后括号
        # 先加左括号,只要还有就一直加
        if fq_count > 0:
            path.append("(")
            backtraces(fq_count-1, bq_count)
            path.pop()
        
        # 只有剩余的右括号比左括号多（说明加的左括号比右括号多），才能加右括号
        if bq_count > fq_count:
            path.append(")")
            backtraces(fq_count, bq_count-1)
            # 会一直pop直到fq_count!=0
            path.pop()
        
        return
    backtraces(fq_count, bq_count)

    return res

