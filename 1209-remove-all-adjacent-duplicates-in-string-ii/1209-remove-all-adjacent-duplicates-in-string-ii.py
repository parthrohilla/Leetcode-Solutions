class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            
            if stack and stack[-1][0] == char:
                last, freq = stack.pop()
                stack.append([char, freq+1])
            else:
                stack.append([char,1])
            
            while stack and stack[-1][1] >= k:
                temp, f = stack.pop()
                if f - k > 0:
                    stack.append([temp,f - k])
                if len(stack) >= 2 and stack[-1][0] == stack[-2][0]:
                    top, f1 = stack.pop()
                    sec, f2 = stack.pop()
                    stack.append([top, f1 + f2])
                    
        ans = ""
        for char, freq in stack:
            ans += char*freq
        return ans
                
            
        