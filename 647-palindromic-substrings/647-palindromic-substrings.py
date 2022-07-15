class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        dp = [[0]*n for _ in range(n)]
        
        for diff in range(n):
            i, j = 0, diff
            while j<n and i<n-diff:
                if i == j:
                    dp[i][j] = 1
                elif diff == 1:
                    dp[i][j] = 2 if s[i] == s[j] else 0
                else:
                    dp[i][j] = 2 + dp[i+1][j-1] if (dp[i+1][j-1] and s[i] == s[j]) else 0
                        
                if dp[i][j]:
                    ans += 1
                i += 1
                j += 1
        return ans