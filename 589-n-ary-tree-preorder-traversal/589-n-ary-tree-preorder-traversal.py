"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root:
            return ans
        for child in root.children:
            ans += self.preorder(child)
        return [root.val] + ans