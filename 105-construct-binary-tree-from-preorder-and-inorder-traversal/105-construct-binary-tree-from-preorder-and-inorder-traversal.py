# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        if len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0])
        
        root = preorder[0]
        index = -1
        for i,num in enumerate(inorder):
            if root == num:
                index = i
        
        leftTree = self.buildTree(preorder[1:index+1], inorder[:index])
        rightTree = self.buildTree(preorder[index+1:], inorder[index+1:])
        
        return TreeNode(root, leftTree, rightTree)