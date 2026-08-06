class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Think of n as a pointer to position
        # we dont care the 0th node 1 because no node points to 1
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        s1, s2 = nums[0], fast
        while s1 != s2:
            s1 = nums[s1]
            s2 = nums[s2]
            if s1 == s2: break

        return s1