# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(node, P, G):
            if not node: return
            if G and G.val % 2 == 0:
                self.ans += node.val
            dfs(node.left, node, P)
            dfs(node.right, node, P)
                        
        dfs(root, None, None)
        return self.ans