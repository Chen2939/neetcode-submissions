class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            new_perm = []
            for r in res:
                for i in range(len(r)+1):
                    r_copy = r.copy()
                    r_copy.insert(i, n)
                    new_perm.append(r_copy)
            res = new_perm
        return res