# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        
        if not head:
            return head
        
        curr = head.next
        prev = head
        while curr:
            if curr and curr.val == val:
                while curr and curr.val == val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
                   
        return head