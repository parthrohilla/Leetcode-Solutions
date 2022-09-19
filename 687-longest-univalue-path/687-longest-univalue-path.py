# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.ans = 0
        # dfs() returns the longest path starting from the current node 
        def dfs(node):
            temp1, temp2 = 0,0
            if node.left: temp1 = dfs(node.left)
            if node.right: temp2 = dfs(node.right)
            # Taking care of all the conditions if we need to combine results from left sub-tree or right sub-tree or from neither
            if node.left and node.right and node.val == node.left.val and node.val == node.right.val:
                self.ans = max(self.ans, 2 + temp1 + temp2)
                return 1 + max(temp1, temp2)
            elif node.left and node.left.val == node.val:
                self.ans = max(self.ans, 1 + temp1)
                return 1 + temp1
            elif node.right and node.right.val == node.val:
                self.ans = max(self.ans, 1 + temp2)
                return 1 + temp2
            else:
                return 0
        
        dfs(root)
        return self.ans