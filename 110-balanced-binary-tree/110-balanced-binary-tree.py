# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None: return True
        
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.height(root.left)-self.height(root.right))<=1
    
    def height(self, root) -> int:
        if root == None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))