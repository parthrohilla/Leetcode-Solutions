# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node: return 0
            return 1 + max(height(node.left), height(node.right))
        
        def dfs(node, level):
            if not node: return 0
            if level == h: return node.val
            
            res = 0
            if node.left: res += dfs(node.left, level+1)
            if node.right: res += dfs(node.right, level+1)
            return res
        
        h = height(root)
        return dfs(root, 1)