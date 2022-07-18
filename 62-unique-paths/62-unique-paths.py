class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(i, j):
            if i == m-1 and j == n-1:
                return 1
            if i >= m or j >= n:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            memo[(i,j)] = dfs(i, j+1) + dfs(i+1, j)
            return memo[(i,j)]
        
        return dfs(0, 0)