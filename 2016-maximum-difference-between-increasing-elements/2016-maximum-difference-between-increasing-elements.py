class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        smallest = nums[0]
        ans = 0
        for num in nums[1:]:
            ans = max(ans, num - smallest)
            smallest = min(smallest, num)
        
        return ans if ans else -1