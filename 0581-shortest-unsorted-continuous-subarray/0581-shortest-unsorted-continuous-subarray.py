class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # temp = sorted(nums)
        # l = 0
        # r = len(nums)-1
        # while l < len(nums) and nums[l] == temp[l]: l += 1
        # while r>=0 and nums[r] == temp[r]: r -= 1
        # return 0 if l == len(nums) else (r-l+1)
        if len(nums) <= 1: return 0
        
        mini = math.inf
        maxi = -math.inf
        for i, num in enumerate(nums):
            if i == 0 and num > nums[i+1]:
                mini = min(mini, num)
                maxi = max(maxi, num)
            elif i == len(nums) - 1 and num < nums[i-1]:
                mini = min(mini, num)
                maxi = max(maxi, num)        
            elif 0 < i < len(nums)-1:
                if num < nums[i-1] or num > nums[i+1]:
                    mini = min(mini, num)
                    maxi = max(maxi, num)
        
        left = 0
        right = len(nums)-1
        while left < len(nums) and nums[left] <= mini: left += 1
        while right >= 0 and nums[right] >= maxi: right -= 1
        
        ans = right - left + 1
        return ans if ans > 0 else 0
        
        
            