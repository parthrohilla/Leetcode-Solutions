class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i, current):
            if current == t:
                return 1
            if len(current)-1 >= 0 and current[len(current)-1] != t[len(current)-1]:
                return 0
            if i >= len(s):
                return 0
            if (i, current) in memo:
                return memo[(i, current)]
            
            memo[(i, current)] = dfs(i+1, current + s[i]) + dfs(i+1, current)
            return memo[(i, current)]
        
        return dfs(0, "")
            
            