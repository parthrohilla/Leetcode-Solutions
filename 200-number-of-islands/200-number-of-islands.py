class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set() 
        
        def bfs(i, j):
            q = deque()
            visited.add((i,j))
            q.append((i, j))
            while q:
                r,c = q.popleft()
                directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                for rx, ry in directions:
                    row, col = r + rx, c + ry
                    if row>=0 and row<m and col>=0 and col<n and grid[row][col] == "1" and (row,col) not in visited:
                        q.append((row,col))
                        visited.add((row,col))
                        
                        
        
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands