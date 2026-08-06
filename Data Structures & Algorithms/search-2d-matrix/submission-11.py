class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l, r = 0, len(matrix[i]) - 1
            while l <= r:
                mid = l + (r-l) // 2
                if matrix[i][mid] < target:
                    l = mid + 1
                elif matrix[i][mid] > target:
                    r = mid - 1
                else:
                    return True
        return False 