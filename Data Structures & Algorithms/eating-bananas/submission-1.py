class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = float("infinity")

        while l <= r:
            k = (l+r) // 2
            hour = 0
            for i in piles:
                hour += math.ceil(i / k)

            if hour > h:
                l = k+1
            elif hour <= h:
                result = min(result, k)
                r = k-1
        return result
            