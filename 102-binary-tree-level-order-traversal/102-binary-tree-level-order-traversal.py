# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        res = []
            
        if root: q.append(root)
        while len(q) != 0:
            qLen = len(q)
            level = []
            for i in range(qLen):
                temp = q.popleft()
                if temp:
                    level.append(temp.val)
                    if temp.left: q.append(temp.left) 
                    if temp.right: q.append(temp.right) 
            res.append(level)
            
        return res