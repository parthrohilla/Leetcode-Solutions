# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if self.length(head) < k:
            return head
        
        temp = head
        for _ in range(k-1):
            temp = temp.next
        
        small = self.reverseKGroup(temp.next, k)
        temp.next = None
        
        updatedPart = self.reverse(head)
        head.next = small
        return updatedPart
    
    def length(self, head):
        if not head:
            return 0
        return 1 + self.length(head.next)
    
    def reverse(self, head):
        if not head or not head.next:
            return head
        small = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return small
        