class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def dfs(i, subset):
            if i == len(nums):
                output.append(subset)
                return
            
            dfs(i+1, subset + [nums[i]])
            dfs(i+1, subset)
        
        dfs(0, [])
        return output