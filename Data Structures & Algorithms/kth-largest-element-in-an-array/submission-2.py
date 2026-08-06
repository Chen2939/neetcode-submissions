import numpy as np
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return int(np.partition(nums, len(nums)-k)[len(nums) - k])