class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1 # 1 way to sum to zero with first 0 elements

        for i in range(len(nums)):
            nextdp = defaultdict(int)

            for cur_sum, count in dp.items():
                nextdp[cur_sum + nums[i]] += count
                nextdp[cur_sum - nums[i]] += count
            
            dp = nextdp

        return dp[target]