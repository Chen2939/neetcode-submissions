class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonically Decreasing Stack
        stack = [] # [temp, index]
        result = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            while len(stack) != 0 and t > stack[-1][0]:
                lower = stack.pop()
                result[lower[1]] = i - lower[1]

            stack.append([t, i])
        return result