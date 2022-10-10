class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n, mod = len(grid), len(grid[0]), (10**9) + 7
        directions, ans = [[0,1], [0,-1], [1,0], [-1,0]], n*m
        
        @lru_cache(None)
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n: return 0
            count = 0
            for dx, dy in directions:
                x,y = i + dx, j + dy
                if self.isValid(x, y, m, n) and grid[x][y] > grid[i][j]:
                    count += (1 + dfs(x, y))
            return count % mod
        
        for i in range(m):
            for j in range(n):
                ans += dfs(i,j)
        return ans % mod
    
    def isValid(self, i, j, m, n):
        return 0<= i <m and 0<= j <n
        
                