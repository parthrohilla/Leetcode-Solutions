# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            if not head or not head.next: return head
            small = reverse(head.next)
            head.next.next = head
            head.next = None
            return small
        
        A = reverse(l1)
        B = reverse(l2)
        C = ListNode(val = -1)
        
        i, j, k = A, B, C
        carry = 0
        while i and j:
            S = i.val + j.val + carry
            carry = S // 10
            k.next = ListNode(S % 10)
            i = i.next
            j = j.next
            k = k.next
        
        while i:
            S = i.val + carry
            carry = S // 10
            k.next = ListNode(S % 10)
            i = i.next
            k = k.next
        
        while j:
            S = j.val + carry
            carry = S // 10
            k.next = ListNode(S % 10)
            j = j.next
            k = k.next
        
        if carry:
            k.next = ListNode(carry)
            
        return reverse(C.next)
            
            