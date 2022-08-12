class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 0
        while i < len(nums):
            if nums[i] != nums[j]:
                nums[j+1] = nums[i]
                j += 1
            i += 1
        return j+1