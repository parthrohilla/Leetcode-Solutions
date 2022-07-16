class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) 
        if target % 2 == 1:
            return False
        
        memo = {}
        target = target // 2
        
        def dfs(i, needed):
            if needed == 0:
                return True
            if i >= len(nums) or needed < 0:
                return False
            if (i, needed) in memo:
                return memo[(i, needed)]
            
            memo[((i, needed))] = dfs(i+1, needed - nums[i]) or dfs(i+1, needed)
            return memo[((i, needed))]
        
        return dfs(0, target)