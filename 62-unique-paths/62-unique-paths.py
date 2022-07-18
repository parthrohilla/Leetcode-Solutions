class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 or j == n-1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j+1] + dp[i+1][j]
        return dp[0][0]
                