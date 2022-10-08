class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        memo = {}
        def dfs(i):
            if i == n: return 0
            if i in memo: return memo[i]
            ans = math.inf
            for j in range(i,n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    count = 1 + dfs(j+1)
                    ans = min(ans, count)
            memo[i] = ans
            return ans

        return dfs(0)-1