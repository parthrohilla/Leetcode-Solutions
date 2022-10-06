# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node):
            if not node: return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        def merge(a,b):
            i,j, ans = 0,0, []
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
        
        return merge(inorder(root1), inorder(root2))