class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i,j) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            
            grid[i][j] = -1
            ans = 1 + (dfs(i+1, j)+
                       dfs(i, j+1)+
                       dfs(i-1, j)+
                       dfs(i, j-1))
            return ans
            
        max_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_island = max(max_island, dfs(i, j))
        return max_island
        
        