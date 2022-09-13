class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        visited = set()
        
        def dfs(i,j):
            if (i,j) in visited: return 1
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] != x: return 0
            
            visited.add((i,j))
            if dfs(i+1,j) + dfs(i,j+1) + dfs(i-1,j) + dfs(i,j-1) < 4:
                grid[i][j] = color
            return 1
            
            
        x =  grid[row][col]
        dfs(row, col)
        return grid
    