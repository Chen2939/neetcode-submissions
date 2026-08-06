class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        numOfStrs = len(strs)
        res = ""
        for i, c in enumerate(strs[0]):
            for j in range(numOfStrs):
                if i >= len(strs[j]) or c != strs[j][i]: return res
            res += c
        return res