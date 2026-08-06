class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setS = set()
        result = 0
        l = 0
        for r in range(len(s)):
            while s[r] in setS: # this means we have a duplicate
                # then we need to shrink the window from l
                setS.remove(s[l])
                l += 1
            setS.add(s[r])
            result = max(result, r-l+1)
        return result
