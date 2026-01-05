"""

"""
from typing import List
def climbStairs_recur(self, n: int) -> int:
    # f(n) = f(n-1) + f(n-2) = f(n-2) + f(n-3) + f(n-3) + f(n-4) = ...
    # 这似乎是一个斐波那契数列

    rec = {}

    def f(cur_n): # Recur based on the f(n) = f(n-1) + f(n-2)  and record the cals we did
        if cur_n in rec:
            return rec[cur_n]
        if cur_n > 2:
            rec[cur_n] = f(cur_n-1) + f(cur_n-2)
            return rec[cur_n]
        else:
            return cur_n

    return f(n)


def climbStairs(n: int) -> int:
        # f(n) = f(n-1) + f(n-2) = f(n-2) + f(n-3) + f(n-3) + f(n-4) = ...
        # 这似乎是一个斐波那契数列

        if n <= 2:
            return n

        # f 表示 f(i-2)，s 表示 f(i-1)
        # 对应 f(1)=1, f(2)=2
        f, s = 1, 2

        for i in range(3, n + 1):
            # 暂存当前的 f(i-1)，以便更新 f(i-2)
            last_s = s

            # 递推关系：f(i) = f(i-1) + f(i-2)
            # s 更新为当前的 f(i)
            s = f + s

            # f 更新为旧的 f(i-1)，即下一轮的 f(i-2)
            f = last_s
           

        return s

