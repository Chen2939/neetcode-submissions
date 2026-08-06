class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:  # sum to large, decrease r
                r -= 1
            elif numbers[l] + numbers[r] < target:  # sum to small, increase l
                l += 1