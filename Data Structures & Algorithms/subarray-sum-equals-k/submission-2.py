class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = {0:1}
        res, sums = 0, 0

        for n in nums:
            sums += n
            diff = sums - k
            res += hmap.get(diff, 0)
            hmap[sums] = 1 + hmap.get(sums, 0)
        return res