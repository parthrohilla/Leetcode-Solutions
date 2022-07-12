from functools import lru_cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        @lru_cache(None)
        def helper(index):
            if index >= len(nums):
                return False
            if index == len(nums)-1:
                return True 
            for i in range(nums[index], 0, -1):
                if helper(index + i):
                    return True   

            return False
        
        return helper(0)
            