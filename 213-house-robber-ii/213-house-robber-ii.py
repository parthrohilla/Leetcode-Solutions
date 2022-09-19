class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        memo = {}
        def dfs(i, end):
            if i > end: return 0
            if (i,end) in memo: return memo[(i,end)]
            memo[(i,end)] = max(nums[i] + dfs(i+2, end), dfs(i+1, end))
            return memo[(i,end)]
        
        return max(dfs(0,len(nums)-2),dfs(1,len(nums)-1))