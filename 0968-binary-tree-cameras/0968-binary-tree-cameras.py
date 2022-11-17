# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cameras = 0
        
        def dfs(node):
            if not node:
                return "covered"
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == "covered" and right == "covered":
                return "to_be_covered"
            
            if left == "to_be_covered" or right == "to_be_covered":
                self.cameras += 1
                return "covering"
            
            if left == "covering" or right == "covering":
                return "covered"

        return (dfs(root)=='to_be_covered') + self.cameras
            
            
            
            