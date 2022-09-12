class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m,n, visited = len(grid), len(grid[0]), set()
        
        def dfs(i,j,px,py):
            visited.add((i,j))
            for dx,dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                x,y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and (x,y) != (px,py) and grid[x][y] == grid[i][j]:
                    if (x,y) in visited: return True
                    if dfs(x,y,i,j): return True        
            return False
                    
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    if dfs(i,j,-1,-1):
                        return True
        return False