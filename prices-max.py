class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        prices.sort
        l, r = 0, len(prices)-1
        while prices[r]>prices[l]:
            print('im in')
            profit = prices[r] - prices[l]
            print(profit)
            max_profit = max(max_profit, profit)
            print(max_profit)
        return max_profit
sol = Solution()
prices = [7,1,5,3,6,4]
res = sol.maxProfit(prices)
print(res)