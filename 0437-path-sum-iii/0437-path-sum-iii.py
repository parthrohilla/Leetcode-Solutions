# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        
        def dfs(node, S, parent_taken):
            if not node:
                return
            
            if node.val + S == targetSum:
                self.ans += 1
            
            if parent_taken:
                dfs(node.left, S + node.val, parent_taken)
                dfs(node.right, S + node.val, parent_taken)
            else:
                dfs(node.left, S + node.val, True)
                dfs(node.right, S + node.val, True)
                dfs(node.left, S, False)
                dfs(node.right, S, False)
        
        dfs(root, 0, False)
        return self.ans