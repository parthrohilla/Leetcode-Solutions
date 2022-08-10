class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        visited.add((0,0))
        heap = [[grid[0][0], 0, 0]]
        
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        while heap:
            height, x, y = heapq.heappop(heap)
            
            if x == n-1 and y == n-1:
                return height
            
            for i,j in directions:
                x1, y1 = x + i, y + j
                if (x1,y1) in visited or x1 not in range(n) or y1 not in range(n):
                    continue
                else:
                    visited.add((x1,y1))
                    heapq.heappush(heap, [max(grid[x1][y1], height), x1, y1])
        
        return -1