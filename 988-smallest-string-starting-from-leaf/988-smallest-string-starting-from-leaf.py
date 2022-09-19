# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def dfs(root, s):
            s = s + chr(ord('a') + root.val)
            if not root.left and not root.right:
                if res[0] == None:
                    res[0] = s[::-1]
                else:
                    res[0] = min(res[0], s[::-1])
            if root.left:
                dfs(root.left, s)
            if root.right:
                dfs(root.right, s)
        
        if not root:
            return ''
        res = [None]
        dfs(root, '')
        return res[0]