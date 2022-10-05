# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def dfs(node, h):
            if not node: return
            if h == depth - 1:
                temp1, temp2 = node.left, node.right
                node.left = TreeNode(val)
                node.right = TreeNode(val)
                node.left.left = temp1
                node.right.right = temp2
            
            dfs(node.left, h+1)
            dfs(node.right, h+1)        
                
        if depth == 1: return TreeNode(val,root)
        else: dfs(root, 1)
        return root
            