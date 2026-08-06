class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        if len(t) > len(s): return ""

        countT, window = {}, {}
        result, resLen = [-1, -1], float("infinity")

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        have, need = 0, len(countT)
        
        l = 0
        for r in range(len(s)):
            # read character and update window
            c = s[r]
            window[c] = window.get(c, 0) + 1
            # does window satisfy what we need?
            if c in countT and countT[c] == window[c]:
                have += 1
            
            # when we finally have what we need
            while have == need:
                # update result if current is shorter
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    result = [l, r]
                # pop window from the left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = result
        return s[l: r+1] if resLen != float("infinity") else ""
            