class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for o in operations:
            if o == '+':
                plus = stack[-1] + stack[-2]
                stack.append(plus)
                res += plus
            elif o == 'D':
                doubled = stack[-1] * 2
                stack.append(doubled)
                res += doubled
            elif o == "C":
                res -= stack.pop()
            else:
                stack.append(int(o))
                res += int(o)

        return res