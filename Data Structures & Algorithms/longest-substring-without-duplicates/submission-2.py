class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        strSet = set()

        for r in range(len(s)):
            while s[r] in strSet:
                strSet.remove(s[l])
                l += 1
            strSet.add(s[r])
            res = max(res, len(strSet))
        
        return res
