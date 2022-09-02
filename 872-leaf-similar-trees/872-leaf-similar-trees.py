# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf(root):
            if not root: return []
            if root.left == None and root.right == None: return [root.val]
            else: return leaf(root.left) + leaf(root.right)
        
        return leaf(root1) == leaf(root2)