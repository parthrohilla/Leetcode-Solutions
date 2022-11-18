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
            i, num = largest(A)
            L = dfs(A[:i])
            R = dfs(A[i+1:])
            root = TreeNode(num, L, R)
            return root
        
        def largest(A):
            m = [0,-math.inf]
            for i, num in enumerate(A):
                if num > m[1]:
                    m[0] = i
                    m[1] = num
            return m
        
        return dfs(nums)
        