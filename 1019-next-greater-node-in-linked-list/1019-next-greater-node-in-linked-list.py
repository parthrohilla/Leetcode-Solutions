# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        def length(head):
            if not head:
                return 0
            return 1 + length(head.next)
        
        i = 1
        n = length(head)
        ans = [0] * n
        stack = [[head.val, 0]]
        head = head.next
        while head:
            num = head.val
            if num <= stack[-1][0]:
                stack.append([num, i])
            else:
                while stack and num > stack[-1][0]:
                    top = stack.pop()
                    ans[top[1]] = num
                stack.append([num, i])
            i += 1
            head = head.next
        return ans
                    
                