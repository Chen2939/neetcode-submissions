class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for n in nums:
            hmap[n] = 1 + hmap.get(n, 0)

        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in hmap.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res