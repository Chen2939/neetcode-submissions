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
                is_val_true = (grid[r][c]==1)
                return Node(is_val_true, True)
            
            # post order, construct 4 child tree
            half = n // 2
            topleft = dfs(r, c, half)
            topright = dfs(r, c + half, half)
            bottomleft = dfs(r + half, c, half)
            bottomright = dfs(r + half, c + half, half)\

            # check if can merge to node: when all leaf, and same value
            if (topleft.isLeaf and topright.isLeaf and bottomleft.isLeaf and bottomright.isLeaf and
                topleft.val == topright.val == bottomleft.val == bottomright.val):
                return Node(topleft.val, True)
            
            # if cant merge, means have both 1 and 0, isLeaf is false
            return Node(False, False, topleft, topright, bottomleft, bottomright)
        
        return dfs(0, 0, len(grid))