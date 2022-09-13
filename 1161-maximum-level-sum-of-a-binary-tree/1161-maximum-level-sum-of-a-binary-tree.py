# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        val, q, level_sum, max_sum, level, ans = 0, deque(), 0, -math.inf, 0, 1
        q.append(root)
        
        while q:
            level_sum = 0
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
            if level_sum > max_sum:
                max_sum = level_sum
                ans = level
        return ans