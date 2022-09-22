class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m,n = len(grid), len(grid[0])
        
        def dfs(i,j):
            if i == m: return j
            if j+1 < n and grid[i][j] == 1 and grid[i][j+1] == 1: return dfs(i+1,j+1)
            if j-1 >= 0 and grid[i][j] == -1 and grid[i][j-1] == -1: return dfs(i+1, j-1)
            else: return -1
        
        ans = []
        for j in range(n):
            ans.append(dfs(0,j))
        return ans