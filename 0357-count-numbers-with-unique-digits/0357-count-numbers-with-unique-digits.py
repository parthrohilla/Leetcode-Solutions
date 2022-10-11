class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def dfs(n):
            if n == 0: return 1
            res, options = 9, 9
            for _ in range(n-1):
                res *= options
                options -= 1
            res += dfs(n-1)
            return res
        
        return dfs(n)