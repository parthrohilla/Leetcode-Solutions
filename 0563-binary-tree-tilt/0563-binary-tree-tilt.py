# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return [0,0]
            left, sumL = dfs(node.left)
            right, sumR = dfs(node.right)
            return [left + right + abs(sumL - sumR), node.val + sumL + sumR]
        
        return dfs(root)[0]