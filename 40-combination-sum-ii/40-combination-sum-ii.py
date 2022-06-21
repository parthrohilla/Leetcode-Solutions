class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        
        def dfs(i, total, subset):
            if total == target:
                output.append(subset)
                return
            
            if total > target or i>=len(nums):
                return
            
            #include
            dfs(i+1, total+nums[i], subset + [nums[i]])
            
            #exclude
            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i += 1
            dfs(i+1, total, subset)
        
        dfs(0, 0, [])
        return output
            