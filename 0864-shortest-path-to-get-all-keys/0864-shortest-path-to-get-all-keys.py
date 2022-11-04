class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m,n = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        
        startx, starty, totalK = 0, 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    startx, starty = i, j
                elif grid[i][j] in "abcdef":
                    totalK += 1
        
        Q = deque()
        Q.append([startx,starty,".@abcdef",0, 0])
        visited = set()
        
        while Q:
            i, j, string, steps, keys = Q.popleft()
            
            if grid[i][j] in "abcdef" and grid[i][j].upper() not in string:
                string += grid[i][j].upper()
                keys += 1
            
            if keys == totalK:
                return steps
            
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0<=x<m and 0<=y<n:
                    if grid[x][y] in "@.ABCDEFabcdef" and grid[x][y] in string:
                        if (x,y,string) not in visited:
                            Q.append([x,y,string,steps+1,keys])
                            visited.add((x,y,string))
            
        return -1
                        