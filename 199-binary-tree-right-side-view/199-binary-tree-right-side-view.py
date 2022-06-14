# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        
        if root: q.append(root)
        while len(q) != 0:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                temp = q.popleft()
                if temp.left: q.append(temp.left)
                if temp.right: q.append(temp.right)
                level.append(temp)
            res.append(level[-1].val)
        
        return res
        