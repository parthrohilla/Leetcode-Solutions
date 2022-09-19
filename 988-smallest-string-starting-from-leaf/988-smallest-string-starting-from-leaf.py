# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node: return []
            if node.left == None and node.right == None: return [chr(ord("a") + node.val)]
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and not right: return [s + chr(ord("a") + node.val) for s in left]
            if right and not left: return [s + chr(ord("a") + node.val) for s in right]
            else: 
                for i,s in enumerate(left): left[i] = s + (chr(ord("a") + node.val))
                for i,s in enumerate(right): right[i] = s + (chr(ord("a") + node.val))
                return left + right
            
        return min(dfs(root))