# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(curr, target, height, parent):
            if not curr: return [-1,-1]
            if curr.val == target: return [height, parent]
            
            [lh,lp] = dfs(curr.left, target, height+1, curr)
            [rh,rp] = dfs(curr.right, target, height+1, curr)
            if (lh,lp) != (-1,-1): return [lh,lp]
            else: return [rh,rp]
        
        [lh,lp] = dfs(root, x, 0, -1)
        [rh,rp] = dfs(root, y, 0, -1)
        if lh == rh and lp != rp: return True
        else: return False