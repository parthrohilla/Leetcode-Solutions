class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        
        def helper(current, openNum, closeNum):
            if len(current) == 2*n:
                output.append(current)
                return
            else:
                if openNum < n:
                    helper(current + "(", openNum+1, closeNum)
                if closeNum < openNum:
                    helper(current + ")", openNum, closeNum+1)
        
        helper("", 0, 0)
        return output
            