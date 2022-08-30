class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        visited = [[-1]*n for _ in range(n)]
        directions = [[0,1], [0,-1], [1,0], [-1,0], [-1,-1], [-1,1], [1,-1], [1,1]]
        
        visited[n-1][n-1] = 1
        q = deque()
        q.append((n-1, n-1))
        
        d = 1
        while q:
            d += 1
            k = len(q)
            for _ in range(k):
                x,y = q.popleft()
                for dx, dy in directions:
                    i, j = x+dx, y+dy
                    if i>=0 and i<n and j>=0 and j<n and grid[i][j] == 0 and visited[i][j] == -1:
                        visited[i][j] = d
                        q.append((i,j))
                        if [i,j] == [0,0]:
                            return d
        
        return visited[0][0]
                        