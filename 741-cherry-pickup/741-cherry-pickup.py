class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, lookup = len(grid), {}
        def dfs(x1,y1,x2,y2):
            if (x1,y1,x2,y2) == (n-1,n-1,n-1,n-1): return grid[x1][y1]
            if max(x1,y1,x2,y2) >= n or grid[x1][y1] == -1 or grid[x2][y2] == -1 : return -math.inf
            if (x1,y1,x2,y2) in lookup: return lookup[(x1,y1,x2,y2)]
            
            ans = 0
            if x1 == x2 and y1 == y2: ans += grid[x1][y1]
            else: ans += grid[x1][y1] + grid[x2][y2]
            ans += max(dfs(x1,y1+1,x2,y2+1), dfs(x1+1,y1,x2+1,y2), dfs(x1+1,y1,x2,y2+1), dfs(x1,y1+1,x2+1,y2))
            lookup[(x1,y1,x2,y2)] = ans
            return ans
        
        res = dfs(0,0,0,0)
        return res if res > 0 else 0