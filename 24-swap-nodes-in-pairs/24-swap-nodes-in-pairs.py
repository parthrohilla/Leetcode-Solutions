# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def length(head):
            if not head:
                return 0
            return 1 + length(head.next)
        
        n = length(head)
        if n < 2:
            return head
        
        small = self.swapPairs(head.next.next)
        
        temp = head
        head = head.next
        head.next = temp
        head.next.next = small
        return head