# coding=utf-8
# 121. 买卖股票的最佳时机
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
关键在于状态转移方程，用f(i)表示第i 天可以获取的最大利润，那么
f(i)= max(f(i-1),  prices[i] - min(prices[0:i]))
也就是说，最大值在前i-1天 和 第i天价格与前i-1天价格最小值的差值 之间选择较大的即可
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        earned = 0
        if prices:
            buy = prices[0]
            for price in prices:
                buy = min(price, buy)
                earned = max(earned, price - buy)
        return earned
