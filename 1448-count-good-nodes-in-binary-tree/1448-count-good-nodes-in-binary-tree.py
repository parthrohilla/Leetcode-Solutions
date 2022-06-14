# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.helper(root, root.val)
    
    def helper(self, root, maxValue) -> int:
        if not root:
            return 0
        
        maxValue = max(maxValue, root.val)
        if maxValue <= root.val:
            return 1 + self.helper(root.left, maxValue) + self.helper(root.right, maxValue)
        else:
            return self.helper(root.left, maxValue) + self.helper(root.right, maxValue)