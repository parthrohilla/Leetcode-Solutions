class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        def dfs(r, prev):
            if r == n: return 0
            if (r,prev) in memo: return memo[(r,prev)]
            op1 = triangle[r][prev] + dfs(r+1,prev)
            op2 = triangle[r][prev+1] + dfs(r+1, prev+1)
            memo[(r,prev)] = min(op1, op2)
            return memo[(r,prev)]
        memo = {}
        return triangle[0][0] + dfs(1, 0)