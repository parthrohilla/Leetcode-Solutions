class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1), len(text2)
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    if i-1 >= 0 and j-1 >= 0:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = 1
                else:
                    temp1, temp2 = 0,0
                    if i-1 >= 0: temp1 = dp[i-1][j]
                    if j-1 >= 0: temp2 = dp[i][j-1]
                    dp[i][j] = max(temp1, temp2)
        return dp[m-1][n-1]