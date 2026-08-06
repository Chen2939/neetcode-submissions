class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0

        l = 0
        for r in range(len(s)):
            # Update count
            count[s[r]] = count.get(s[r], 0) + 1
            # When window is invalid, when max different value is > k steps we are allowed to modify
            # steps_to_modify is (r - l + 1) - max(count.values())
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            result = max((r-l+1), result)
        return result  
