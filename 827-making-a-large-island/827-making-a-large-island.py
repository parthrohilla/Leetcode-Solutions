class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, island, seen = len(grid), 2, {}
        
        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=n or grid[i][j] != 1: return 0
            grid[i][j] = island
            res = 1
            for dx,dy in [[0,1], [1,0], [-1,0], [0,-1]]:
                x,y = i + dx, j + dy
                res += dfs(x,y)
            return res
        
        def helper(i,j):
            temp = 1
            s = set()
            for dx,dy in [[0,1], [1,0], [-1,0], [0,-1]]:
                x,y = i + dx, j + dy
                if not(x<0 or x>=n or y<0 or y>=n) and grid[x][y] > 1 and grid[x][y] not in s:
                    s.add(grid[x][y])
                    temp += seen.get(grid[x][y], 0)
            return temp

        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    val = dfs(i,j)
                    seen[island] = val
                    island += 1
                    
        ans = max(seen.values()) if seen else 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    ans = max(ans,helper(i,j))
        
        return ans
        
        
        
        
        
        