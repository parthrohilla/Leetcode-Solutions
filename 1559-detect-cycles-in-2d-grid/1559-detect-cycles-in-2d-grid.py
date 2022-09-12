class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m,n = len(grid), len(grid[0])
        visited = set()
        
        def dfs(i,j,px,py):
            visited.add((i,j))
            for dx,dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                x,y = i + dx, j + dy
                if x>=0 and x<m and y>=0 and y<n and (x,y) != (px,py) and grid[x][y] == grid[i][j]:
                    if (x,y) in visited:
                        return True
                    if dfs(x,y,i,j):
                        return True
                    
            return False
                    
        
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    if dfs(i,j,-1,-1):
                        return True
        return False