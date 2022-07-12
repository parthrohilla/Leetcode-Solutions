class Solution:
    def canJump(self, nums: List[int]) -> bool:
        failed_index = [False] * len(nums)
        @lru_cache(None)
        def helper(index):
            if index >= len(nums) or failed_index[index]:
                return False
            if index == len(nums)-1:
                return True 
            for i in range(nums[index], 0, -1):
                if helper(index + i):
                    return True   
            failed_index[index] = True
            return False
        
        return helper(0)
            