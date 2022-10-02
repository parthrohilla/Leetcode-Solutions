class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        memo = [[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        def dfs(i, j):
            if i < 0: return j+1
            if j < 0: return i+1
            if memo[i][j] != -1: return memo[i][j]
            
            if word1[i] == word2[j]: memo[i][j] = dfs(i-1, j-1)
            else: memo[i][j] = 1 + min(dfs(i,j-1), dfs(i-1,j-1), dfs(i-1,j))
            return memo[i][j]
        return dfs(m-1,n-1)