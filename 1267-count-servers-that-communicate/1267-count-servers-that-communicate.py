class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        row_map = defaultdict(int)
        col_map = defaultdict(int)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_map[i] += 1
                    col_map[j] += 1
        
        connected = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_map[i] > 1 or col_map[j] > 1):
                    connected += 1
        return connected
                        
                    
        
        