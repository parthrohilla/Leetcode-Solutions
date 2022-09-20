class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n, memo = len(grid), len(grid[0]), {}
        def dfs(i,j):
            if i== m-1 and j == n-1: return grid[i][j]
            if i >=m or j >=n: return math.inf
            if (i,j) in memo: return memo[(i,j)]
            memo[(i,j)] = grid[i][j] + min(dfs(i+1,j), dfs(i,j+1))
            return memo[(i,j)]
        return dfs(0,0)