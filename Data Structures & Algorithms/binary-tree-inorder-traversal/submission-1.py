# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root

        # When node not null or still unprocessed node in stack
        while curr or stack:
            # Go all the way left
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Always handle the leftist
            curr = stack.pop()
            res.append(curr.val)

            # Now go right
            curr = curr.right
        return res