# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        
        def dfs(node, S):
            if not node:return
            if S + node.val == targetSum: self.ans += 1
            dfs(node.left, S + node.val)
            dfs(node.right, S + node.val)
            
        def dfs_starter(node):
            if not node: return
            dfs(node, 0)
            dfs_starter(node.left)
            dfs_starter(node.right)
        
        dfs_starter(root)
        return self.ans