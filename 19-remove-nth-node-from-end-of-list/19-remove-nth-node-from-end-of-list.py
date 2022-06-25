# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = self.length(head)
        
        if k == 1 and n>=1:
            return None
        if n-k == 0:
            return head.next
        
        temp = head
        for i in range(k-n-1):
            temp = temp.next
            
        temp.next = temp.next.next
        return head
    
    def length(self, head):
        if not head:
            return 0
        return 1 + self.length(head.next)