class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        row_map = defaultdict(list)
        col_map = defaultdict(list)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_map[i].append((i,j))
                    col_map[j].append((i,j))
        
        connected = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if len(row_map[i]) > 1 or len(col_map[j]) > 1:
                        connected.add((i,j))
        return len(connected)
                        
                    
        
        