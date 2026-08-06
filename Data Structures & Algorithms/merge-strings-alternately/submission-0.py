class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:        
        res = ""
        if len(word1) > len(word2):
            for i in range(len(word1)):
                res += word1[i]
                if i < len(word2):
                    res += word2[i]
        else:
            for i in range(len(word2)):
                if i < len(word1):
                    res += word1[i]
                res += word2[i]
        
        return res
            