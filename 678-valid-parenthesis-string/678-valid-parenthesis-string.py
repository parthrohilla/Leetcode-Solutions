class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for i,char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if not stack and not star: return False
                elif stack: stack.pop()
                elif star: star.pop()
            else:
                star.append(i)
    
        while stack:
            if star and stack[-1] < star[-1]:
                stack.pop()
                star.pop()
            else:
                if not star:
                    return False
                else:
                    star.pop()
        return True
            
            