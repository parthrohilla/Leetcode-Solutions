class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2: return False
        if k == 1: return True
        
        seen = {0:-1}
        prefix = 0
        
        for i, num in enumerate(nums):
            prefix += num
            
            if num == 0:
                if i >= 1 and nums[i-1] == 0: return True
                else: continue
            
            m = 1
            while m*k <= prefix:
                needed = prefix - m * k
                if needed in seen and i - seen[needed] >= 2:
                    return True
                else: m += 1
            
            seen[prefix] = i
        
        return False
            