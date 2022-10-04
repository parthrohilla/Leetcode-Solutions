class Solution:
    def numTrees(self, N: int) -> int:
        memo = [-1]*(N+1)
        def f(n):
            if n <= 1: return 1
            if memo[n] != -1: return memo[n]
            count = 0
            for i in range(1,n+1):
                count += f(i-1)*f(n-i)
            memo[n] = count
            return count
        return f(N)