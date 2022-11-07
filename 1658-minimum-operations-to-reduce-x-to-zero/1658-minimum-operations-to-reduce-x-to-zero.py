class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        P = {}
        prefix_left = 0
        P[0] = 0
        
        for i, num in enumerate(nums):
            prefix_left += num
            P[prefix_left] = i + 1
            
        prefix_right = 0
        ans = math.inf
        
        if x in P:
            ans = min(ans, P[x])
        
        for j, num in enumerate(nums[::-1]):
            prefix_right += num
            
            if prefix_right == x:
                ans = min(ans, j+1)
            
            if x - prefix_right in P and P[x-prefix_right] + j + 1 < len(nums):
                ans = min(ans, P[x-prefix_right] + j + 1)
            
        return ans if ans < math.inf else -1