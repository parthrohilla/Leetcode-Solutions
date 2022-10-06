class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1]*(n+2) for _ in range(n+2)]
        @lru_cache(None)
        def dfs(i,j):
            if i>j: return 0
            if memo[i][j] != -1: return memo[i][j]
            maxi = -math.inf
            for k in range(i,j+1):
                temp = nums[i-1]*nums[k]*nums[j+1] + dfs(i,k-1) + dfs(k+1,j)
                maxi = max(maxi, temp)
            memo[i][j] = maxi
            return memo[i][j]
        nums = [1] + nums + [1]
        return dfs(1,len(nums)-2)
                