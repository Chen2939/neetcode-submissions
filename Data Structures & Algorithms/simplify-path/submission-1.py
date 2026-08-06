class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curStr = ""

        for c in path+'/':
            if c == '/':
                if curStr == "..":
                    if stack: stack.pop()
                elif curStr != "" and curStr != ".":
                    stack.append(curStr)
                curStr = ""
            else:
                curStr += c
        
        return "/"+"/".join(stack)