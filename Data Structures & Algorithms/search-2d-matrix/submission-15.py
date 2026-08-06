class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Instead of using bs for each row, 
        # bs the rows to find potential row that has target
        l, r = 0, len(matrix)-1
        while l <= r:
            m = (l+r)//2
            if target < matrix[m][0]: r = m-1
            elif target > matrix[m][-1]: l = m+1
            else: break

        mat = matrix[m]
        le, re = 0, len(mat)-1
        while le <= re:
            me = (le+re) // 2
            if target == mat[me]: return True
            elif target > mat[me]: le = me + 1
            else: re = me - 1

        return False 