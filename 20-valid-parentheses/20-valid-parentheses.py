class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        
        openBrackets = ["(", "{", "["]
        stack = []
        for i, char in enumerate(s):
            if char in openBrackets:
                stack.append(char)
            elif len(stack) == 0:
                return False
            else:
                # some closing type bracket
                pop = stack.pop()
                if char == ")" and pop != "(":
                    return False
                elif char == "}" and pop != "{":
                    print(char)
                    return False
                elif char == "]" and pop != "[":
                    return False
        
        # if never Failed then return True
        return True if len(stack)==0 else False
                
                
                
            
            
        