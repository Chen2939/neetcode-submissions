class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s = []
        for i in range(len(nums)):
            heapq.heappush(s,nums[i])
            if i >=k:
                heapq.heappop(s)
            # print(s)
        return s[0]