class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        running = previous = 0
        seen = set()
        
        for num in nums:
            running += num
            running %= k
            
            if running in seen:
                return True
            
            seen.add(previous)
            previous = running
            
        return False
            