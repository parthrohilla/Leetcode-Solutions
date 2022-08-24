class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modification = False
        
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            elif nums[i] > nums[i+1] and not modification:
                modification = True
                if (i-1 >= 0 and nums[i-1] <= nums[i+1]) or i == 0:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
            else:
                return False
            
        return True