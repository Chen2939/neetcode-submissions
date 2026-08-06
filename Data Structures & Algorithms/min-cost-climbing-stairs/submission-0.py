class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        # reverse order, start from -3 cuz 1) we append an 0, 2) last valid element is fixed 
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2]) # compare 1st jump to second jump
        
        return min(cost[0], cost[1])