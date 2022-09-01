class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n = len(heights), len(heights[0])
        heap = [(0,0,0)]
        visited = set()
        res = 0
        
        while heap:
            diff, x, y = heapq.heappop(heap)
            visited.add((x,y))
            
            res = max(res,diff)
            if x == m-1 and y == n-1:
                return res
            
            for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                i,j = x+ dx, y + dy
                if i>=0 and i<m and j >=0 and j<n and (i,j) not in visited:
                    heapq.heappush(heap, (abs(heights[i][j] - heights[x][y]),i,j))
        return 0
        