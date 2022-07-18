class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        sx, sy, fx, fy = -1, -1, -1, -1
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx, sy = i, j
                elif grid[i][j] == 0:
                    count += 1
                    
        def dfs(i, j, steps):
            if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] == -1:
                return 0
            if grid[i][j] == 2:
                if steps == -1:
                    return 1
                else:
                    return 0
                
            
            grid[i][j] = -1
            ans = (dfs(i, j+1, steps-1)+
                   dfs(i, j-1, steps-1)+
                   dfs(i-1, j, steps-1)+
                   dfs(i+1, j, steps-1))
            grid[i][j] = 0
            return ans
        
        return dfs(sx, sy, count)
