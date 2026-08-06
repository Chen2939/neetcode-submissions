class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for n in nums:
            hmap[n] = 1 + hmap.get(n, 0)
        
        freq = [[] for _ in range(len(nums)+1)]
        for num in hmap:
            freq[hmap[num]].append(num)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for val in freq[i]:
                res.append(val)
            if len(res) == k: return res
