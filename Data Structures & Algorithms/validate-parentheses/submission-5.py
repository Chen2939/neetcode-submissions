class Solution:
    def isValid(self, s: str) -> bool:
        ref = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in ref.values():
                stack.append(c)
            else:
                # If stack is not empty and we found match
                if stack and stack[-1] == ref.get(c, '/'):
                    stack.pop()
                else:
                    return False
        
        return True if len(stack) == 0 else False