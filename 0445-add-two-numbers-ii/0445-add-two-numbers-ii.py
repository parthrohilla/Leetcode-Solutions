# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            if not head or not head.next: return head
            T = reverse(head.next)
            head.next.next = head
            head.next = None
            return T
        
        A = reverse(l1)
        B = reverse(l2)
        C = ListNode(val = -1)
        
        i, j, k, carry = A, B, C, 0
        while i or j:
            X, Y = i.val if i else 0, j.val if j else 0
            S = X + Y + carry
            carry = S // 10
            k.next = ListNode(S % 10)
            i = i.next if i else None
            j = j.next if j else None
            k = k.next
        
        if carry: k.next = ListNode(carry)   
        return reverse(C.next)
            
            