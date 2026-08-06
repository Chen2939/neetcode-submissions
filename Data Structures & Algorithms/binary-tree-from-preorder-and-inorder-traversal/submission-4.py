# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. Hashtable to store inorder value: index
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        # 2. Record where in preorder we are at
        preorder_index = 0
        # 3. Here left, right are boundaries for inorder
        def array_to_tree(left, right):
            nonlocal preorder_index
            # OOB
            if left > right: return

            # start from preorder
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)
            preorder_index += 1

            # get mid from index of curr node at inorder
            mid = inorder_map[root_val]

            root.left = array_to_tree(left, mid - 1)
            root.right = array_to_tree(mid + 1, right)
            return root
        
        return array_to_tree(0, len(inorder)-1)

