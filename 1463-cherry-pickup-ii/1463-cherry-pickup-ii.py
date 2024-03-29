class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n,dp = len(grid), len(grid[0]), {}
        def dfs(i,j1,j2):
            if min(j1,j2)<0 or max(j1,j2)>=n: return -math.inf
            if (i,j1,j2) in dp: return dp[(i,j1,j2)]
            if i == m: return 0
            ans = 0
            for a in [-1,0,1]:
                for b in [-1,0,1]:
                    if j1 == j2: temp = grid[i][j1] + dfs(i+1,j1+a,j2+b)
                    else: temp = grid[i][j1] + grid[i][j2] + dfs(i+1,j1+a,j2+b)   
                    ans = max(ans, temp)
            dp[(i,j1,j2)] = ans
            return ans
            
        return dfs(0,0,n-1)