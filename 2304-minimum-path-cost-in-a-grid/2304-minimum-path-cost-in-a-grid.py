class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m,n,lookup = len(grid), len(grid[0]), {}
        def dfs(i,j):
            if i == m-1: return grid[i][j]
            if (i,j) in lookup: return lookup[(i,j)]
            
            val, res = grid[i][j], math.inf
            for col in range(n):
                res = min(res, grid[i][j] + dfs(i+1,col) + moveCost[val][col])
            lookup[(i,j)] = res
            return lookup[(i,j)]
        
        ans = math.inf
        for c in range(n):
            ans = min(ans, dfs(0,c))
        return ans