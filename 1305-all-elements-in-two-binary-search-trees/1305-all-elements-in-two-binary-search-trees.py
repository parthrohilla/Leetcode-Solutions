# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def preorder(node):
            if not node: return []
            return preorder(node.left) + [node.val] + preorder(node.right)
        
        def merge(a,b):
            i,j = 0,0
            ans = []
            while i<len(a) and j<len(b):
                if a[i] < b[j]:
                    ans.append(a[i])
                    i += 1
                else:
                    ans.append(b[j])
                    j += 1
            
            if i < len(a): ans += a[i:]
            if j < len(b): ans += b[j:]
            return ans
        
        return merge(preorder(root1), preorder(root2))