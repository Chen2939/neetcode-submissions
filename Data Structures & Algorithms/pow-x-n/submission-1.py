class Solution:
    def myPow(self, x: float, n: int) -> float:
                # x^-n = 1 / x ^ n
        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            # DnC, n = 5, n = 2
            res = helper(x * x, n // 2)
            return x * res if n % 2 else res

        res = helper(x, abs(n))
        return res if n >= 0 else 1/res