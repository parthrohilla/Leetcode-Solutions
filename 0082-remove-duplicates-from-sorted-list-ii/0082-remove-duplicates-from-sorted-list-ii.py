# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        dummy = ListNode(0, head)
        slow, fast = dummy, head.next
        
        while fast and slow.next:
            if slow.next.val == fast.val:
                while fast.next and fast.next.val == slow.next.val: fast = fast.next
                slow.next = fast.next
                fast = fast.next.next if fast.next else None
            else:
                slow = slow.next
                fast = fast.next
        
        return dummy.next
            
        