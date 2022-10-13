# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.ans, self.n = [], n
        return self.build_bst(1,n)
    
    def build_bst(self, start, end):
        trees = []
        if start > end: return [None]
        if start == end: return [TreeNode(start)]
        
        for i in range(start, end+1):
            leftTrees = self.build_bst(start,i-1)
            rightTrees = self.build_bst(i+1, end)
            
            for lroot in leftTrees:
                for rroot in rightTrees:
                    root = TreeNode(i, lroot, rroot)
                    trees.append(root)
        
        return trees
            
        
        
            
            
        
        
            
        
        