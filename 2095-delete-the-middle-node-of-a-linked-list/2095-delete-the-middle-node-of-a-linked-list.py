# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n, dummy = self.length(head), ListNode(-1, head)
        curr = dummy
        
        for _ in range(n//2): 
            curr = curr.next
            
        curr.next = curr.next.next
        return dummy.next
    
    def length(self, head):
        if not head: return 0
        return 1 + self.length(head.next)