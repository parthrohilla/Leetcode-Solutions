# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if original == target:
            return cloned
        
        a1 = self.getTargetCopy(original.left, cloned.left, target)
        a2 = self.getTargetCopy(original.right, cloned.right, target)
        if a1:
            return a1
        elif a2:
            return a2
        else:
            return None