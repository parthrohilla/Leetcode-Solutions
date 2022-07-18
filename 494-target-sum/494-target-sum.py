class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n, memo = len(nums), {}
        
        def dfs(i, current):
            if i == n:
                if current == target:
                    return 1
                else:
                    return 0
            
            if (i, current) in memo:
                return memo[(i, current)]
            
            add = dfs(i+1, current + nums[i])
            subtract = dfs(i+1, current - nums[i])
            memo[(i, current)] = add + subtract
            return memo[(i, current)]
        
        return dfs(0, 0)