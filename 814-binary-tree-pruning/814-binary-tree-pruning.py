# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node: return node
            left, right = dfs(node.left), dfs(node.right)
            if node.val == 0 and not left and not right: return None
            if not left: node.left = None
            if not right: node.right = None
            return node
        
        return dfs(root)
                