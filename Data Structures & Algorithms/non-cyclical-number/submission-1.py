class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        def soS(n):
            res = 0
            while n:
                digit = n % 10
                digit = digit ** 2
                res += digit
                n = n // 10
            return res
        
        while n not in visit:
            visit.add(n)
            n = soS(n)
            if n == 1: return True
        
        return False