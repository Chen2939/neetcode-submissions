# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        insertNode = TreeNode(val=val)
        if not root: return insertNode
        
        def dfs(node, parentNode=None, flag=0):

            if not node:
                if flag == 1:
                    parentNode.right = insertNode
                elif flag == -1:
                    parentNode.left = insertNode
                else: return
            else:
                if insertNode.val > node.val:
                    dfs(node.right, node, 1)
                else:
                    dfs(node.left, node, -1)
             
        dfs(root, root)
        return root