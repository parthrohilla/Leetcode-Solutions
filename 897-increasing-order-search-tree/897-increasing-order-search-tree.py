# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root: return root
        
        left, right = None, None
        if root.left: left = self.increasingBST(root.left)
        if root.right: right = self.increasingBST(root.right)
        
        dummy = TreeNode(-1)
        dummy.right = left if left else root
        
        tail = left
        while tail and tail.right:
            tail = tail.right
        
        if tail: tail.right = root    
        root.left = None
        root.right = right
        return dummy.right