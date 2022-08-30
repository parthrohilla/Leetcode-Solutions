class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] != 1:
                return
            
            grid[i][j] = -1
            for dx, dy in directions:
                x, y = i + dx, j + dy
                dfs(x,y)
            return
        
        
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    dfs(i, j)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
        return count
                    