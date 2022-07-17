class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        curr, ans = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1
                ans = max(ans, curr)
            else:
                curr = 1
        return ans
            