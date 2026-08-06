class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return (helper(l+1, r) or helper(l, r-1))
            l += 1
            r -= 1
        
        return True