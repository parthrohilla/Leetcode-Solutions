class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        memo = {}
        @lru_cache(None)
        def helper(i, robbedFirst):
            if i>=n or (i==n-1 and robbedFirst):
                return 0
            if i in memo:
                memo[i]
            
            memo[i] = max(nums[i] + helper(i+2, robbedFirst) , helper(i+1, robbedFirst))
            return memo[i]
            
            
        return max(helper(1, False),nums[0] + helper(2, True))