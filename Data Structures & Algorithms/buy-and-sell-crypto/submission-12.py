class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        pro = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                pro = max(pro, prices[r]-prices[l])
                r += 1

        return pro