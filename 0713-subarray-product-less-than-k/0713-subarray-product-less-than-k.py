class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = l = 0
        prefix = 1
        
        if k <= 1:
            return 0
        
        for r, num in enumerate(nums):
            prefix *= num
            while l < r and prefix >= k:
                prefix /= nums[l]
                l += 1
            if prefix < k:
                ans += (r - l + 1)
        
        return ans
        