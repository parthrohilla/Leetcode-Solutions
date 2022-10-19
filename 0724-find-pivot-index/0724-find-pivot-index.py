class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        n, left, right = len(nums), [0]*n, [0]*n
        for i in range(1, n):
            left[i] = nums[i-1] + left[i-1]
            right[n-i-1] = nums[n-i] + right[n-i]
        
        for i in range(n):
            if left[i] == right[i]: 
                return i
        
        return -1