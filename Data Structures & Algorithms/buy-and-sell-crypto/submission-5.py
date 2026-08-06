class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        # Edge case: less than 2 days
        if len(prices) < 2:
            return result

        l, r = 0, 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            result = max(result, profit)

            if prices[l] <= prices[r]:
                r += 1
            else:
                l = r
                r += 1
        return result
