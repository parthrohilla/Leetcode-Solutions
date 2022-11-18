# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(A):
            if not A: return None
            i, num = max(enumerate(A), key = lambda x: x[1])
            root = TreeNode(num, dfs(A[:i]), dfs(A[i+1:]))
            return root
        
        return dfs(nums)
        