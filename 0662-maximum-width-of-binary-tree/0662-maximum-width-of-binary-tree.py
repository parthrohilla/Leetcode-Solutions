# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        Q = deque()
        Q.append([0,root])
        ans = 0
        
        while Q:
            k = len(Q)
            ans = max(ans, Q[-1][0] - Q[0][0] + 1)
            for _ in range(k):
                i, node = Q.popleft()
                if node.left: Q.append([2*i+1,node.left])
                if node.right: Q.append([2*i+2, node.right])            
        return ans

        
            
            