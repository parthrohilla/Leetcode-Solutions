"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root:
            return ans
        
        for node in root.children:
            ans += self.postorder(node)
        return ans + [root.val]