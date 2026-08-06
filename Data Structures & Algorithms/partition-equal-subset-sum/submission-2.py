class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums) % 2 == 1: return False

        dp = set()
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            newdp = set()
            for item in dp:
                newdp.add(item)
                newdp.add(item + nums[i])
            dp = newdp
        
        return target in dp
            