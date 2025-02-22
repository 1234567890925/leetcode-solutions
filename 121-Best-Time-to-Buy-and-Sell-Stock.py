class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit
            