"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

easy
"""
from typing import List
def maxProfit(prices: List[int]) -> int:
        min_in, max_out = inf, 0
        max_gap = 0

        for price in prices:
            # 假设我每天都卖出，计算每天的收益
            if max_gap < (price-min_in):
                max_gap = price-min_in
            
            # 寻找加上今天，所有之前的历史最低点
            if min_in > price:
                min_in = price
            

        
        return max_gap

def maxProfit_doublepoint(self, prices: List[int]) -> int:
        max_gap = 0
        l = 0
        
        for r in range(len(prices)):
            if max_gap < prices[r] - prices[l]:
                max_gap =  prices[r] - prices[l]
            
            if prices[r] < prices[l]:
                l = r

        return max_gap