class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = prefix = ans = 0
        for r, num in enumerate(nums):
            while prefix & num:
                prefix ^= nums[l]
                l += 1
            prefix |= num
            ans = max(ans, r-l+1)
            
        return ans