class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        
        def helper(index) -> int:
            if index >= n-1:
                return 0
            if index in cache:
                return cache[index]
            
            jumps = math.inf
            for i in range(1, nums[index]+1):
                jumps = min(jumps, 1 + helper(index+i))
            
            cache[index] = jumps
            return jumps
        
        return helper(0)