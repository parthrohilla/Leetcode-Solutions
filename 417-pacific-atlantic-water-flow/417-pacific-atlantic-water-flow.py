class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic, pacific = set(), set()
        m, n = len(heights), len(heights[0])
        
        def dfs(r, c, visited, prev):
            if r < 0 or c < 0 or r >= m or c >= n or prev > heights[r][c] or (r,c) in visited:
                return
            
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            return
        
        
        for j in range(len(heights[0])):
            dfs(0, j, pacific, 0)
            dfs(len(heights)-1, j, atlantic, 0) 
        
        for i in range(len(heights)):
            dfs(i, 0, pacific, 0)
            dfs(i, len(heights[0])-1, atlantic, 0)
        
        return atlantic & pacific
        
        