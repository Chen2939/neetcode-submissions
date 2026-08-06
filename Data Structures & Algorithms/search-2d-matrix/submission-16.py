class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l <= r:
            m = (l+r) // 2
            if matrix[m][-1] < target: l = m + 1
            elif matrix[m][0] > target: r = m - 1
            else: break
        
        le, re = 0, len(matrix[m])-1
        while le <= re:
            me = (le + re) // 2
            res = matrix[m][me]
            if res == target: return True
            elif res > target: re = me - 1
            else: le = me + 1
        return False