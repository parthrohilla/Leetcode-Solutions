class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = ans = prefix =  0
        for r, num in enumerate(nums):
            prefix += num
            while num*(r-l+1) > prefix + k:
                prefix -= nums[l]
                l += 1
            ans = max(ans, r-l+1)
        return ans