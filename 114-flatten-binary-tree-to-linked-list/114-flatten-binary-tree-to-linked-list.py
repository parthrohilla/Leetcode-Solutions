# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # dfs() returns head(ROOT) and Tail of the list
        def dfs(node):
            if not node: 
                return [node,node]
            # Recursve Calls on Left Sub-tree and Right Sub-Tree
            left, tailL = dfs(node.left)
            right, tailR = dfs(node.right)
             # Combine the risult of left subTree into the Right Half to "flatten it"
             # ROOT 
             #    \
             #     \         
             #      \
             #    [Left sub-Tree HEAD]
             #        \             
             #         \
             #          \  
             #        [Left sub-Tree TAIL]
             #            \
             #             \  
             #              \
             #        [Right sub-Tree flattened result] 
            if left: node.right = left
            if tailL: tailL.right = right
            node.left, tail = None, node
            while tail.right: tail = tail.right
            return [node, tail]
        return dfs(root)[0]
            
        