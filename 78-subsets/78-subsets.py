class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def helper(nums):
            if len(nums) == 0:
                return [[]]
                       
            output = []
            small = helper(nums[1:])
            for x in small:
                output.append(x)
                output.append([nums[0]] + x)
            
            return output
        
        return helper(nums)
            