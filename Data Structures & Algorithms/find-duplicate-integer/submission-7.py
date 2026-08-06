class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        
        s1, s2 = nums[0], fast
        while s1!=s2:
            s1 = nums[s1]
            s2 = nums[s2]
            if s1 == s2:
                break
        
        return s1