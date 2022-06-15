# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = self.inOrder(root)
        
        for i in range(len(output)-1):
            if output[i]>=output[i+1]:
                return False
        return True
    
    def inOrder(self, root):
        if not root:
            return []
        
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)