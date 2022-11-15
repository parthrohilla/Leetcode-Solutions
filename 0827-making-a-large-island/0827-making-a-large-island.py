class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        parent = {}
        size = {}
        
        def find(x):
            if parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            x, y = find(a), find(b)
            if x == y: return
            parent[y] = x
            size[x] += size[y]
            size[y] = size[x]
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    parent[(i,j)] = (i,j)
                    size[(i,j)] = 1
        
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                        x, y = i + dx, j + dy
                        if 0<=x<m and 0<=y<n and (x,y) in seen:
                            union((i,j), (x,y))
                    seen.add((i,j))
                    
        curr_max_island = max(size.values()) if size else 0
        
        for i in range(m):
            for j in range(n):
                combined = 1
                if grid[i][j] == 0:
                    island_seen = set()
                    for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                        x, y = i + dx, j + dy
                        if 0<=x<m and 0<=y<n and grid[x][y] == 1 and find((x,y)) not in island_seen:
                            combined += size[find((x,y))]
                            island_seen.add(find((x,y)))
                    curr_max_island = max(curr_max_island, combined)
        
        return curr_max_island
                    
        
            
        
        
        
        
        
        
        
        