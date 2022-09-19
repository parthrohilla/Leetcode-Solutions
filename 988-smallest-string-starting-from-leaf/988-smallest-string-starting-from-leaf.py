# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.res = None
        def dfs(root, s):
            if not root: return ""
        
            s += chr(ord('a') + root.val)
            if not root.left and not root.right:
                if not self.res: self.res = s[::-1]
                else: self.res = min(self.res, s[::-1])
            if root.left: dfs(root.left, s)
            if root.right: dfs(root.right, s)
                
        dfs(root, '')
        return self.res