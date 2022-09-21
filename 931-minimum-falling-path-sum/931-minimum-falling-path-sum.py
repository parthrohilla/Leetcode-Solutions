class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        def dfs(i,j):
            if j<0 or j>=n: return math.inf
            if i == m: return 0
            if (i,j) in memo: return memo[(i,j)]
            memo[(i,j)] = matrix[i][j] + min(dfs(i+1,j-1), dfs(i+1, j), dfs(i+1,j+1))
            return memo[(i,j)]
        ans, memo = math.inf, {}
        for j in range(n):
            ans = min(ans, dfs(0,j))
        return ans