class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_set = set()
        for i, v in enumerate(nums):
            dup_set.add(v)
            if len(dup_set) != i+1:
                return True
        return False


        