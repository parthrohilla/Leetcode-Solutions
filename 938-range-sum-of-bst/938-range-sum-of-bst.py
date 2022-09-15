# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, n: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if not root: return 0
            small = 0
            if root.left and not (low > root.val): small += dfs(root.left)
            if root.right and not (high < root.val): small += dfs(root.right)
            if root.val <= high and root.val >= low: small += (root.val)
            return small
        return dfs(n)