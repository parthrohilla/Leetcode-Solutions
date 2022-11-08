class Solution:
    def makeGood(self, s: str) -> str:
        K = ord("a") - ord("A")
        stack = []
        
        i = 0
        while i < len(s):
            
            stack.append(s[i])
            i += 1
            
            while stack and len(stack) >= 2 and abs(ord(stack[-1]) - ord(stack[-2])) == K:
                stack.pop()
                stack.pop()
   

        return "".join(stack)
            
        