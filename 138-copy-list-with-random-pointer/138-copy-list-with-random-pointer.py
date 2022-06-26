"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapToCopy = {}
        mapToCopy[None] = None
        
        temp = head
        while temp:
            newNode = Node(temp.val)
            mapToCopy[temp] = newNode
            temp = temp.next
        
        temp = head
        while temp:
            curr = mapToCopy[temp]
            curr.next = mapToCopy[temp.next]
            curr.random = mapToCopy[temp.random]
            temp = temp.next
        
        return mapToCopy[head]