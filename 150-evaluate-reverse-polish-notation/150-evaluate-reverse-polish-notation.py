class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for char in tokens:
            if char == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a+b)
            elif char == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif char == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a*b)
            elif char == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(char))
        
        return stack[0]
                
            