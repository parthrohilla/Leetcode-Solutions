class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        dp = [[False]*n for _ in range(n)]
        
        for diff in range(n):
            i, j = 0, diff
            while j<n and i<n-diff:
                if i == j:
                    dp[i][j] = True
                elif diff == 1:
                    dp[i][j] = True if s[i] == s[j] else False
                else:
                    dp[i][j] = True if (dp[i+1][j-1] and s[i] == s[j]) else False
                        
                if dp[i][j]:
                    ans += 1
                i += 1
                j += 1
        return ans