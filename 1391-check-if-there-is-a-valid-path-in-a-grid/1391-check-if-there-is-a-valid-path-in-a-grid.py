class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m,n = len(grid), len(grid[0])
        M,N = m*3, n*3
        g = [[0]*N for _ in range(M)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: g[3*i+1][3*j] = g[3*i+1][3*j+1] = g[3*i+1][3*j+2] = 1 
                elif grid[i][j] == 2: g[3*i][3*j + 1] = g[3*i+1][3*j+1] = g[3*i+2][3*j+1] = 1
                elif grid[i][j] == 3: g[3*i+1][3*j] = g[3*i+1][3*j+1] = g[3*i+2][3*j+1] = 1
                elif grid[i][j] == 4: g[3*i+1][3*j+1] = g[3*i+2][3*j+1] = g[3*i+1][3*j+2] = 1
                elif grid[i][j] == 5: g[3*i+1][3*j] = g[3*i+1][3*j+1] = g[3*i][3*j+1] = 1
                else: g[3*i][3*j+1] = g[3*i+1][3*j+1] = g[3*i+1][3*j+2] = 1
        
        def dfs(i,j):
            if i<0 or i>=M or j<0 or j>=N or g[i][j] != 1: return False
            if i>=M-3 and j>=N-3: return True
            
            g[i][j] = 0
            for dx,dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                x,y = i + dx, j + dy
                if dfs(x,y):
                    return True
            return False

        
        for i in range(3):
            for j in range(3):
                if g[i][j] == 1:
                    return dfs(i,j)
        return False
        
        
                    
                    
                    