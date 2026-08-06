class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        
        stack = []
        # Want to reverse sort by the car cloest to the target 
        for p, s in sorted(pair)[::-1]:
            # What time the car is reaching the des
            stack.append((target - p) / s)
            # Check does it overlap with the other one
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # Decrease fleet
                stack.pop()
        return len(stack)