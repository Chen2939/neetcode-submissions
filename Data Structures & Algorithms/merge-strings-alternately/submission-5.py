class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        l = r = 0
        for i in range(len(word1)):
            if l < len(word1):
                res.append(word1[l])
                l += 1
            if r < len(word2):
                res.append(word2[r])
                r += 1

        res.append(word1[l:])
        res.append(word2[r:])
    
        return "".join(res)