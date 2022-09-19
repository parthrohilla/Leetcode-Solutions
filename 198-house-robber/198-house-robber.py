class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, prev2 = nums[0],0
        for i in range(1,len(nums)):
            curr = max(nums[i] + prev2, prev)
            prev2 = prev
            prev = curr
        return prev