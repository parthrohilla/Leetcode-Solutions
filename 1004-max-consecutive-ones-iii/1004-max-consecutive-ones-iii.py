class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        freq = {}
        l, n = 0, len(nums)
        ans = 0
        
        for r, num in enumerate(nums):
            freq[num] = 1 + freq.get(num, 0)
            if freq.get(0,0) <= k:
                ans = max(ans, r-l+1)

            while 0 in freq and freq[0] > k:
                freq[nums[l]] -= 1
                l += 1
        return ans
                
            