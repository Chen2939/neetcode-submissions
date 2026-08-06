"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        hmap = {} # old: new
        def dfs(n):
            if n in hmap:
                return hmap[n]
            newNode = Node(n.val)
            hmap[n] = newNode

            for nei in n.neighbors:
                newNode.neighbors.append(dfs(nei))
            
            return newNode
        return dfs(node)