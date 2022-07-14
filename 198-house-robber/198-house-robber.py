class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)

        def helper(i):
            if i >= n:
                return 0
            if i in dp:
                return dp[i]
            
            dp[i] = max(nums[i] + helper(i + 2), helper(i + 1))
            return dp[i]
        
        return helper(0)