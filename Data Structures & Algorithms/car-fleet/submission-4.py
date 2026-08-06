class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [(p, s) for p, s in zip(position, speed)]
        res = []
        for p, s in sorted(stack)[::-1]:
            t = (target - p) / s
            res.append(t)

            if len(res) >= 2 and res[-1] <= res[-2]:
                res.pop()
        
        return len(res)