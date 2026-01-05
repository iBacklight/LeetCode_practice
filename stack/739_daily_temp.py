"""
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

示例 1:

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
示例 2:

输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
示例 3:

输入: temperatures = [30,60,90]
输出: [1,1,0]

"""
from typing import List
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    ans = [0] * n
    stack = [] # 存索引

    for i, temp in enumerate(temperatures):
        # 当栈不为空，且当前温度比栈顶索引对应的温度高
        # 说明栈顶那个元素的“下一个更高温度”找到了，就是当前这个 temp
        while stack and temp > temperatures[stack[-1]]:
            # 遍历所有小于当前温度的天数并且pop
            # 在栈中的天数都是没有找到最近高温的
            prev_index = stack.pop()
            ans[prev_index] = i - prev_index # 计算距离

        # 把当前索引入栈，等待它的“更高温度”出现
        stack.append(i)

    return ans