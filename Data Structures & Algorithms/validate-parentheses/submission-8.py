class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {"}":"{", "]":"[", ")":"("}
        stack = []

        for paren in s:
            if paren in hmap.values():
                stack.append(paren)
            else:
                if stack and hmap[paren] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return True if len(stack) == 0 else False

        
