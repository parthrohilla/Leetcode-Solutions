class Solution:
    def numTrees(self, N: int) -> int:
        @lru_cache(None)
        def f(n):
            if n <= 1: return 1
            count = 0
            for i in range(1,n+1):
                count += f(i-1)*f(n-i)
            return count
        return f(N)