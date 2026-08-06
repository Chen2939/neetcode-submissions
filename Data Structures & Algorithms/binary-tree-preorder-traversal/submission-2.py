# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, curr = [], root

        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                
                if not pre.right:
                    res.append(curr.val)
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    curr = curr.right

        return res 