class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        stack = []
        for o in operations:
            if o == "+":
                num = stack[-1] + stack[-2]
                stack.append(num)
                res += num
            elif o == "D":
                num = 2 * stack[-1]
                stack.append(num)
                res += num
            elif o == "C":
                res -= stack.pop()
            else:
                num = int(o)
                stack.append(num)
                res += num

        return res