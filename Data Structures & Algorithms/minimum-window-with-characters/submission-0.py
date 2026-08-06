class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        countT, window = {}, {}
        # Build count map for t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        result, resLen = [-1, -1], float("infinity")
        # Just need to iterate through the array once
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # Does window satisfy what we need
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                # Update our result if current is shorter
                if (r - l + 1) < resLen:
                    result = [l, r]
                    resLen = (r - l + 1)
                # Pop from the left of the window
                window[s[l]] -= 1
                # If popped reduce from what we have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = result

        return s[l:r+1] if resLen != float("infinity") else ""
