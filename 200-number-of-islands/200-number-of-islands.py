class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if i not in range(m) or j not in range(n) or grid[i][j] != "1":
                return
            
            grid[i][j] = "-1"
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        
        return islands
        