class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m,n = len(grid1), len(grid1[0])
        
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        def dfs(i, j):
            if grid1[i][j] == 0:
                return False
            
            grid2[i][j] = -1
            res = True
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if x<m and x>=0 and y>=0 and y<n and grid2[x][y] == 1:
                    res = dfs(x,y) and res
            return res
        
        
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        islands += 1
        return islands