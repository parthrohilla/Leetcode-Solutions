class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        
        def dfs(i, subset):
            if i == len(nums):
                output.append(subset)
                return
            #include
            dfs(i+1, subset + [nums[i]])
            
            #exclude
            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i += 1
            dfs(i+1, subset)
        
        dfs(0, [])
        return output