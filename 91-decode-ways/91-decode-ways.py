class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def helper(string) -> int:
            if not string:
                return 1
            if string[0] == "0":
                return 0
            if string in memo:
                return memo[string]
            
            op1, op2 = 0, 0
            op1 = helper(string[1:])
            if len(string) >= 2 and int(string[:2]) <= 26:
                op2 = helper(string[2:])
            memo[string] = op1 + op2
            return op1 + op2
                    
        return helper(s)