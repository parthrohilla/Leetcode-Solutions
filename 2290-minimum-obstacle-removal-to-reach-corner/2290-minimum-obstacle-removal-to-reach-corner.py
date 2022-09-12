class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        q = deque()
        m,n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        heap = [(0,(0,0))]
        visited[0][0] = True
        while heap:
            obs,(i,j) = heapq.heappop(heap)
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                x,y = i + dx, j + dy
                if x in range(m) and y in range(n) and visited[x][y] == False:
                    if x == m-1 and y == n-1:
                        return obs
                    if grid[x][y] == 1:
                        heapq.heappush(heap,[obs+1,(x,y)])
                    else:
                        heapq.heappush(heap,[obs,(x,y)])
                    visited[x][y] = True
        return 0