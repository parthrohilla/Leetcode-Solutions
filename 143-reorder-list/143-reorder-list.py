# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        l1, l2 = head, self.reverse(slow.next)
        slow.next = None
        
        flag = 0
        dummy = ListNode()
        x = dummy
        while l1 and l2:
            if flag % 2 == 0:
                x.next = l1
                l1 = l1.next
            else:
                x.next = l2
                l2 = l2.next
            flag += 1
            x = x.next
        
        if l1:
            x.next = l1
        else:
            x.next = l2
            
        return dummy.next
    
    def reverse(self, head):
        if not head or not head.next:
            return head
        small = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return small
                
                
                
        