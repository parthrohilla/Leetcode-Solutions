class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1 house = 1 solution
        if len(nums) == 1:
            return nums[0]
        # rob all houses besides first to work around constraint
        skip_first = self.rob_helper(nums[1:], 0, {})
        # rob all houses besides last to work around constraint
        skip_last = self.rob_helper(nums[:-1], 0, {})
        return max(skip_first, skip_last)
        
    def rob_helper(self, houses, index, memo):
        if index >= len(houses):
            return 0
        
        if index not in memo:
            # option 1: rob current house and skip next one
            rob_current = houses[index] + self.rob_helper(houses, index + 2, memo)
            # option 2: skip current house and rob next one
            skip_current = self.rob_helper(houses, index + 1, memo)
            memo[index] = max(rob_current, skip_current)
        
        return memo[index]