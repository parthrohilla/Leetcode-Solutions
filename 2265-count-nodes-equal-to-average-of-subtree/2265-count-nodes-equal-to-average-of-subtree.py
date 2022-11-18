# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node: return [0,0]
            leftSum, leftNodes = dfs(node.left)
            rightSum, rightNodes = dfs(node.right)
            
            S = leftSum + rightSum + node.val
            N = leftNodes + rightNodes + 1
            Avg = S // N
            if Avg == node.val:
                self.ans += 1
                
            return [S,N]
        
        dfs(root)
        return self.ans