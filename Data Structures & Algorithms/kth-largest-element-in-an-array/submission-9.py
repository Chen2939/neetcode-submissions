import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        left, right = 0, len(nums) - 1

        while left <= right:
            # random choose pivot index and value, then move to tail (swap with right)
            pIdx = random.randint(left, right)
            pValue = nums[pIdx]
            nums[pIdx], nums[right] = nums[right], nums[pIdx]

            # in place partition
            sIdx = left
            for i in range(left, right):
                if nums[i] < pValue:
                    nums[sIdx], nums[i] = nums[i], nums[sIdx]
                    sIdx += 1
            nums[right], nums[sIdx] = nums[sIdx], nums[right]

            if sIdx == target:
                return nums[sIdx]
            elif sIdx < target:
                left = sIdx + 1
            else:
                right = sIdx - 1
        
        return -1