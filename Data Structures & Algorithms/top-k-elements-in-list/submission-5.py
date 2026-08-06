class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1
        sorted_hmap = dict(sorted(hmap.items(), key=lambda item: item[1], reverse=True))

        result = []
        for v, c in sorted_hmap.items():
            result.append(v)
            if len(result) == k:
                return result
            