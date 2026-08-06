class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        for i in range(len(prices)):
            if r < len(prices):
                if prices[l] <= prices[r]: # have a profit
                    profit = max(profit, prices[r] - prices[l])
                    r += 1
                else: # there is no profit
                    l = r
                    r += 1
        return profit