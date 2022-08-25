class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow, fast = 0, 0
        for fast, num in enumerate(nums):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
            
            if nums[slow] != 0:
                slow += 1
        return
            
            
        