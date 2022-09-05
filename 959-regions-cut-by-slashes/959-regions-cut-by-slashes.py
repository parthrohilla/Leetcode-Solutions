class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        
        def dfs(i, j):
            if i<0 or i>=N or j<0 or j>=N or g[i][j] != 0:
                return
            
            g[i][j] = -1
            for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                x, y = i + dx, j + dy
                dfs(x,y)
            return
        
        g = [[0]*n*3 for _ in range(n*3)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == "/":
                    g[3*i+2][3*j] = g[3*i+1][3*j+1] = g[3*i][3*j+2] = 1
                elif grid[i][j] == "\\":
                    g[3*i][3*j] = g[3*i+1][3*j+1] = g[3*i+2][3*j+2] = 1
        
        #1 - water and 0 - land
        N,count = n*3, 0
        for i in range(N):
            for j in range(N):
                if g[i][j] == 0:
                    dfs(i,j)
                    count += 1
        return count
        