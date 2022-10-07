class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        
        maxi = 0
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0) and matrix[i][j] == "1":
                    dp[i][j] = 1    
                elif matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                maxi = max(maxi, dp[i][j])
        return maxi**2
                    