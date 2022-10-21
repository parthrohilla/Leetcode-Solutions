class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp = sorted(nums)
        l = 0
        r = len(nums)-1
        while l < len(nums) and nums[l] == temp[l]:
            l += 1
        while r>=0 and nums[r] == temp[r]:
            r -= 1
        
        if l == len(nums): return 0
        return (r-l+1)
            