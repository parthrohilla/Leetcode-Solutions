# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def length(head):
            if not head:
                return 0
            return 1 + length(head.next)
        
        def merge(head1, head2):
            dummy = ListNode()
            t1, t2 = head1, head2
            curr = dummy
            while t1 and t2:
                if t1.val < t2.val:
                    curr.next = ListNode(t1.val)
                    t1 = t1.next
                    curr = curr.next
                else:
                    curr.next = ListNode(t2.val)
                    t2 = t2.next
                    curr = curr.next
            
            if t1:
                curr.next = t1
            
            if t2:
                curr.next = t2
                
            return dummy.next
                      
        def sort(head):
            if not head or not head.next:
                return head
            
            n = length(head)
            tail = head
            for _ in range(n//2-1):
                tail = tail.next
            
            list1 = sort(tail.next)
            tail.next = None
            list2 = sort(head)
            return merge(list1, list2)
        
        
        return sort(head)