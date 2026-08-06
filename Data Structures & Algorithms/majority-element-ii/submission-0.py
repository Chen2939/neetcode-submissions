class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hmap = defaultdict(int)

        for n in nums:
            hmap[n] = 1 + hmap.get(n, 0)
            if not len(hmap) > 2:
                continue

            new_hmap = defaultdict(int)
            for n, c in hmap.items():
                if c > 1:
                    new_hmap[n] = c - 1
            hmap = new_hmap

        res = []
        for n in hmap:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res