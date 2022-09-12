class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        q,m,n = deque(), len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        heap, visited[0][0] = [(0,(0,0))], True
        while heap:
            obs,(i,j) = heapq.heappop(heap)
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                x,y = i + dx, j + dy
                if x>=0 and x<m and y>=0 and y<n and visited[x][y] == False:
                    if x == m-1 and y == n-1: return obs 
                    heapq.heappush(heap,[obs+ (grid[x][y]&1) ,(x,y)])
                    visited[x][y] = True
        return 0