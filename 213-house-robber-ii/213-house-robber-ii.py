class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(i, nums, memo):
            if i>=len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + helper(i+2, nums, memo) , helper(i+1, nums, memo))
            return memo[i]
            
        nums1, nums2 = nums[1:], nums[:-1]
        temp1 = helper(0, nums1, {})
        temp2 = helper(0, nums2, {})
        return max(temp1, temp2)
        