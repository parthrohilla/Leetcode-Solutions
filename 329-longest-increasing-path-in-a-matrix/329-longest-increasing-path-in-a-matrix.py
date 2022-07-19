class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo, m, n = {}, len(matrix), len(matrix[0])
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            current = 1
            if j+1 < n and matrix[i][j+1] > matrix[i][j]:
                right = 1 + dfs(i, j+1)
                current = max(current, right)
            
            if j-1 >= 0 and matrix[i][j-1] > matrix[i][j]:
                left = 1 + dfs(i, j-1)
                current = max(current, left)
                
            if i+1 < m and matrix[i+1][j] > matrix[i][j]:
                bottom = 1 + dfs(i+1, j)
                current = max(current, bottom)
                
            if i-1 >= 0 and matrix[i-1][j] > matrix[i][j]:
                top = 1 + dfs(i-1, j)
                current = max(current, top)
            
            memo[(i,j)] = current
            return memo[(i,j)]
            
            
        
        ans = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lip = dfs(i, j)
                ans = max(ans, lip)
        return ans
        