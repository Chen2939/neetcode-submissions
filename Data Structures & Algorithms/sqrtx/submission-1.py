class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l <= r:
            m = (l+r) // 2
            res = m * m
            if res == x: return m
            elif res > x: r = m - 1
            else: l = m + 1
        return r