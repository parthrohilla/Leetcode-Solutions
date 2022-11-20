class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        print("2".isdigit())
        for c in operations:
            if c.isdigit() or c[1:].isdigit(): stack.append(int(c))
            if c == "+": stack.append(stack[-1] +stack[-2])
            if c == "D": stack.append(stack[-1]*2)
            if c == "C": stack.pop()     
        return sum(stack)