class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[0,1], [0,-1], [-1,0], [1,0]]
        # DFS for finding 1st Island
        def dfs(i, j):
            if i<0 or i>=n or j<0 or j>=n or grid[i][j] != 1:
                return
            grid[i][j] = 2
            for dx, dy in directions:
                x,y = i + dx, j + dy
                dfs(x,y)
            return
        
        #BFS for finding bridge length 
        def bfs():
            d = 0
            while q:
                k = len(q)
                for _ in range(k):
                    x, y = q.popleft()
                    for dx, dy in directions:
                        a, b = x + dx, y + dy
                        if a>=0 and a<n and b>=0 and b<n and (a,b) not in visited:
                            if grid[a][b] == 2:
                                return d
                            else:
                                q.append((a,b))
                                visited.add((a,b))
                d += 1
                                     
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    x,y = i,j
                    
        # Calling Dfs to turn 1st island to 2
        dfs(x,y)
        
        q = deque()
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    visited.add((i,j))
                    q.append((i,j))
        
        
        return bfs()
        
            
            