class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])
        if m == 1 and n == 1: return 0 if k>=1 else -1
        q, visited = deque(), set()
        q.append((0,0,0,0))
        visited.add((0,0,0))
        while q:
            i,j,obs,dist = q.popleft()
            for dx,dy in [[0,1], [1,0], [-1,0], [0,-1]]:
                x,y = i+dx, j+dy
                if x>=0 and x<m and y>=0 and y<n and (x,y,obs+(grid[x][y] & 1)) not in visited:
                    if x == m-1 and y == n-1:
                        return dist+1
                    if grid[x][y] == 1 and obs >= k:
                        continue
                    else:
                        q.append((x,y,obs+(grid[x][y] & 1),dist+1))
                        visited.add((x,y,obs+(grid[x][y] & 1)))
        return -1