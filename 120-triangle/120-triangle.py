class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n, memo = len(triangle), {}
        def dfs(r, prev):
            if r == n: return 0
            if (r,prev) in memo: return memo[(r,prev)]
            memo[(r,prev)] = min(triangle[r][prev] + dfs(r+1,prev), triangle[r][prev+1] + dfs(r+1, prev+1))
            return memo[(r,prev)]
        return triangle[0][0] + dfs(1, 0)