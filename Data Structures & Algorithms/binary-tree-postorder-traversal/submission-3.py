# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root

        while curr:
            if not curr.right:
                res.append(curr.val)
                curr = curr.left
            
            else:
                pre = curr.right
                while pre.left and pre.left != curr:
                    pre = pre.left
                
                if not pre.left:
                    res.append(curr.val)
                    pre.left = curr
                    curr = curr.right
                else:
                    pre.right = None
                    curr = curr.left
        
        res.reverse()
        return res