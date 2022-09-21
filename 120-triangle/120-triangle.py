class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n, memo = len(triangle), {}
        def dfs(i,j):
            if i == n: return 0
            if (i,j) in memo: return memo[(i,j)]
            memo[(i,j)] = triangle[i][j] + min(dfs(i+1,j), dfs(i+1,j+1))
            return memo[(i,j)]
        return dfs(0,0)