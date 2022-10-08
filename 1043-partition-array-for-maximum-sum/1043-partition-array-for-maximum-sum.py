class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        memo = [-1]*n
        def dfs(i):
            if i == n: return 0
            if memo[i] != -1: return memo[i]
            
            maxi = 0
            for j in range(i, min(i+k,n)): 
                maxi = max(maxi, max(arr[i:j+1])*(j-i+1) + dfs(j+1))
            memo[i] = maxi
            return memo[i]
                
        return dfs(0)