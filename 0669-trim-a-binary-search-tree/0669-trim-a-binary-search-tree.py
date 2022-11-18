# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node: return
            L, R = dfs(node.left), dfs(node.right)
            if node.val < low: return R
            elif node.val > high: return L
            node.left = L
            node.right = R
            return node

        return dfs(root)