class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(l, r):
            while l < r:
                if not s[l].lower() == s[r].lower(): return False
                l += 1
                r -= 1
            return True
        
        left, right = 0, len(s)-1
        while left < right:
            if not s[left] == s[right]:
                return (helper(left + 1, right) or helper(left, right - 1))
            left += 1
            right -= 1
        return True