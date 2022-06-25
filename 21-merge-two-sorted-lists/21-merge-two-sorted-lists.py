# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        
        head = None
        if not temp1 or not temp2:
            if not temp1:
                return temp2
            else:
                return temp1
        
        if temp1 and temp2 and temp1.val < temp2.val:
            head = ListNode(temp1.val)
            temp1 = temp1.next
        elif temp2:
            head = ListNode(temp2.val)
            temp2 = temp2.next
        
        temp3 = head
        while temp1 and temp2:
            if temp1.val < temp2.val:
                temp3.next = ListNode(temp1.val)
                temp3 = temp3.next
                temp1 = temp1.next
            else:
                temp3.next = ListNode(temp2.val)
                temp3 = temp3.next
                temp2 = temp2.next
        
        while temp1:
            temp3.next = ListNode(temp1.val)
            temp3 = temp3.next
            temp1 = temp1.next
            
        while temp2:
            temp3.next = ListNode(temp2.val)
            temp3 = temp3.next
            temp2 = temp2.next
        
        return head
                