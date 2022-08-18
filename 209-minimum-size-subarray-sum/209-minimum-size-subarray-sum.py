class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        ans = math.inf
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                ans = min(ans, r-l+1)
                total -= nums[l]
                l += 1
                
        return ans if ans != math.inf else 0