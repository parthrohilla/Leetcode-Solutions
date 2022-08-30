"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        ans = 0
        for node in root.children:
            ans = max(ans, self.maxDepth(node))
        return 1 + ans