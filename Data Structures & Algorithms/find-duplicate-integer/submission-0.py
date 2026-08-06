class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Find end of cycle where s and f intersect
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # slow2 and slow 1 for p and x
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow