class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        seen = set()
        
        i, j = 0, len(nums)-1
        while i < j:
            if (nums[i] + nums[j]) not in seen:
                seen.add(nums[i] + nums[j])
            i += 1
            j -= 1
        
        return len(seen)