class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def backtrack(op, cl, stack):
            if op == cl == n:
                res.append("".join(stack.copy()))
                return
            
            if op < n:
                stack.append("(")
                backtrack(op+1, cl, stack)
                stack.pop()
            
            if cl < op:
                stack.append(")")
                backtrack(op, cl+1, stack)
                stack.pop()
        
        backtrack(0, 0, stack)
        return res
            


