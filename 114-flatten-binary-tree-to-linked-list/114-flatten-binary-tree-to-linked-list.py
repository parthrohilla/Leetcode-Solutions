# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            if not node: return [node,node]
            left, tailL = dfs(node.left)
            right, tailR = dfs(node.right)
            
            if left: node.right = left
            if tailL: tailL.right = right
            node.left = None
            
            tail = node
            while tail.right: tail = tail.right
            return [node, tail]
        
        return dfs(root)[0]
            
        