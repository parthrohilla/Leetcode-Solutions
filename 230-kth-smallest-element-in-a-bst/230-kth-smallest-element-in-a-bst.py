# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = self.inOrder(root, [])
        return output[k-1]
    
    def inOrder(self, root, ans):
        if not root:
            return []
        
        self.inOrder(root.left, ans)
        ans.append(root.val)
        self.inOrder(root.right, ans)
        return ans