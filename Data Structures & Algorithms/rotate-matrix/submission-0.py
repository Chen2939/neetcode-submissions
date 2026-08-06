class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix[0]) - 1
        
        while l < r:
            for i in range(r - l):
                top, bot = l, r
                # save the top left
                topLeft = matrix[top][l + i]

                # move bot left into top left
                matrix[top][l + i] = matrix[bot - i][l]
                # move bot right to bot left
                matrix[bot - i][l] = matrix[bot][r - i]
                # move top right to bot right
                matrix[bot][r - i] = matrix[top + i][r]
                # move top left to top right
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1
        