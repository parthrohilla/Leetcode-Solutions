# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)
        
        temp = self.depth(root.left) + self.depth(root.right) 
        return max(max(leftDiameter, rightDiameter), temp)
    
    def depth(self, root) -> int:
        if root == None:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))