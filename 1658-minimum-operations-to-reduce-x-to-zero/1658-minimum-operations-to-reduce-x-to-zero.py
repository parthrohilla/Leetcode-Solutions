class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        P = {}
        running = 0
        P[0] = 0
        
        for i, num in enumerate(nums):
            running += num
            P[running] = i + 1
            
        running = 0
        ans = math.inf
        
        if x in P:
            ans = min(ans, P[x])
        
        for j, num in enumerate(nums[::-1]):
            running += num
            
            if running == x:
                ans = min(ans, j+1)
            
            if x - running in P and P[x-running] + j + 1 < len(nums):
                ans = min(ans, P[x-running] + j + 1)
            
        return ans if ans < math.inf else -1