class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        skip_first = self.helper(0, nums[1:], {})
        skip_last = self.helper(0, nums[:-1], {})
        return max(skip_first, skip_last)
    
    def helper(self, i, nums, memo):
        if i >= len(nums):
            return 0
        if i in memo:
            return memo[i]
        
        memo[i] = max(nums[i] + self.helper(i+2, nums, memo), self.helper(i+1, nums, memo))
        return memo[i]