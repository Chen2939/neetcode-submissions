class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums: return []

        res = []

        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i >= len(nums):
                return
            
            # Continue with this number
            curr.append(nums[i])
            backtrack(i, curr, total+nums[i])
            # Use next number
            curr.pop()
            backtrack(i+1, curr, total)
        
        backtrack(0, [], 0)
        return res

                