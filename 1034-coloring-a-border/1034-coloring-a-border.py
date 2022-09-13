class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m,n,visited = len(grid), len(grid[0]), set()
        def dfs(i,j):
            if (i,j) in visited: return 1
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] != color_old: return 0
            
            visited.add((i,j))
            if dfs(i+1,j) + dfs(i,j+1) + dfs(i-1,j) + dfs(i,j-1) < 4:
                grid[i][j] = color
            return 1
                
        color_old =  grid[row][col]
        dfs(row, col)
        return grid
    