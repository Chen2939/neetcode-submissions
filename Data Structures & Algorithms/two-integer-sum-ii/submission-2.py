class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            twoS = numbers[l] + numbers[r]
            if twoS == target:
                return [l+1, r+1]
            elif twoS < target:
                l += 1
            else:
                r -= 1