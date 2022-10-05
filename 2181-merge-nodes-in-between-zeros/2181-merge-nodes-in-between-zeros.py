# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail,temp = head, head.next
        while temp:
            s = 0
            while temp.val != 0:
                s += temp.val
                temp = temp.next
            tail.next = ListNode(s)
            tail, temp = tail.next, temp.next
        return head.next
        