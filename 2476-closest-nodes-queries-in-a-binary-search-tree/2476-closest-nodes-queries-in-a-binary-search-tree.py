# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        
        def inorder(node):
            if node: inorder(node.left), A.append(node.val), inorder(node.right)
        
        A, ans = [], []
        inorder(root)
        N = len(A)
        
        for q in queries:
            i = bisect_left(A,q)
            if i < N and A[i] == q: ans.append([q,q])
            else:
                if i == 0: ans.append([-1, A[i]])
                elif i == N: ans.append([A[-1], -1])
                else: ans.append([A[i-1], A[i]])
        
        return ans
        