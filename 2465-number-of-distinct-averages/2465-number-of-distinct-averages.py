class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        seen = set()
        ans = 0
        
        i, j = 0, len(nums)-1
        while i < j:
            if (nums[i] + nums[j]) not in seen:
                ans += 1
                seen.add(nums[i] + nums[j])
            i += 1
            j -= 1
        
        return ans