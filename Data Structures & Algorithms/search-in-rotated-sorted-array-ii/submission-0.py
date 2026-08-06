class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        m = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                m = i
                break
        
        if m == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[0]:
            l, r = 0, m - 1
        else:
            l, r = m, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False