class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        @lru_cache(None)
        def dfs(A):
            ans = 0
            if len(A) > 1 and A[0] != A[-1]:
                ans = max(ans, len(A)-1)
            else:
                ans = max(ans, dfs(A[:-1]), dfs(A[1:]))
            return ans
        
        return dfs(tuple(colors))
    