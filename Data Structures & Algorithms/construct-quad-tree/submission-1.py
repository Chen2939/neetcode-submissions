"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, n):
            if n == 1:
                return Node(val=grid[r][c], isLeaf=1)
            
            half = n // 2
            topLeft = dfs(r, c, half)
            topRight = dfs(r, c+half, half)
            bottomLeft = dfs(r+half, c, half)
            bottomRight = dfs(r+half, c+half, half)

            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf 
                and (topLeft.val == topRight.val == bottomLeft.val == bottomRight.val)):
                
                return Node(val=topLeft.val, isLeaf=1)
            
            return Node(val=grid[r][c], isLeaf=0, topLeft=topLeft, topRight=topRight, bottomLeft=bottomLeft, bottomRight=bottomRight)
        
        return dfs(0, 0, len(grid))



            