class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        @lru_cache(None)
        def dfs(i):
            if i == n: return 0
            
            maxi = 0
            for j in range(i, min(i+k,n)):
                a = arr[i:j+1]
                temp = max(a)*(j-i+1) + dfs(j+1)
                maxi = max(maxi, temp)
            return maxi
                
        return dfs(0)