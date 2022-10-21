class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp = sorted(nums)
        l = 0
        r = len(nums)-1
        while l < len(nums) and nums[l] == temp[l]: l += 1
        while r>=0 and nums[r] == temp[r]: r -= 1
        return 0 if l == len(nums) else (r-l+1)
            