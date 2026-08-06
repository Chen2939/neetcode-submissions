class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l+r) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                break
        # return false if we cross out every single row
        if not (l <= r):
            return False
        
        mid = (l+r) // 2
        le, re = 0, len(matrix[mid]) - 1
        while le <= re:
            mide = (le+re) // 2
            if matrix[mid][mide] > target:
                re = mide - 1
            elif matrix[mid][mide] < target:
                le = mide + 1
            else:
                return True
        
        return False