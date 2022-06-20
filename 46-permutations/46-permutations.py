class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(nums):
            if len(nums) == 1:
                return [[nums[0]]]
            
            small = helper(nums[1:])
            output = []
            for subset in small:
                for i in range(len(subset)+1):
                    temp = subset.copy()
                    temp.insert(i, nums[0])
                    output.append(temp)
            return output
        
        return helper(nums)
                    