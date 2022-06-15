# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        return self.isValidBST(root.left) and self.isValidBST(root.right) and self.maxOf(root.left) < root.val and root.val < self.minOf(root.right)
            
    
    def maxOf(self, root) -> int:
        if not root:
            return -math.inf
        
        return max(max(self.maxOf(root.left), self.maxOf(root.right)), root.val)
    
    def minOf(self, root) -> int:
        if not root:
            return math.inf
        
        return min(min(self.minOf(root.left), self.minOf(root.right)), root.val)
    
            