class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            temp = n * curMax
            curMax = max(temp, n*curMin, n)
            curMin = min(temp, n*curMin, n)
            res = max(curMax, curMin, res)
        return res