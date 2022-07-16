class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -5
        current_max, current_min = 1, 1
        
        for n in nums:
            temp = current_max
            current_max = max(n, temp*n, current_min*n)
            current_min = min(n, temp*n, current_min*n)
            ans = max(ans, current_max)
        return ans