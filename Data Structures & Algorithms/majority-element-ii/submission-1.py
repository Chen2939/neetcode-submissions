class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hmap = {}
        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1
            if not len(hmap) > 2: continue
        
            newMap = {}
            for num, count in hmap.items():
                if count > 1:
                    newMap[num] = count - 1
            
            hmap = newMap
        
        res = []
        for n in hmap:
            if nums.count(n) > len(nums) // 3:
                res.append(n)
        return res