class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n, q, level = len(grid), len(grid[0]), deque(), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    q.append((i,j))
                else:
                    grid[i][j] = -1
        
        if len(q) == m*n:
            return -1
        
        while q:
            level += 1
            for _ in range(len(q)):
                i,j = q.popleft()
                for dx,dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                    x,y = i + dx, j + dy
                    if 0<= x < m and 0<= y <n and grid[x][y] == -1:
                        grid[x][y] = level
                        q.append((x,y))
        
        return max([max(row) for row in grid])
        