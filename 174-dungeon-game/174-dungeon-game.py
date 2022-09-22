class Solution:
    def calculateMinimumHP(self, grid: List[List[int]]) -> int:
        m,n, lookup = len(grid), len(grid[0]), {}
        def dfs(i,j):
            if (i,j) in lookup: return lookup[(i,j)]
            elif i == m-1 and j == n-1: return -grid[i][j]+1 if grid[i][j] < 0 else 1
            elif i == m-1: return max(1,dfs(i,j+1)-grid[i][j])
            elif j == n-1: return max(1,dfs(i+1,j)-grid[i][j])
            
            lookup[(i,j)] = max(1,min(dfs(i+1,j), dfs(i,j+1))-grid[i][j])
            return lookup[(i,j)]
        
        return dfs(0,0)