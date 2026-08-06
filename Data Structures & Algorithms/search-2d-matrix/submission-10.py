class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        # If we create a invalid condition, return False
        # We cross out every single row and none contains the case
        if not (top <= bot):
            return False
        
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        # while l <= r:
        #     mid = (l+r) // 2
        #     if matrix[row][mid] > target:
        #         r = mid - 1
        #     elif matrix[row][mid] < target:
        #         l = mid + 1
        #     else: return True
        while l <= r:
            m = (l+r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True

        return False