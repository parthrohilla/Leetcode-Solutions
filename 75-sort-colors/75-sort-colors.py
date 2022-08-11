class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        i,j = 0, len(nums)-1
        while k <= j:
            if nums[k] == 0:
                nums[i], nums[k] = 0, nums[i]
                i += 1
                k += 1
            elif nums[k] == 2:
                nums[j], nums[k] = 2, nums[j]
                j -= 1
            else:
                k += 1
            
            
        