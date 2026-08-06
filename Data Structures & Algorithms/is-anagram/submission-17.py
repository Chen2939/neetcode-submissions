class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        counts = {}
        
        # 使用单个字典，s 里的字符加 1，t 里的字符减 1
        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
            counts[t[i]] = counts.get(t[i], 0) - 1
            
        # 检查是否所有字符的净频率都抵消成了 0
        for count in counts.values():
            if count != 0:
                return False
                
        return True