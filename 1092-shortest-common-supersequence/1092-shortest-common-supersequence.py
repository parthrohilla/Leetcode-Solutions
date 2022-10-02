class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m,n = len(str1), len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
                else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        ans = ""
        i,j = m,n
        while i and j:
            if str1[i-1] == str2[j-1]:
                ans += str1[i-1]
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                ans += str1[i-1]
                i -= 1
            else:
                ans += str2[j-1]
                j -= 1
        
        if i: ans += str1[:i][::-1]
        elif j: ans += str2[:j][::-1]
        return ans[::-1]
                
                    